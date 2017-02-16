$(function() {
  $('.affix a, .mobile-anchor-nav a').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 800);
        return false;
      }
    }
  });
});

$(document).ready(function () {

var menu = $('.navbar-default');
var origOffsetY = menu.offset().top;
var is_sticky = menu.hasClass('navbar-fixed-top');

function scroll() {
	if ($(window).scrollTop() >= origOffsetY) {
		$('.navbar-default').addClass('navbar-fixed-top');
		$('body').addClass('navbar-padding');
	} else {
		$('.navbar-default').removeClass('navbar-fixed-top');
		$('body').removeClass('navbar-padding');
	}
}
if (is_sticky === false) {
	document.onscroll = scroll;
}
});