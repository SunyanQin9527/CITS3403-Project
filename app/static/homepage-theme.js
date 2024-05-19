document.addEventListener('DOMContentLoaded', () => {
    const themeToggleButton = document.getElementById('themeToggle');
    const body = document.body;

    // Check for saved theme preference in localStorage and apply it
    const currentTheme = localStorage.getItem('theme') || 'light'; // Default to 'light'
    if (currentTheme === 'dark') {
        body.classList.add('dark-mode');
    }

    // Listen for a click on the theme toggle button
    themeToggleButton.addEventListener('click', () => {
        // Toggle the 'dark-mode' class on the <body>
        body.classList.toggle('dark-mode');

        // Save the current theme preference to localStorage
        const newTheme = body.classList.contains('dark-mode') ? 'dark' : 'light';
        localStorage.setItem('theme', newTheme);
    });
});
