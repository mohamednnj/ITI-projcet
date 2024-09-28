function changeImage(imageSrc) {
    document.getElementById("mainImage").src = imageSrc;
}

function decreaseQty() {
    let qty = document.getElementById('qty').value;
    if (qty > 1) {
        document.getElementById('qty').value = --qty;
    }
}

function increaseQty() {
    let qty = document.getElementById('qty').value;
    document.getElementById('qty').value = ++qty;
}

function openTab(evt, tabName) {
    let tabContent = document.getElementsByClassName("tab-content");
    for (let i = 0; i < tabContent.length; i++) {
        tabContent[i].style.display = "none";
    }
    let tabBtns = document.getElementsByClassName("tab-btn");
    for (let i = 0; i < tabBtns.length; i++) {
        tabBtns[i].className = tabBtns[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

// Set default tab
document.getElementById("description").style.display = "block";

function addToCart(productId) {
        // Get the quantity from the hidden input field
        var quantity = document.getElementById("quantity").value;

        // Construct the URL by passing quantity as a query parameter
        var url = '/cart/add/' + productId + '/?quantity=' + quantity;

        // Redirect to the constructed URL
        window.location.href = url;
    }