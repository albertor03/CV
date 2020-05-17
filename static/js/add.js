$(document).ready(function () {
    $('#addItem').on('click', function () {
        $('#itemForm').toggleClass('d-none');
    });
    $('#editInfo').on('click', function () {
        $('#configForm').toggleClass('d-none');
        if (! $('#passForm').hasClass('d-none')){
            $('#passForm').toggleClass('d-none');
        }
    });
    $('#editPass').on('click', function () {
        $('#passForm').toggleClass('d-none');
        if (!$('#configForm').hasClass('d-none')){
            $('#configForm').toggleClass('d-none');
        }
    });
  
});