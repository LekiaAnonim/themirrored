$(document).ready(function() {
    $('.post-carousel').slick({
        // autoplay: true,
        autoplaySpeed: 3000,
        arrows: true,
        ltf: true,
        dots: true

    });
});
$('.blog-carousel').slick({
    ltr: true,
    autoplay: true,
    arrows: true,
    autoplaySpeed: 4000,
    accessibility: true,
    dots: true
});