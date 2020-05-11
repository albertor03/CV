function sideMenu(){
  button = $('#btn-sidebar');
  menu = $('.header-navegation ul')

  if (button.attr('class') == 'fas fa-bars'){
    button.removeClass('fas fa-bars').addClass('fas fa-times').css({'transition': '.3s'});
    menu.css({'left': '0px'})
  }else{
    button.removeClass('fas fa-times').addClass('fas fa-bars');
    menu.css({'left': '-320px'})
  }
}

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("top-button").style.display = "block";
  } else {
    document.getElementById("top-button").style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

