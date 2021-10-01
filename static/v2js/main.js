(function($) {
  "use strict";

  var fullHeight = function() {
    $(".js-fullheight").css("height", $(window).height());
    $(window).resize(function() {
      $(".js-fullheight").css("height", $(window).height());
    });
  };
  fullHeight();
  $("#sideDropDownCollapse").on("click", function() {
    // $("#sidebar").toggleClass("active");
    // document.getElementById("sidebar").style.min - width = "500px";
    $("sideDropDownCollapse").attr("aria-expanded", "false");
  });
  $(document).ready(function () {
    $("#sidebarCollapse").on("click", function () {
    $("#sidebar").toggleClass("active");
    $(".collapse").removeClass("show");
    // $(".dropdown-toggle").toggleClass("hidden-shaw");

  });
  });
  let checkActive = function () {
    if ($('#sidebar').hasClass('active'))
    {
      $('.logo').children('span:first').html('B');
      $('.logo').children('span:nth-child(2)').html('S.');
    }
    else {
      $('.logo').children('span:first').html('BIG');
      $('.logo').children('span:nth-child(2)').html(' SAFAR.');
    }
  }
})(jQuery);

