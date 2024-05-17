document.addEventListener('DOMContentLoaded', function () {
    const avatarModal = document.getElementById('avatarModal');
    const closeModal = document.getElementById('closeModal');
    const profilePicture = document.getElementById('profilePicture');

    // Open modal on profile picture click
    profilePicture.addEventListener('click', () => {
        avatarModal.style.display = 'block';
    });

    // Close modal on clicking the close button
    closeModal.addEventListener('click', () => {
        avatarModal.style.display = 'none';  // 此处应改为 'none'
    });

    // Close modal when clicking outside the modal content
    window.addEventListener('click', (event) => {
        if (event.target === avatarModal) {
            avatarModal.style.display = 'none';  // 此处应改为 'none'
        }
    });
});
