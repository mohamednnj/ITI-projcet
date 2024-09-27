document.addEventListener('mouseleave', function(event) {
    const dropdown = document.querySelector('.dropdown-menu');
    const navItem = document.querySelector('.dropdown');
    
    if (!navItem.contains(event.target)) {
        dropdown.style.display = 'none';
    }
    
    navItem.addEventListener('mouseenter', () => {
        dropdown.style.display = 'flex';
    });
});

    let slideIndex = 0;
    let slideInterval;
    let slides = document.getElementsByClassName("slide");
    let dots = document.getElementsByClassName("dot");

    // Function to show the current slide
    function showSlides() {
        // Hide all slides
        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }

        // Remove the active class from all dots
        for (let i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }

        // Increment slideIndex and reset it if it goes out of bounds
        slideIndex++;
        if (slideIndex > slides.length) {
            slideIndex = 1;
        }

        // Display the current slide and activate the corresponding dot
        slides[slideIndex - 1].style.display = "block";
        dots[slideIndex - 1].className += " active";

        // Automatically move to the next slide every 5 seconds
        slideInterval = setTimeout(showSlides, 5000);
    }

    // Function to move to the next/previous slide
    function plusSlides(n) {
        clearTimeout(slideInterval);  
        slideIndex += n;              
        if (slideIndex >= slides.length) slideIndex = 0;
        if (slideIndex < 0) slideIndex = slides.length - 1;
        showSlides();                  
    }

    // Function to go to a specific slide
    function currentSlide(n) {
        clearTimeout(slideInterval);  
        slideIndex = n - 1;            
        showSlides();                  
    }

// handel navbar

function addParagraphToNavbar() {
    const windowWidth = window.innerWidth;

    if (windowWidth <= 1200) {

        const navItems = document.getElementById('nav-items');
        const navBtn = document.getElementById('nav-btn');
        navItems.style.display="none"
        navBtn.style.display="block"
        
    }
    if (windowWidth >= 1200) {

        const navItems = document.getElementById('nav-items');
        const navBtn = document.getElementById('nav-btn');
        navItems.style.display="flex"
        navBtn.style.display="none"
        
    }
}

window.onload = addParagraphToNavbar;

window.onresize = addParagraphToNavbar;

document.addEventListener('DOMContentLoaded', function() {
    // Function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Add event listener for the 'Add to Cart' button
    document.getElementById('add-to-cart').addEventListener('click', function() {
        let productId = this.getAttribute('data-product-id');
        let qty = document.getElementById('qty').value;  // Fetching the quantity value

        fetch('/cart/add-to-cart/', {  // Ensure this matches the endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'), // Get CSRF token
            },
            body: JSON.stringify({
                product_id: productId,
                quantity: qty // Sending the quantity
            })
        })
        .then(response => response.json())  // Convert response to JSON
        .then(data => {
            if (data.success) {  // Check for success in the response
                openCart();  // Call to open the cart
            } else {
                alert('Failed to add to cart.');
            }
        })
        .catch(error => console.error('Error:', error));
    });

    // Function to open the cart
    function openCart() {
        fetch('/cart/get_cart/')  // Update this to your actual endpoint for fetching cart data
            .then(response => response.json())
            .then(data => {
                if (data.products) {
                    let cartContent = '';
                    let total = 0;
                    data.products.forEach(product => {
                        cartContent += `
                            <div class="cart-item">
                                <img src="${product.image}" alt="${product.name}">
                                <p>${product.name} - $${product.price}</p>
                            </div>
                        `;
                        total += parseFloat(product.price);
                    });
                    document.getElementById('cart-items').innerHTML = cartContent;
                    document.getElementById('cart-total-amount').innerText = '$' + total.toFixed(2);
                    document.getElementById('side-cart').classList.add('open');  // Open the cart
                }
            })
            .catch(error => console.error('Error fetching cart:', error));
    }

    // Toggle the cart visibility
    document.getElementById('cart-icon').addEventListener('click', function(e) {
        e.preventDefault();
        let sideCart = document.getElementById('side-cart');
        sideCart.classList.toggle('open');
    });
    

    // Optional: Close the cart if you click outside of it
    window.addEventListener('click', function(e) {
        let sideCart = document.getElementById('side-cart');
        if (!sideCart.contains(e.target) && !document.getElementById('cart-icon').contains(e.target)) {
            sideCart.classList.remove('open');
        }
    });
});
