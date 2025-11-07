
// Smooth scroll and scroll spy functionality
const links = document.querySelectorAll('.nav-link');

// Smooth scroll to section
links.forEach(link => {
    link.addEventListener('click', function(event) {
        event.preventDefault();
        
        const targetId = this.getAttribute('href');
        const targetSection = document.querySelector(targetId);
        
        if (targetSection) {
            // Close mobile menu if open
            const mobileMenu = document.querySelector('.mobile-menu');
            const hamburger = document.querySelector('.hamburger-menu');
            const mobileMenuOverlay = document.querySelector('.mobile-menu-overlay');
            if (mobileMenu && mobileMenu.classList.contains('active')) {
                mobileMenu.classList.remove('active');
                hamburger.classList.remove('active');
                if (mobileMenuOverlay) {
                    mobileMenuOverlay.classList.remove('active');
                }
            }
            
            // Calculate offset for sticky header
            const headerHeight = document.querySelector('header').offsetHeight;
            const targetPosition = targetSection.offsetTop - headerHeight - 20;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
            
            // Update active link after scroll
            setTimeout(() => {
                updateActiveLink();
            }, 100);
        }
    });
});

// Update active link based on scroll position
function updateActiveLink() {
    const sections = document.querySelectorAll('main section[id]');
    const headerHeight = document.querySelector('header').offsetHeight;
    const scrollPosition = window.scrollY + headerHeight + 100;
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        const sectionId = section.getAttribute('id');
        
        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
            // Remove active class from all links
            document.querySelectorAll('.nav-link').forEach(link => {
                link.classList.remove('active');
            });
            
            // Add active class to current section link
            document.querySelectorAll(`.nav-link[href="#${sectionId}"]`).forEach(link => {
                link.classList.add('active');
            });
        }
    });
}

// Listen to scroll events for scroll spy
window.addEventListener('scroll', updateActiveLink);

// Hamburger menu toggle
const hamburgerMenu = document.querySelector('.hamburger-menu');
const mobileMenu = document.querySelector('.mobile-menu');
const mobileMenuOverlay = document.querySelector('.mobile-menu-overlay');

if (hamburgerMenu && mobileMenu) {
    hamburgerMenu.addEventListener('click', function() {
        this.classList.toggle('active');
        mobileMenu.classList.toggle('active');
        if (mobileMenuOverlay) {
            mobileMenuOverlay.classList.toggle('active');
        }
    });
    
    // Close menu when clicking overlay
    if (mobileMenuOverlay) {
        mobileMenuOverlay.addEventListener('click', function() {
            hamburgerMenu.classList.remove('active');
            mobileMenu.classList.remove('active');
            this.classList.remove('active');
        });
    }
    
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!hamburgerMenu.contains(event.target) && !mobileMenu.contains(event.target) && !mobileMenuOverlay.contains(event.target)) {
            hamburgerMenu.classList.remove('active');
            mobileMenu.classList.remove('active');
            if (mobileMenuOverlay) {
                mobileMenuOverlay.classList.remove('active');
            }
        }
    });
}


const texts = ["Frontend Developer", "برنامه نویس بک اند","Django Backend Developer", "Web Designer", "طراح ربات تلگرامی","Telegram Bot Developer", "طراح وبسایت"];
let index = 0;

function changeText() {
    const textElement = document.getElementById('skill-text');
    
    // Fade out the current text
    textElement.classList.add('fade-out');

    setTimeout(() => {
        // Change the text after fading out
        textElement.textContent = texts[index];
        index = (index + 1) % texts.length; // Move to the next text

        // Fade in the new text
        textElement.classList.remove('fade-out');
        textElement.classList.add('fade-in');

        setTimeout(() => {
            textElement.classList.remove('fade-in'); // Remove fade-in class for next iteration
        }, 500); // Match this duration with the CSS transition duration
    }, 500); // Match this duration with the CSS transition duration
}

// Change text every 3 seconds
setInterval(changeText, 3500);

// Initialize with the first text
changeText();

elm = document.getElementById('id_captcha_1')
elm.parentNode.removeChild(elm)

window.addEventListener('DOMContentLoaded', (event) => {    
    var myModal = new bootstrap.Modal(document.getElementById("exampleModal"));
    myModal.show();
  });