$(document).ready(function () {
    $('#addItem').on('click', function () {
        $('#itemForm').toggleClass('d-none');
    });
    $('#addSection').on('click', function () {
        $('#sectionForm').toggleClass('d-none');
        if (! $('#courseForm').hasClass('d-none')){
            $('#courseForm').toggleClass('d-none');
        }
    });
    $('#addCourse').on('click', function () {
        $('#courseForm').toggleClass('d-none');
        if (! $('#sectionForm').hasClass('d-none')){
            $('#sectionForm').toggleClass('d-none');
        }
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