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

        // Automatically move to the next slide every 3 seconds
        slideInterval = setTimeout(showSlides, 1000);
    }

    // Function to move to the next/previous slide
    function plusSlides(n) {
        clearTimeout(slideInterval);  // Stop automatic sliding
        slideIndex += n;              // Adjust the slide index
        if (slideIndex >= slides.length) slideIndex = 0;
        if (slideIndex < 0) slideIndex = slides.length - 1;
        showSlides();                  // Show the updated slide
    }

    // Function to go to a specific slide
    function currentSlide(n) {
        clearTimeout(slideInterval);   // Stop automatic sliding
        slideIndex = n - 1;            // Set the slide index to the clicked dot
        showSlides();                  // Show the selected slide
    }