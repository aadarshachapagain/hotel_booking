$(document).ready(function () {
    notificationDropDown();
    notificationBellColor();
});

$(document).on('click', "a[data-dropdown='notificationMenu']", function (e) {
    e.preventDefault();
    var el = $(e.currentTarget);
    var container = $(e.currentTarget).parent();
    var dropdown = container.find('.my-dropdown');
    var containerWidth = container.width();
    var containerHeight = container.height();
    var anchorOffset = $(e.currentTarget).offset();
    dropdown.css({
        'right': containerWidth / 2 + 'px'
    });
    container.toggleClass('expanded');
    if ($('.collapse').hasClass('show')) {
        $('.collapse').removeClass('show');
    }
});
$(document).on('click', '.admin-dashboard-wrapper', function (e) {
    var el = $(e.currentTarget)[0].activeElement;

    if (typeof $(el).attr('data-dropdown') === 'undefined') {
        $('#dropdownOverlay').remove();
        $('.dropdown-container.expanded').removeClass('expanded');
        $('.card-header').removeClass('box-shadow-my');
    }
});
let notificationDropDown = function () {
    $('.card-header').click(function (e) {
        if ($(e.currentTarget).siblings('.my-collapse').hasClass('show') & $(e.currentTarget).hasClass('box-shadow-my')) {
            $(e.currentTarget).toggleClass('box-shadow-my');
            $(e.currentTarget).siblings('.my-collapse').removeClass('show');
        } else {
            $('.card-header').not(this).removeClass('box-shadow-my');
            $(e.currentTarget).toggleClass('box-shadow-my');
            $('.my-collapse').not($(e.currentTarget)).removeClass('show');
            $(e.currentTarget).siblings('.my-collapse').toggleClass('show');
        }


    });
};

let notificationBellColor = function () {
    a = $('#notification-number').text();
    if (a > 0) {
        $('#notification-bell ,#notification-number').css({'color': '#e93e3a', 'display': 'inline-block'});
    } else {
        $('#notification-bell ,#notification-number').css({'color': 'black', 'display': 'inline-block'});
    }
};

