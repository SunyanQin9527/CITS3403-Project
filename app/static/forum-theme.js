// forum-theme.js

document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.body.classList.toggle('dark-mode', currentTheme === 'dark');

    themeToggle.addEventListener('click', function() {
        const isDarkMode = document.body.classList.toggle('dark-mode');
        const theme = isDarkMode ? 'dark' : 'light';
        localStorage.setItem('theme', theme);

        // Update hidden input fields in forms
        document.querySelectorAll('input[name="theme"]').forEach(input => {
            input.value = theme;
        });

        // Redirect with the theme parameter
        const searchParams = new URLSearchParams(window.location.search);
        searchParams.set('theme', theme);
        window.location.search = searchParams.toString();
    });

    // Set hidden input fields to the current theme
    document.querySelectorAll('input[name="theme"]').forEach(input => {
        input.value = currentTheme;
    });
});
