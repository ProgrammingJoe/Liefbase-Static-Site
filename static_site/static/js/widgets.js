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
  // document.getElementById('hamburger-x').style.display = 'block';
  // document.getElementById('hamburger-lines').style.display = 'none';
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
  document.getElementById('hamburger-menu').style.display = 'none'.delay(1000);
  // document.getElementById('hamburger-x').style.display = 'none';
  // document.getElementById('hamburger-lines').style.display = 'block';
  $('body').removeClass('body-no-scroll');
}
