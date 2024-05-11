// Handles avatar selection in the modal and updates the profile picture
document.addEventListener('DOMContentLoaded', function () {
    const avatarModal = document.getElementById('avatarModal');
    const closeModal = document.getElementById('closeModal');
    const profilePicture = document.getElementById('profilePicture');
    const avatarOptions = document.querySelectorAll('.avatar-option');

    // Open modal on profile picture click
    profilePicture.addEventListener('click', () => {
        avatarModal.style.display = 'block';
    });

    // Close modal on clicking the close button
    closeModal.addEventListener('click', () => {
        avatarModal.style.display = 'none';
    });

    // Update profile picture with the chosen avatar and close the modal
    avatarOptions.forEach(avatar => {
        avatar.addEventListener('click', (e) => {
            profilePicture.src = e.target.src;
            avatarModal.style.display = 'none';
        });
    });

    // Close modal when clicking outside the modal content
    window.addEventListener('click', (event) => {
        if (event.target === avatarModal) {
            avatarModal.style.display = 'none';
        }
    });
});

