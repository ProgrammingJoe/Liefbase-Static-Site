function showHamburger() {
  document.getElementById('hamburger-lines').style.display = 'none';
  document.getElementById('hamburger-menu').style.display = 'block';
  $('#hamburger-menu').animate({
    left: '0vw'
  });
  $('#hamburger-x').animate({
    opacity: '1'
  });
  $('body').addClass('body-no-scroll');
}

function hideHamburger() {
  setTimeout(function(){
  document.getElementById('hamburger-lines').style.display = 'block';
  }, 350);
  setTimeout(function(){
    document.getElementById('hamburger-menu').style.display = 'none';
  }, 350);
  $('#hamburger-menu').animate({
    left: '100vw'
  });
  $('#hamburger-x').animate({
    opacity: '0'
  });
  $('#hamburger-lines').animate({
    opacity: '1'
  });
  $('body').removeClass('body-no-scroll');
}
