document.addEventListener('DOMContentLoaded', function() {

    var contactForm = document.getElementById('contactForm');
    var successMessageModal = document.getElementById('successMessageModal');
    var closeSuccessModal = document.getElementById('closeSuccessModal');

    contactForm.onsubmit = function(event) {
        event.preventDefault(); 
        // 在此添加 AJAX 提交逻辑
        // 这里可以替换为实际的 AJAX 提交逻辑，示例展示提交成功后的模态框
        successMessageModal.style.display = 'block';
    };


    closeSuccessModal.onclick = function() {
        successMessageModal.style.display = "none";
    };


    window.onclick = function(event) {
        if (event.target == successMessageModal) {
            successMessageModal.style.display = "none";
        }
    };
});

