document.addEventListener('DOMContentLoaded', () => {
  const red_header = document.getElementById('red_header');
  const header = document.querySelector('header');

  red_header.addEventListener('click', () => {
    header.style.color = '#FF0000';
  });
});
