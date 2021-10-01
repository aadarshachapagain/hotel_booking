$(document).ready(function () {
    let room_type_selector = $(".room-type");
    let initial_selected_room = room_type_selector.children(':selected').val();
    bed_type_option_toggle(initial_selected_room);
    room_type();
    bed_type();
    multi_clone();
});

function room_type() {
    $(".room-type").change(function () {
        let selected_room = $(this).children(':selected').val();
        $('.bed-type option:selected').removeAttr('selected');
        $('.bed-type').val('0').trigger('change.select2');
        $('input[name="bed_count"]').val('');
        bed_type_option_toggle(selected_room);
    });
}
function bed_type() {
    $(".bed-type").change(function () {
        let bed_count = $(this).children(':selected').attr('data-bed-count');
        let $current = $(this);
        display_room_count(bed_count, $current);
    });
}
function bed_type_option_toggle(selected_room) {

    let $bed_type = $('.bed-type option');
    $bed_type.prop('disabled',false);
    $bed_type.each(function () {
        if ($(this).attr('data-room-type') !== selected_room) {
            $(this).prop('disabled', true);
        }
    });
    $('.bed-type').select2("destroy").select2();
}

function display_room_count(bed_count, $current) {
   $current.parents().eq(2).children().eq(1).children().eq(1).find('input[name="bed_count"]').val(bed_count);
}

function multi_clone() {
    $('.multi-field-wrapper').each(function () {
        var $wrapper = $('.multi-fields', this);
        $(".add-bed", $(this)).click(function (e) {
            if ($('.multi-field:last-child .bed-type', $wrapper).data('select2')) {
                $('.multi-field:last-child .bed-type', $wrapper).select2('destroy');
            }

            var a = $('.multi-field:last-child', $wrapper).clone(true);
            a.find('select, input').val("");
            a.find('.bed-type').select2({width: ' 263.962px'});
            a.find('.bed-type').val('0').trigger('change.select2');
            $('.multi-field:last-child .bed-type', $wrapper).select2({width: ' 263.962px'});
            $wrapper.append(a);
        });

        $('.multi-field .remove-field', $wrapper).click(function () {
            if ($('.multi-field', $wrapper).length > 1)
                $(this).parent('.multi-field').remove();

        });
    });
};