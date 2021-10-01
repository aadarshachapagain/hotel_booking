$(document).ready(() => {
    $('.my-amenity-div').first().css('display', 'grid');
    $('.my-amenity-button').first().addClass('activ');
});
var acc = $(".accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function () {
        this.classList.toggle("activ");
        var panel = this.nextElementSibling;
        if (panel.style.display === "grid") {
            panel.style.display = "none";
        } else {
            panel.style.display = "grid";
        }
    });
}
