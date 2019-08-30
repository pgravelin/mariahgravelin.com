$(document).ready(function() {
    $(".sidenav").sidenav();
});

$(document).ready(function() {
    $(".modal").modal();
    $(".dropdown-trigger").dropdown();
});

$(document).ready(function() {
    $("#homepage").css("background-image");
    $("#homepage").fadeIn(1100);
});

var $grid = $('.grid').imagesLoaded( function() {
    // init Masonry after all images have loaded
    $grid.masonry({
        itemSelector: '.grid-item',
        percentPosition: true,
        columnWidth: '.grid-sizer'
    });
    
    $(".grid-item").each(function() {
        $(this).fadeIn(1100);
   });
});