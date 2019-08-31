$(document).ready(function() {
    $(".sidenav").sidenav();
});

$(document).ready(function() {
    $(".modal").modal();
    $(".dropdown-trigger").dropdown({
        
    });
});

var $grid = $(".grid").imagesLoaded(function() {
    $grid.addClass("animated fadeIn");
    $grid.masonry({
        itemSelector: ".grid-item",
        percentPosition: true,
        columnWidth: ".grid-sizer"
    });
});

$(window).resize(function () {
    $grid = $(".grid").imagesLoaded(function() {
        $grid.masonry({
            itemSelector: ".grid-item",
            percentPosition: true,
            columnWidth: ".grid-sizer"
        });    
    });
});