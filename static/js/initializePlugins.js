$(document).ready(function() {
    $(".sidenav").sidenav();
});

$(document).ready(function() {
    $(".modal").modal();
    $(".dropdown-trigger").dropdown();
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