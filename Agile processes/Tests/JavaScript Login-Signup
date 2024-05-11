document.addEventListener('DOMContentLoaded', function() {
    function setupModals() {
        const modals = {
            'login': document.getElementById('loginModal'),
            'signup': document.getElementById('signupModal'),
            'passwordReset': document.getElementById('passwordResetModal')
        };

        const buttons = {
            'login': document.getElementById('showLoginModal'),
            'signup': document.getElementById('showSignUpModal'),
            'passwordReset': document.getElementById('forgotPasswordLink')
        };

        const closeIcons = {
            'login': document.getElementById('closeLogin'),
            'signup': document.getElementById('closeSignup'),
            'passwordReset': document.getElementById('closePasswordReset')
        };

        Object.keys(buttons).forEach(key => {
            buttons[key].onclick = () => modals[key].style.display = "block";
            closeIcons[key].onclick = () => modals[key].style.display = "none";
        });

        window.onclick = event => {
            Object.values(modals).forEach(modal => {
                if (event.target === modal) {
                    modal.style.display = "none";
                }
            });
        };
    }

    setupModals();
});
