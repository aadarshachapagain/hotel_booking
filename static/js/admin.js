// Hide submenus
$('#body-row .collapse').collapse('hide'); 

// // Collapse/Expand icon
// $('#collapse-icon').addClass('fa-angle-double-left');
//
// // Collapse click
// $('[data-toggle=sidebar-colapse]').click(function() {
//     SidebarCollapse();
// });

// function SidebarCollapse () {
//     $('.menu-collapsed').toggleClass('d-none');
//     $('.sidebar-submenu').toggleClass('d-none');
//     $('.submenu-icon').toggleClass('d-none');
//     $('#sidebar-container').toggleClass('sidebar-expanded sidebar-collapsed');
//
//     // Treating d-flex/d-none on separators with title
//     var SeparatorTitle = $('.sidebar-separator-title');
//     if ( SeparatorTitle.hasClass('d-flex') ) {
//         SeparatorTitle.removeClass('d-flex');
//     } else {
//         SeparatorTitle.addClass('d-flex');
//     }
//
//     // Collapse/Expand icon
//     $('#collapse-icon').toggleClass('fa-angle-double-left fa-angle-double-right');
// }
//
// $('.items a').on('click', function() {
//   var $this = $(this),
//       $bc = $('<div class="item"></div>');
//
//   $this.parents('li').each(function(n, li) {
//       var $a = $(li).children('a').clone();
//       $bc.prepend(' / ', $a);
//   });
//     $('.breadcrumb').html( $bc.prepend('<a href="#home">Home</a>') );
//     return false;
// })
// setTimeout(function () {
//             document.getElementById('approved').className = 'approvefade';
//         }, 5000);
