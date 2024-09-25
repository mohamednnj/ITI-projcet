let proP = document.getElementsByClassName("product-slide");
for (let index = 0; index < 4; index++) {
    const element = proP[index];
    element.className +="active"
    
}
// let slidesIndexP = 1;
// document.addEventListener("DOMContentLoaded", function() {
//     showSlidesP(slidesIndexP);

//     let prevP = document.querySelector(".prev-p");
//     let nextP = document.querySelector(".next-p");
//     let dotsP = document.querySelectorAll(".dot-p");

//     prevP.addEventListener("click", function() {
//         plusSlidesP(-1);
//     });

//     nextP.addEventListener("click", function() {
//         plusSlidesP(1);
//     });

//     dotsP.forEach((dot, index) => {
//         dot.addEventListener("click", function() {
//             currentSlideP(index + 1);
//         });
//     });
// });

// function showSlidesP(n) {
//     let slidesP = document.getElementsByClassName("product-slide");
//     let dotsP = document.getElementsByClassName("dot-p");

//     // Loop through slides
//     if (n > slidesP.length) slidesIndexP = 1;
//     if (n < 1) slidesIndexP = slidesP.length;

//     // Hide all slides
//     Array.from(slidesP).forEach(slide => (slide.style.display = "none"));
    
//     // Remove active class from all dots
//     Array.from(dotsP).forEach(dot => (dot.className = dot.className.replace(" active", "")));

//     // Show current slide and set active dot
//     slidesP[slidesIndexP - 1].style.display = "block";
//     dotsP[slidesIndexP - 1].className += " active";
// }

// function plusSlidesP(n) {
//     showSlidesP(slidesIndexP += n);
//     slidesP[n].style.display="none"
// }

// function currentSlideP(n) {
//     showSlidesP(slidesIndexP = n);
// }
let slidesIndexP = 1;
document.addEventListener("DOMContentLoaded", function() {
    showSlidesP(slidesIndexP);

    let prevP = document.querySelector(".prev-p");
    let nextP = document.querySelector(".next-p");
    let dotsP = document.querySelectorAll(".dot-p");

    prevP.addEventListener("click", function() {
        plusSlidesP(-1);
    });

    nextP.addEventListener("click", function() {
        // Special logic: hide the first product when 'next' is clicked
        if (slidesIndexP === 1) {
            let firstSlide = document.getElementsByClassName("product-slide")[0];
            firstSlide.style.display = "none !important"; // Hide the first slide
        }
        plusSlidesP(1);
    });

    dotsP.forEach((dot, index) => {
        dot.addEventListener("click", function() {
            currentSlideP(index + 1);
            
        });
    });
});

function showSlidesP(n) {
    let slidesP = document.getElementsByClassName("product-slide");
    let dotsP = document.getElementsByClassName("dot-p");

    // Reset index if out of bounds
    if (n > slidesP.length) slidesIndexP = 1;
    if (n < 4) slidesIndexP = slidesP.length;

    // Hide all slides
    Array.from(slidesP).forEach(slide => (slide.style.display = "none"));
    
    // Remove active class from all dots
    Array.from(dotsP).forEach(dot => (dot.className = dot.className.replace(" active", "")));

    // Show the current slide and add active class to the corresponding dot
    slidesP[slidesIndexP - 1].style.display = "block";
    slidesP[slidesIndexP - 4].style.display = "none";
    dotsP[slidesIndexP - 1].className += " active";
}

function plusSlidesP(n) {
    showSlidesP(slidesIndexP += n);
}

function currentSlideP(n) {
    showSlidesP(slidesIndexP = n);
}
