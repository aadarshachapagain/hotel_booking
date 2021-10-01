$(document).ready(function () {
    $('.select_all').on('click', function () {
        if (this.checked) {
            $(this).parent().parent().parent().children('tr').each(function () {
                $(this).children().children().find('input').prop('checked', true)
            });
        } else {
            $(this).parent().parent().parent().children('tr').each(function () {
                $(this).children().children().find('input').prop('checked', false)
            });
        }
    });

    $('input[name="hotelinventory"]').on('click', function () {
        if ($('input[name="hotelinventory"][checked]').length == $('input[name="hotelinventory"]').length) {
             $(this).parent().parent().parent().parent().children('tr').eq(0).children('td').find('input').prop('checked', true);
        } else {
            $(this).parent().parent().parent().parent().children('tr').eq(0).children('td').find('input').prop('checked', false);
        }
    });
});
