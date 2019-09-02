$(window).on("load", function() {
   var $cover = $("#homepage").imagesLoaded(function() {
      $cover.removeClass("is-invisible");
   });
});

var $sep = $(".separation").imagesLoaded(function() {
   $sep.addClass("animated fadeIn");
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
   modal.hide();
});

$("body").click(function (e) {
   if(!$(e.target).is("img") && !$(e.target).closest(".modal-content").length && !$(e.target).is(".modal-content")) {
     $(".modal").hide();
   }     
});