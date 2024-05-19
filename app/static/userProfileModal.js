function openModal(userId) {
    console.log("Opening modal for user ID:", userId);
    // Fetch user details from the server
    fetch('/get_user_details/' + userId)
        .then(response => response.json())
        .then(data => {
            // Populate the modal with user data
            document.getElementById('modalUsername').textContent = data.username;
            document.getElementById('modalEmail').textContent = "Email: " + data.email;
            document.getElementById('modalJoined').textContent = "Joined on: " + (data.member_since ? data.member_since : 'Unknown');
            // Show the modal
            document.getElementById('userProfileModal').style.display = 'block';
        });
}

function closeModal() {
    document.getElementById('userProfileModal').style.display = 'none';
}

// Close the modal if the user clicks outside of it
window.onclick = function(event) {
    var modal = document.getElementById('userProfileModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}
