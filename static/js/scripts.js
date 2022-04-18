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
                    $('#key').val(response['key']);
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