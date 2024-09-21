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
