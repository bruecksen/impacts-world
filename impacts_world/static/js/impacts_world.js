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

var is_sticky = false;
$(document).ready(function () {

var menu = $('.navbar-default');
var origOffsetY = menu.offset().top;
is_sticky = menu.hasClass('navbar-fixed-top');

function scroll() {
	if ($(window).scrollTop() >= origOffsetY) {
		$('.navbar-default').addClass('navbar-fixed-top');
		$('body').addClass('navbar-padding');
		is_sticky = true;
	} else {
		$('.navbar-default').removeClass('navbar-fixed-top');
		$('body').removeClass('navbar-padding');
		is_sticky = false;
	}
}
if (is_sticky === false) {
	document.onscroll = scroll;
}
});

$(document).ready(function () {
	var navbarMobile = $('.navbar-mobile');
	$('.navbar-toggle').click(function(event) {
		event.preventDefault();
		if ($(this).hasClass('collapsed')) {
			$(this).removeClass('collapsed');
			if (is_sticky === false) {
				$('.navbar-default').addClass('navbar-fixed-top');
				$('body').addClass('navbar-padding');
			}
			navbarMobile.show();
		} else {
			$(this).addClass('collapsed');
			if (is_sticky === false) {
				$('.navbar-default').removeClass('navbar-fixed-top');
				$('body').removeClass('navbar-padding');
			}
			navbarMobile.hide();
		}
	});

});