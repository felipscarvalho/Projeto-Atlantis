const nav = document.querySelector('#nav');

window.onscroll = function () { 
    if (document.body.scrollTop >= 10 || document.documentElement.scrollTop >= 10) {
        nav.classList.add("nav__colored");
        nav.classList.remove("nav__transparent");
    } 
    else {
        nav.classList.add("nav__transparent");
        nav.classList.remove("nav__colored");
    }
};

// Mobile Nav
let navStatus = false;

function toggleNav() {
    if (navStatus === false) {
        document.querySelector('#nav').style.maxHeight = '512px'

        navStatus = true
    } else {
        document.querySelector('#nav').style.maxHeight = '64px'

        navStatus = false
    }
}