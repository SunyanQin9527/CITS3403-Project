document.addEventListener('DOMContentLoaded', function() {

    var modal = document.getElementById("discussionModal");

    var btn = document.getElementById("discussionform");

    var closeDiscussionModal = document.getElementById('closeDiscussionModal');

    btn.onclick = function() {
        modal.style.display = "block";
    }

    closeDiscussionModal.onclick = function() {
        modal.style.display = "none"; // Close the entire modal, not just the close button itself
    };

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
});

