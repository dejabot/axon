/* Shared light/dark theme for Axon curriculum interactive visualizers.
   Load this in <head> before stylesheets. It:
   1. sets the theme before first paint (reading from localStorage 'axon-theme' or 'axon_theme');
   2. injects a fixed ☾/☀ toggle button at top-right once the body exists;
   3. persists the choice in localStorage so flipping anywhere applies everywhere;
   4. dispatches a custom 'themechange' event so canvas renders update immediately. */

(function () {
  var root = document.documentElement;
  var saved;
  try {
    saved = localStorage.getItem('axon-theme') || localStorage.getItem('axon_theme');
  } catch (e) {}

  if (root.getAttribute('data-theme') !== 'light' && root.getAttribute('data-theme') !== 'dark') {
    root.setAttribute('data-theme', saved === 'light' ? 'light' : 'dark');
  }

  function cur() {
    return root.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
  }

  function notifyThemeChange(newTheme) {
    window.dispatchEvent(new CustomEvent('axon-theme-changed', { detail: { theme: newTheme } }));
  }

  function addToggle() {
    if (document.getElementById('axonThemeToggle')) return;
    var btn = document.createElement('button');
    btn.id = 'axonThemeToggle';
    btn.className = 'theme-toggle';
    btn.type = 'button';
    btn.setAttribute('aria-label', 'Switch between light and dark theme');

    function paint() {
      var isDark = cur() === 'dark';
      btn.textContent = isDark ? '☾' : '☀';
      btn.title = isDark ? 'Dark theme — click to switch to light' : 'Light theme — click to switch to dark';
    }

    btn.addEventListener('click', function () {
      var next = cur() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try {
        localStorage.setItem('axon-theme', next);
        localStorage.setItem('axon_theme', next);
      } catch (e) {}
      paint();
      notifyThemeChange(next);
    });

    paint();
    document.body.appendChild(btn);
  }

  window.addEventListener('storage', function (e) {
    if (e.key === 'axon-theme' || e.key === 'axon_theme') {
      var newTheme = e.newValue || 'dark';
      root.setAttribute('data-theme', newTheme);
      var btn = document.getElementById('axonThemeToggle');
      if (btn) {
        btn.textContent = newTheme === 'dark' ? '☾' : '☀';
        btn.title = newTheme === 'dark' ? 'Dark theme — click to switch to light' : 'Light theme — click to switch to dark';
      }
      notifyThemeChange(newTheme);
    }
  });

  if (document.body) {
    addToggle();
  } else {
    document.addEventListener('DOMContentLoaded', addToggle);
  }
})();
