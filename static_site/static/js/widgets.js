function showHamburger() {
  $('#hamburger-menu').animate({
    left: '0vw'
  });
  $('#hamburger-x').animate({
    opacity: '1'
  });
  $('#hamburger-lines').animate({
    opacity: '0'
  });
  document.getElementById('hamburger-menu').style.display = 'block';
  $('body').addClass('body-no-scroll');
}

function hideHamburger() {
  $('#hamburger-menu').animate({
    left: '100vw'
  });
  $('#hamburger-x').animate({
    opacity: '0'
  });
  $('#hamburger-lines').animate({
    opacity: '1'
  });
  setTimeout(function(){
    document.getElementById('hamburger-menu').style.display = 'none';
  }, 1000);
  $('body').removeClass('body-no-scroll');
}
