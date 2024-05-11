let currentPage = 1;
let itemsPerPage = 12;
let totalPages;

function loadProducts() {
    const container = document.querySelector('.products');
    for (let i = 33; i <= 62; i++) {
        const html = `
            <div class='product-item'>
                <img src='profile-pictures/shop${i}.jpg' alt='Item ${i}'>
                <h3>Item ${i}</h3>
                <p>300 Points</p>
                <button class='shop-button'>Buy</button>
            </div>
        `;
        container.innerHTML += html;
    }
    initPagination();
}

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

document.addEventListener('DOMContentLoaded', loadProducts);
window.goToNextPage = goToNextPage;
window.goToPage = goToPage;
window.goToPreviousPage = goToPreviousPage;

