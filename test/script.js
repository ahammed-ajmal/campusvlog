let isDragging = false;
let startX;
let currentTranslate = 0;
let initialTranslate = 0;

const navbar = document.getElementById('navbar');

navbar.addEventListener('mousedown', (e) => {
  isDragging = true;
  startX = e.clientX - navbar.offsetLeft;
  initialTranslate = currentTranslate;

  document.addEventListener('mousemove', handleMouseMove);
  document.addEventListener('mouseup', () => {
    isDragging = false;
    document.removeEventListener('mousemove', handleMouseMove);
  });
});

function handleMouseMove(e) {
  if (!isDragging) return;

  const newX = e.clientX - navbar.offsetLeft;
  const deltaX = newX - startX;

  currentTranslate = initialTranslate + deltaX;

  // Limit the leftmost and rightmost translation to prevent over-scrolling
  currentTranslate = Math.max(Math.min(0, currentTranslate), -navbar.scrollWidth + window.innerWidth);

  navbar.style.transform = `translateX(${currentTranslate}px)`;
}
