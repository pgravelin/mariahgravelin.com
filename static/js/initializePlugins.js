$(document).ready(function() {
    $(".sidenav").sidenav();
});

$(document).ready(function() {
    $(".modal").modal();
    $(".dropdown-trigger").dropdown({
        hover: true
    });
});

var $grid = $(".grid").imagesLoaded(function() {
    $grid.removeClass("is-invisible");
    $grid.masonry({
        itemSelector: ".grid-item",
        percentPosition: true,
        columnWidth: ".grid-sizer"
    });
});

$(window).resize(function () {
    // $grid.masonry("destroy");
    // $grid.removeData("masonry");
    $grid = $(".grid").imagesLoaded(function() {
        $grid.masonry({
            itemSelector: ".grid-item",
            percentPosition: true,
            columnWidth: ".grid-sizer"
        });    
    });
});