let currentPage = 1;
let itemsPerPage = 12;
let totalPages;

function initPagination() {
    const items = document.querySelectorAll('.product-item');
    totalPages = Math.ceil(items.length / itemsPerPage);
    displayItems();
}

function displayItems() {
    const items = document.querySelectorAll('.product-item');
    const start = (currentPage - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    items.forEach((item, index) => {
        item.style.display = (index >= start && index < end) ? 'block' : 'none';
    });
}

function goToPage(page) {
    currentPage = page;
    displayItems();
}

function goToNextPage() {
    if (currentPage < totalPages) {
        currentPage += 1;
        displayItems();
    }
}

function goToPreviousPage() {
    if (currentPage > 1) {
        currentPage -= 1;
        displayItems();
    }
}

document.addEventListener('DOMContentLoaded', function() {
    initPagination();
});

window.goToNextPage = goToNextPage;
window.goToPage = goToPage;
window.goToPreviousPage = goToPreviousPage;
