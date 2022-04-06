/*!
* Start Bootstrap - Business Frontpage v5.0.8 (https://startbootstrap.com/template/business-frontpage)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-frontpage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

$("#rsaForm").submit(function (e) {
    // preventing from page reload and default actions
    e.preventDefault();
    // serialize the data for sending the form data.
    var serializedData = $(this).serialize();

    // make POST ajax call
    $.ajax({
        type: 'POST',
        data: serializedData,
        success: function (response) {
            // on successfull creating object
            // display the info from backend.
            ciphertext = response['ciphertext']
            $('#ciphertext').val(ciphertext);
            console.log(response['ciphertext'])
        },
        error: function (response) {
            // alert the error if any error occured
            alert(response["responseJSON"]["error"]);
        }
    })
})


/*
$(document).ready(function () {
    $(function() {
        $("#rsaForm").submit(function(event) {
            // Stop form from submitting normally
            event.preventDefault();
            var rsaForm = $(this);
            
            // Send the data using post
            var posting = $.post( rsaForm.attr('action'), rsaForm.serialize() );
            // if success:
            posting.done(function(data) {
                alert('Encriptado.');
            });
            // if failure:
            posting.fail(function(data) {
                // 4xx or 5xx response, alert user about failure
            });
        });
    });

    $(function() {
        $("#rabinForm").submit(function(event) {
            // Stop form from submitting normally
            event.preventDefault();
            var rsaForm = $(this);
            // Send the data using post
            var posting = $.post( rsaForm.attr('action'), rsaForm.serialize() );
            // if success:
            posting.done(function(data) {
                alert('Encriptado.');
            });
            // if failure:
            posting.fail(function(data) {
                // 4xx or 5xx response, alert user about failure
            });
        });
    });
});
*/