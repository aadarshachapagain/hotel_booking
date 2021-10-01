$(document).ready(function () {
    $('.count').prop('disabled', true);
    $(document).on('click', '.plus', function () {
        $('.count').val(parseInt($('.count').val()) + 1);
    });
    $(document).on('click', '.minus', function () {
        $('.count').val(parseInt($('.count').val()) - 1);
        if ($('.count').val() <= 0) {
            $('.count').val(0);
        }
    });

    $("#clone_form").on('submit', function (e) {
        updated_count = $('#qty').val();
        $('#count').val(updated_count);
    });


    // $('.populate_count').
});
