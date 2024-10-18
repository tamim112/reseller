(() => {
  const THEME = 'coreui-free-bootstrap-admin-template-theme';

  // Function to get stored theme from localStorage
  const getStoredTheme = () => localStorage.getItem(THEME);

  // Function to store the theme in localStorage
  const setStoredTheme = theme => localStorage.setItem(THEME, theme);

  // Function to get the preferred theme, checking local storage or system preference
  const getPreferredTheme = () => {
    const storedTheme = getStoredTheme();
    if (storedTheme) {
      return storedTheme;
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  };

  // Function to apply the selected theme
  const setTheme = theme => {
    if (theme === 'auto') {
      if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.setAttribute('data-coreui-theme', 'dark');
      } else {
        document.documentElement.setAttribute('data-coreui-theme', 'light');
      }
    } else {
      document.documentElement.setAttribute('data-coreui-theme', theme);
    }

    const event = new Event('ColorSchemeChange');
    document.documentElement.dispatchEvent(event);
  };

  // Apply the preferred theme on page load
  setTheme(getPreferredTheme());

  // Function to show the active theme
  const showActiveTheme = theme => {
    const activeThemeIcon = document.querySelector('.theme-icon-active i');
    const btnToActive = document.querySelector(`[data-coreui-theme-value="${theme}"]`);

    if (!btnToActive || !activeThemeIcon) {
      console.error(`Button or active icon element not found for theme: ${theme}`);
      return;
    }

    // Define the appropriate Font Awesome icon class based on the theme
    let themeIconClass;
    if (theme === 'dark') {
      themeIconClass = 'fa-moon';
    } else if (theme === 'light') {
      themeIconClass = 'fa-sun';
    } else if (theme === 'auto') {
      themeIconClass = 'fa-circle-half-stroke'; // Auto mode icon
    }

    // Remove 'active' class from all theme buttons
    document.querySelectorAll('[data-coreui-theme-value]').forEach(element => {
      element.classList.remove('active');
    });

    // Add 'active' class to the selected button
    btnToActive.classList.add('active');

    // Update the icon class for the active theme icon
    activeThemeIcon.className = `icon fa-solid ${themeIconClass}`;
  };

  // Listen for system-level dark mode changes
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
    const storedTheme = getStoredTheme();
    if (storedTheme === 'auto') {
      setTheme('auto'); // Reapply auto theme if system preference changes
      showActiveTheme('auto'); // Update icon dynamically for auto mode
    }
  });

  // When the DOM is fully loaded, show the active theme and set up event listeners
  window.addEventListener('DOMContentLoaded', () => {
    showActiveTheme(getPreferredTheme());

    // Add event listeners to theme toggle buttons
    document.querySelectorAll('[data-coreui-theme-value]').forEach(toggle => {
      toggle.addEventListener('click', () => {
        const theme = toggle.getAttribute('data-coreui-theme-value');
        setStoredTheme(theme);
        setTheme(theme);
        showActiveTheme(theme);
      });
    });
  });
})();
