let slidesIndexP = 0; 
const slidesToShow = 5; 

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
    let dotsP = document.getElementsByClassName(".dot-p");

    Array.from(slidesP).forEach(slide => (slide.style.display = "none"));

    if (startIndex >= slidesP.length) {
        slidesIndexP = 0;
    }
    if (startIndex < 0) {
        slidesIndexP = slidesP.length - slidesToShow; 
    }

    for (let i = slidesIndexP; i < slidesIndexP + slidesToShow && i < slidesP.length; i++) {
        slidesP[i].style.display = "block"; 
    }  
}

function plusSlidesP(n) {
    slidesIndexP += n * slidesToShow; 
    showSlidesP(slidesIndexP);
    dotsP[i].className += "active"
    dotsP[i-1].className.replace(" active", "");
}

function currentSlideP(n) {
    slidesIndexP = (n - 1) * slidesToShow; 
    showSlidesP(slidesIndexP);
}
