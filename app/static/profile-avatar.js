document.addEventListener('DOMContentLoaded', function () {
    const avatarModal = document.getElementById('avatarModal');
    const closeModal = document.getElementById('closeModal');
    const profilePicture = document.getElementById('profilePicture');
    const checkInModal = document.getElementById('checkInModal'); // 获取签到信息弹窗元素
    const openCheckInModal = document.getElementById('openCheckInModal');
    const closeCheckInModal = document.getElementById('closeCheckInModal');

    // Open modal on profile picture click
    profilePicture.addEventListener('click', () => {
        avatarModal.style.display = 'block';
    });

    // Close modal on clicking the close button
    closeModal.addEventListener('click', () => {
        avatarModal.style.display = 'none';  // 此处应改为 'none'
    });

    
    // Open check-in modal on button click
    openCheckInModal.addEventListener('click', () => {
        checkInModal.style.display = 'block';
    });

    // Close check-in modal when clicking the close button
    closeCheckInModal.addEventListener('click', () => {
        checkInModal.style.display = 'none';
    });

    // Optionally close check-in modal when clicking outside of it
    window.addEventListener('click', (event) => {
        if (event.target === checkInModal) {
            checkInModal.style.display = 'none';
        }
    });
});
