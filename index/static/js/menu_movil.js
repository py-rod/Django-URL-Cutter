function toggleMenu() {
  let menu = document.querySelector('.menu');
  let overlay = document.querySelector('.overlay');
  menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
  overlay.style.display = overlay.style.display === 'block' ? 'none' : 'block';
}

function closeMenu() {
  let menu = document.querySelector('.menu');
  let overlay = document.querySelector('.overlay');
  menu.style.display = 'none';
  overlay.style.display = 'none';
}
