document.addEventListener('DOMContentLoaded', function () {
    const avatar = document.getElementById('userAvatar');
    const avatarModal = document.getElementById('chat-avatarModal');
    const closeAvatarModal = document.querySelector('#chat-avatarModal .close');
    const openAddFriendModal = document.getElementById('openAddFriendModal');
    const addFriendModal = document.getElementById('addFriendModal');
    const closeAddFriend = document.getElementById('closeAddFriend');
    const addFriendForm = document.getElementById('addFriendForm');
    const userIdInput = document.getElementById('userId');

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

    if (openAddFriendModal) {
        openAddFriendModal.onclick = function () {
            console.log("Add friend icon clicked");
            addFriendModal.style.display = 'block';
        };
    } else {
        console.log("Add friend icon not found");
    }

    if (closeAddFriend) {
        closeAddFriend.onclick = function () {
            console.log("Add friend modal close clicked");
            addFriendModal.style.display = 'none';
        };
    } else {
        console.log("Add friend modal close button not found");
    }

    window.onclick = function (event) {
        if (event.target === avatarModal) {
            console.log("Clicked outside of modal");
            avatarModal.style.display = 'none';
        }
        if (event.target === addFriendModal) {
            console.log("Clicked outside add friend modal");
            addFriendModal.style.display = 'none';
        }
    };

    if (addFriendForm) {
        addFriendForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const userId = userIdInput.value.trim();
            if (!userId) {
                alert('User ID cannot be empty.');
                return;
            }

            
        });
    } else {
        console.log("Add friend form not found");
    }
});
