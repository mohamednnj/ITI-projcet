function applyFilters() {
    // Get all products
    const products = document.querySelectorAll('.product');

    // Get selected categories
    const selectedCategories = [];
    document.querySelectorAll('.sidebar input[type="checkbox"]:checked').forEach(checkbox => {
        selectedCategories.push(checkbox.value);
    });

    // Get price range
    const minPrice = parseInt(document.getElementById('min').value);
    const maxPrice = parseInt(document.getElementById('max').value);

    // Filter logic
    products.forEach(product => {
        const productCategory = product.getAttribute('data-category');
        const productPrice = parseInt(product.getAttribute('data-price'));

        // Check if product should be displayed
        const inCategory = selectedCategories.length === 0 || selectedCategories.includes(productCategory);
        const inPriceRange = productPrice >= minPrice && productPrice <= maxPrice;

        if (inCategory && inPriceRange) {
            product.style.display = 'block'; // Show the product
        } else {
            product.style.display = 'none'; // Hide the product
        }
    });
}
