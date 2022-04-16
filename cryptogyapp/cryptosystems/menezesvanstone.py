import random

# import networkx as nx

# plt.rcParams["figure.figsize"] = (25, 25)

class MenezesVanstoneCipher():
    with open("cryptogyapp/cryptosystems/gammapentagonalgrapha.txt", "r") as f:
        data = f.read()
    a = eval(data)

    with open("cryptogyapp/cryptosystems/gammapentagonalgraphb.txt", "r") as f:
        data = f.read()
    b = eval(data)

    graphs = [a, b]

    with open("cryptogyapp/cryptosystems/gammapentagonalgraphasmall.txt", "r") as f:
        data = f.read()
    asmall = eval(data)

    with open("cryptogyapp/cryptosystems/gammapentagonalgraphbsmall.txt", "r") as f:
        data = f.read()
    bsmall = eval(data)

    graphssmall = [asmall, bsmall]

    curgraph = 0

    """
    Unused: Graph is hardcoded now.

    @staticmethod
    def generateMatrix(h = 50, w = 50):
        # Inicializacion de Diccionarios
        points = {(0,0):[]}
        originpoints = [(0,0)]
        # Iterar por anchura.
        for x in range(w):
            # Crear lista temporal para actualizar puntos de origen.
            pointsnew = []
            # Iterar por los puntos de origen. (Aquellos puntos de los cuales deben comenzar nuevas ramas.)
            for point in originpoints:
                j = point[1]
                # Iterar por altura.
                for i in range(1, h):
                    # Actualizar diccionario de puntos.
                    if (point[0] + i, j) in points:
                        if (point[0] + i - 1, j - i + 1) not in points[(point[0] + i, j)]:
                            points[(point[0] + i, j)].append((point[0] + i - 1, j - i + 1))
                    else:
                        points[(point[0] + i, j)] = [(point[0]+i-1, j-i+1)]
                    # Si el punto es de origen, agregarlo.
                    if point[0] / 2 == point[1] and (point[0] + i, j) not in originpoints:
                        pointsnew.append((point[0] + i - 1, j - i + 1))
                    j += i
            originpoints = pointsnew[1:]
        return points
    """

    @staticmethod
    def shiftEncrypt(text: str, key: int):
        """
        Cifrado de desplazamiento simple para caracteres.
        """
        return chr(((ord(text.lower()) - 97 + key) % 26) + 65)

    def __init__(self, key=None):
        super().__init__()
        self.key = self.generateRandomKey(key)
        self.dicts = None
        self.points = MenezesVanstoneCipher.graphs[MenezesVanstoneCipher.curgraph]
        self.pointssmall = MenezesVanstoneCipher.graphssmall[
            MenezesVanstoneCipher.curgraph
        ]

    def getRouteKey(self, Xi, Yi, coord):
        a, b = coord
        coord = (a - Xi, b - Yi)

        if coord in self.points:
            return len(self.points[coord])
        else:
            return 0

    def generateDicts(self):
        Xi, Yi = self.key[:2]
        perm = self.key[2:]

        ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # Primero desplazamos por la permutacion, y luego desplazamos por el numero de trayectorias.
        dicts = [
            [
                MenezesVanstoneCipher.shiftEncrypt(
                    MenezesVanstoneCipher.shiftEncrypt(ABC[l], perm[k]),
                    MenezesVanstoneCipher.getRouteKey(self, Xi, Yi, (k, l)),
                )
                for l in range(26)
            ]
            for k in range(len(perm))
        ]
        return dicts

    def validKey(self, key):
        if len(key) <= 3:
            return False
        if all((0 <= x and x <= 25) for x in key[2:]):
            return True
        return False

    def generateRandomKey(self, keyParam):
        if keyParam is None:
            key = list()
            for i in range(2):
                key.append(random.randint(-25, 25))
            for i in range(random.randint(5, 15)):
                rand_number = random.randint(0, 25)
                key.append(rand_number)
            print("Key:", key, len(key))
            return key
        else:
            return keyParam

    def encode(self, cleartext: str):
        self.dicts = MenezesVanstoneCipher.generateDicts(self)
        perm = self.key[2:]
        ciphertext = ""
        x = 0
        for l in cleartext:
            xi = x
            while self.dicts[x // 26][x % 26] != l.upper():
                x = (x + 1) % (26 * len(perm))
                if x == xi:  # Puede suceder que una letra no este en los diccionarios
                    return False
            ciphertext += "(" + str(x // 26) + ", " + str(x % 26) + ");"
        return ciphertext[:-1]

    def decode(self, ciphertext):
        self.dicts = MenezesVanstoneCipher.generateDicts(self)
        cleartext = ""
        for x in ciphertext.split(";"):
            a, b = x[1:-1].split(", ")
            cleartext += self.dicts[int(a)][int(b)]
        return cleartext

    def changeGraph(self):
        MenezesVanstoneCipher.curgraph = (MenezesVanstoneCipher.curgraph + 1) % 2
        #print(MenezesVanstoneCipher.curgraph)


# def showGraph(key, filename: str):
#     pointssmall = MenezesVanstoneCipher.graphssmall[MenezesVanstoneCipher.curgraph]
#     #print("asdf")
#     #print(type(key))
#     key = [int(x) for x in key.split(",")]
#     #print(key)
#     Xi, Yi = key[:2]
#     # Generar grafo en networkx.
#     g = nx.DiGraph()
#     keysn = [tuple(map(lambda i, j: i + j, x, (Xi, Yi))) for x in pointssmall.keys()]
#     g.add_nodes_from(keysn)
#     for k, v in pointssmall.items():
#         kn = tuple(map(lambda i, j: i + j, k, (Xi, Yi)))
#         vn = [tuple(map(lambda i, j: i + j, t, (Xi, Yi))) for t in v]
#         g.add_edges_from(([(t, kn) for t in vn]))

#     # Definir las posiciones de los nodos.
#     pos = {(x, y): (x, y) for x, y in g.nodes()}

    # Dibujar el grafo.
    # nx.draw_networkx(g, pos=pos, node_size=500)

    # # Opciones de grafica.
    # plt.gca().set_aspect("equal")
    # plt.gca().set_xlim([-25, 25])
    # plt.gca().set_ylim([-25, 25])
    # plt.gca().axhline(y=0, lw=2, color="k")
    # plt.gca().axvline(x=0, lw=2, color="k")
    # plt.grid("on")
    # plt.tight_layout()
    # plt.savefig(filename)
    # plt.gca().clear()
    # plt.close()
    # 
    #print("printed")
    # return True


if __name__ == "__main__":

    # key = 
    cleartext = "hola como vas"
    cleartext = cleartext.split(" ")

    cipher = MenezesVanstoneCipher([13, -3, 18, 4, 0, 15, 17, 0, 5, 15])
    print("cleartext: ")
    print(cleartext)
    ciphertext = []
    for text in cleartext:
        ciphertext.append(cipher.encode(text))

    ciphertext = '  '.join(ciphertext)
    print("ciphertext: ")
    print(ciphertext, type(ciphertext))

    print("desencriptado:")
    ciphertext = ciphertext.split('  ')

    cleartext = []
    for text in ciphertext:
        print("text", text)
        cleartext.append(cipher.decode(text))

    cleartext = ' '.join(cleartext)
    print(cleartext)