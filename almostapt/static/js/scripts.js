// scripts.js
document.addEventListener('DOMContentLoaded', () => {
  const mainContent = document.querySelector('.main-content');
  const toggleDarkMode = document.getElementById('toggle-dark-mode');
  const toggleLabel = document.getElementById('toggle-label');

  function toggleDarkModeFunc() {
    mainContent.classList.toggle('dark-mode');
    toggleDarkMode.checked = !toggleDarkMode.checked;

    if (mainContent.classList.contains('dark-mode')) {
      localStorage.setItem('dark-mode', 'true');
      toggleLabel.textContent = 'Light Mode';
    } else {
      localStorage.setItem('dark-mode', 'false');
      toggleLabel.textContent = 'Dark Mode';
    }
  }

  if (localStorage.getItem('dark-mode') === 'true') {
    mainContent.classList.add('dark-mode');
    toggleDarkMode.checked = true;
    toggleLabel.textContent = 'Light Mode';
  } else {
    mainContent.classList.remove('dark-mode');
    toggleDarkMode.checked = false;
    toggleLabel.textContent = 'Dark Mode';
  }

  toggleDarkMode.addEventListener('change', toggleDarkModeFunc);
  toggleLabel.addEventListener('click', toggleDarkModeFunc);
});
