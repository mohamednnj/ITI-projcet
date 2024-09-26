// let proP = document.getElementsByClassName("product-slide");
// // for (let index = 0; index < 4; index++) {
// //     const element = proP[index];
// //     element.className +=" active"
    
// // }
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
// let slideIndexd = 0;
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

//     for (let index = n; index < 4; index++) {
//         const element = slidesP[index];
//         element.style.display = "block"
//     }
//     // Show current slide and set active dot
//     slidesP[slidesIndexP - 1].style.display = "block";
//     dotsP[slidesIndexP - 1].className += " active";
//     slidesP[slideIndexd].style.display="none"
//     slidesP[slidesP.length - slideIndexd -1].style.display="block"
//     slideIndexd +=1
//     slidesP[slideIndexd + 4].style.display="block"
// }
// function plusSlidesP(n) {
//     showSlidesP(slidesIndexP += n);
// }

// function currentSlideP(n) {
//     showSlidesP(slidesIndexP = n);
// }
let slidesIndexP = 0; // Start from 0 (first slide)
const slidesToShow = 4; // Number of slides to show at once

document.addEventListener("DOMContentLoaded", function () {
    showSlidesP(slidesIndexP);

    let prevP = document.querySelector(".prev-p");
    let nextP = document.querySelector(".next-p");
    let dotsP = document.querySelectorAll(".dot-p");

    prevP.addEventListener("click", function () {
        plusSlidesP(-1);
    });

    nextP.addEventListener("click", function () {
        plusSlidesP(1);
    });

    dotsP.forEach((dot, index) => {
        dot.addEventListener("click", function () {
            currentSlideP(index + 1);
        });
    });
});

function showSlidesP(startIndex) {
    let slidesP = document.getElementsByClassName("product-slide");

    // Hide all slides
    Array.from(slidesP).forEach(slide => (slide.style.display = "none"));

    // Ensure the index is within the bounds of the slide array
    if (startIndex >= slidesP.length) {
        slidesIndexP = 0; // Reset to the first slide if index exceeds
    }
    if (startIndex < 0) {
        slidesIndexP = slidesP.length - slidesToShow; // Go to the last group of slides if moving back
    }

    // Display 4 slides starting from the current index
    for (let i = slidesIndexP; i < slidesIndexP + slidesToShow && i < slidesP.length; i++) {
        slidesP[i].style.display = "block"; // Show the next set of 4 slides
    }
}

function plusSlidesP(n) {
    slidesIndexP += n * slidesToShow; // Move forward or backward by the number of slidesToShow
    showSlidesP(slidesIndexP);
}

function currentSlideP(n) {
    slidesIndexP = (n - 1) * slidesToShow; // Set the index based on dot navigation
    showSlidesP(slidesIndexP);
}
