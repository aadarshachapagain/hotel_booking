$(document).ready(function () {
    multiGenerateFunction();
});

let multiGenerateFunction = function () {
    $('.multi-field-wrapper').each(function () {
        var $wrapper = $('.multi-fields', this);
        $(".add-field", $(this)).click(function (e) {
            var a = $('.multi-field:first-child', $wrapper).clone(true);
            a.find('number, number, input,input').val("");
            $wrapper.append(a);
        });

        $('.multi-field .remove-field', $wrapper).click(function () {
            if ($('.multi-field', $wrapper).length > 1)
                $(this).parent('.multi-field').remove();

        });
    });
};