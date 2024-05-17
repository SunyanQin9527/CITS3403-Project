document.addEventListener('DOMContentLoaded', function () {

    const avatar = document.getElementById('userAvatar');
    const avatarModal = document.getElementById('chat-avatarModal');
    const closeAvatarModal = document.querySelector('#chat-avatarModal .close');

    if (avatar) {

        avatar.onclick = function () {
            console.log("Avatar clicked");
            avatarModal.style.display = 'block';
        };
    } else {
        console.log("Avatar element not found");
    }

    if (closeAvatarModal) {

        closeAvatarModal.onclick = function () {
            console.log("Close button clicked");
            avatarModal.style.display = 'none';
        };
    } else {
        console.log("Close button not found");
    }


    window.onclick = function (event) {
        if (event.target === avatarModal) {
            console.log("Clicked outside of modal");
            avatarModal.style.display = 'none';
        }
    };
});

