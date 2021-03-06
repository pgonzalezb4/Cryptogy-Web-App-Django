/*!
* Start Bootstrap - Business Frontpage v5.0.8 (https://startbootstrap.com/template/business-frontpage)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-frontpage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


$(document).ready(function () {
    $("#rsaForm").on("submit", function (e) {
        // preventing from page reload and default actions
        e.preventDefault();
        // serialize the data for sending the form data.
        var serializedData = $(this).serialize();
    
        // make POST ajax call
        $.ajax({
            type: 'POST',
            url: "",
            data: serializedData,
            success: function (response) {
                // on successfull creating object
                // display the info from backend.

                console.log("Proceso:")
                if (Object.keys(response).indexOf('ciphertext') != -1) {
                    ciphertext = response['ciphertext'];
                    console.log(ciphertext);
                    $('#ciphertextarea').val(response['ciphertext']);
                    $('#primep').val(response['pParam']);
                    $('#primeq').val(response['qParam']);
                }
                
                else if (Object.keys(response).indexOf('cleartext') != -1) {
                    cleartext = response['cleartext'];
                    console.log(cleartext);
                    $('#cleartextarea').val(response['cleartext']);
                }
    
                else {
                    cleartext = response['error'];
                    console.log(cleartext);
                    $('#ciphertextarea').val(cleartext);
                    $('#cleartextarea').val(cleartext);
                }
                
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        })
    })
});

$(document).ready(function () {
    $("#rabinForm").on("submit", function (e) {
        // preventing from page reload and default actions
        e.preventDefault();
        // serialize the data for sending the form data.
        var serializedData = $(this).serialize();
    
        // make POST ajax call
        $.ajax({
            type: 'POST',
            url: "",
            data: serializedData,
            success: function (response) {
                // on successfull creating object
                // display the info from backend.

                console.log("Proceso:")
                console.log(response)
                if (Object.keys(response).indexOf('ciphertext') != -1) {
                    ciphertext = response['ciphertext'];
                    pParam = response['pParam'];
                    qParam = response['qParam'];
                    console.log(pParam);
                    console.log(qParam);
                    console.log(ciphertext);
                    $('#ciphertextarea').val(ciphertext);
                    $('#primeprabin').val(pParam);
                    $('#primeqrabin').val(qParam);
                }
                
                else if (Object.keys(response).indexOf('cleartext') != -1) {
                    cleartext = response['cleartext'];
                    cleartext = decodeURI(cleartext)
                    cleartext = cleartext.trim()
                    $('#cleartextarea').val(cleartext);
                }
    
                else {
                    cleartext = response['error'];
                    console.log(cleartext);
                    $('#ciphertextarea').val(cleartext);
                    $('#cleartextarea').val(cleartext);
                }
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        })
    })
});

$(document).ready(function () {
    $("#mvForm").on("submit", function (e) {
        // preventing from page reload and default actions
        e.preventDefault();
        // serialize the data for sending the form data.
        var serializedData = $(this).serialize();
    
        // make POST ajax call
        $.ajax({
            type: 'POST',
            url: "",
            data: serializedData,
            success: function (response) {
                // on successfull creating object
                // display the info from backend.


                console.log("Proceso:")
                console.log(response)
                if (Object.keys(response).indexOf('ciphertext') != -1) {
                    ciphertext = response['ciphertext'];
                    console.log(ciphertext);
                    $('#ciphertextarea').val(response['ciphertext']);
                    $('#pubkey').val(response['alpha']);
                    $('#privkey').val(response['k']);
                }
                
                else if (Object.keys(response).indexOf('cleartext') != -1) {
                    cleartext = response['cleartext'];
                    console.log(cleartext);
                    $('#cleartextarea').val(response['cleartext']);
                }
    
                else {
                    cleartext = response['error'];
                    console.log(cleartext);
                    $('#ciphertextarea').val(cleartext);
                    $('#cleartextarea').val(cleartext);
                }
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        })
    })
});

$(document).ready(function () {
    $("#gammalForm").on("submit", function (e) {
        // preventing from page reload and default actions
        e.preventDefault();
        // serialize the data for sending the form data.
        var serializedData = $(this).serialize();
    
        // make POST ajax call
        $.ajax({
            type: 'POST',
            url: "",
            data: serializedData,
            success: function (response) {
                // on successfull creating object
                // display the info from backend.
                console.log("Proceso...")
                console.log(response)
                if (Object.keys(response).indexOf('ciphertext') != -1) {
                    ciphertext = response['ciphertext'];
                    console.log(ciphertext);
                    $('#ciphertextarea').val(response['ciphertext']);
                }
                
                else if (Object.keys(response).indexOf('cleartext') != -1) {
                    cleartext = response['cleartext'];
                    console.log(cleartext);
                    $('#cleartextarea').val(response['cleartext']);
                }
    
                else {
                    cleartext = response['error'];
                    console.log(cleartext);
                    $('#ciphertextarea').val(cleartext);
                    $('#cleartextarea').val(cleartext);
                }

                // Setear claves
                console.log('Settings keys...');

                if ($('#pubkey').val() == '' && $('#privkey').val() == '') {
                    publickey = response['pubkey'];
                    privatekey = response['privkey'];
                    $('#pubkey').val(publickey);
                    $('#privkey').val(privatekey);
                }
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        })
    })
});

// ESQUEMAS DE FIRMA DIGITAL
$(document).ready(function () {
    $("#rsaDSSForm").on("submit", function (e) {
        // preventing from page reload and default actions
        e.preventDefault();
        // serialize the data for sending the form data.
        var serializedData = $(this).serialize();        
        s_text = e.target.value;
    
        // make POST ajax call
        $.ajax({
            type: 'POST',
            url: "",
            data: serializedData,
            success: function (response) {
                // on successfull creating object
                // display the info from backend. 
                console.log("Proceso:")
                if (Object.keys(response).indexOf('signature') != -1) {
                    signature = response['signature'];
                                                         
                    $('#signaturearea').val(signature);
                    $('#primep').val(response['pParam']);
                    $('#primeq').val(response['qParam']);
                    document.getElementById("isvalid-message").innerHTML  = "";
                }
                
                else if (Object.keys(response).indexOf('isValid') != -1) {
                    isValid = response['isValid'];
                    console.log(isValid);
                    document.getElementById("isvalid-message").innerHTML  = isValid;
                }
    
                else {
                    error = response['error'];
                    console.log(error);
                    $('#signaturearea').val(error);
                    $('#messagearea').val(error);
                }
                
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        })
    })
});

// ESQUEMAS DE FIRMA DIGITAL
$(document).ready(function () {
    $("#gammalDSSForm").on("submit", function (e) {
        // preventing from page reload and default actions
        e.preventDefault();
        // serialize the data for sending the form data.
        var serializedData = $(this).serialize();
    
        // make POST ajax call
        $.ajax({
            type: 'POST',
            url: "",
            data: serializedData,
            success: function (response) {
                // on successfull creating object
                // display the info from backend.

                console.log("Proceso:")
                if (Object.keys(response).indexOf('signature') != -1) {
                    signature = response['signature'];
                    console.log(signature);
                    $('#signaturearea').val(signature);
                    document.getElementById("isvalid-message").innerHTML  = "";
                }
                
                else if (Object.keys(response).indexOf('isValid') != -1) {
                    isValid = response['isValid'];
                    console.log(isValid);
                    // $('#isvalid-message').val(response['isValid']);
                    document.getElementById("isvalid-message").innerHTML  = isValid;
                }
    
                else {
                    error = response['error'];
                    console.log(error);
                    $('#signaturearea').val(error);
                    $('#messagearea').val(error);
                }

                // Setear claves
                console.log('Settings keys...');

                if ($('#pubkey').val() == '' && $('#privkey').val() == '') {
                    publickey = response['pubkey'];
                    privatekey = response['privkey'];
                    $('#pubkey').val(publickey);
                    $('#privkey').val(privatekey);
                }
                
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        })
    })
});


// Mostrar la imagen una vez es cargada
function readImage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
    
        reader.onload = function (e) {
            $('#clearimageupload').attr('src', e.target.result);
        };
    
        reader.readAsDataURL(input.files[0]);
    }
}

// Mostrar la imagen una vez es cargada
function readT1Image(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
    
        reader.onload = function (e) {
            $('#cipherimaget1area').attr('src', e.target.result);
        };
    
        reader.readAsDataURL(input.files[0]);
    }
}

// Mostrar la imagen una vez es cargada
function readT2Image(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
    
        reader.onload = function (e) {
            $('#cipherimaget2area').attr('src', e.target.result);
        };
    
        reader.readAsDataURL(input.files[0]);
    }
}

// Read File for Digital Signature Scheme and encode to paste in #messagearea.
const fileInput = document.getElementById("clearFile");
fileInput.addEventListener('change', (e) => {
    // Get a reference to the file
    const file = e.target.files[0];

    // Encode the file using the FileReader API
    const reader = new FileReader();
    reader.onloadend = () => {
        // Use a regex to remove data url part
        const base64String = reader.result
            .replace('data:', '')
            .replace(/^.+,/, '');

            $('#messagearea').val(base64String.substring(0, 10000));
        // Logs wL2dvYWwgbW9yZ...
    };
    reader.readAsDataURL(file);
});


