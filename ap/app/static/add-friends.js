document.addEventListener('DOMContentLoaded', function() {
    const addFriendIcon = document.querySelector('.add-friend-icon');
    const addFriendModal = document.getElementById('addFriendModal');
    const closeAddFriend = document.getElementById('closeAddFriend');
    const addFriendForm = document.getElementById('addFriendForm');

 
    addFriendIcon.onclick = function() {
        addFriendModal.style.display = 'block';
    };

    closeAddFriend.onclick = function() {
        addFriendModal.style.display = 'none';
    };

    window.onclick = function(event) {
        if (event.target === addFriendModal) {
            addFriendModal.style.display = 'none';
        }
    };

    addFriendForm.onsubmit = function(event) {
        event.preventDefault();
        const userId = document.getElementById('userId').value;
        alert(`Friend request sent to User ID: ${userId}`);

        addFriendModal.style.display = 'none';
    };
});
