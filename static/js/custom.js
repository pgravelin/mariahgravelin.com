$(window).on("load", function() {
   var $cover = $("#homepage").imagesLoaded(function() {
      $cover.removeClass("is-invisible");
   });
});

var modal = $(".modal");
var modalImg = $("#modal-img")

$(".grid img").each(function() {
   $(this).on("click", function() {
      modal.css("display", "block");
      modalImg.attr("src", $(this).attr("src"));
   });
});

$("#banner img").on("click", function() {
   modal.css("display", "block");
   modalImg.attr("src", $(this).attr("src"));
});

var span = $(".close");
span.on("click", function() {
   modal.css("display", "none");
});