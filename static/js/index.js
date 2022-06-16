'use strict';

const btnMenu = document.getElementById('btn-menu');
const navMainMenu = document.getElementById('nav-main');
const containerHeader = document.getElementById('header');
const body = document.getElementById('body');
const listOptionsMenu = document.querySelectorAll('.container-element-nav');
const containerAside = document.getElementById('container-aside');

btnMenu.addEventListener('click', () => {
    navMainMenu.classList.toggle('container-main-nav--show');
    containerHeader.classList.toggle('container-header--width');
    body.classList.toggle('body-scroll-hidden');

    listOptionsMenu.forEach(element => {
        element.addEventListener('click', () => {
            navMainMenu.classList.remove('container-main-nav--show');
            containerHeader.classList.remove('container-header--width');
            body.classList.remove('body-scroll-hidden');
        })
    });
});

window.addEventListener('scroll', () => {
    if (window.innerWidth >= 800 && window.scrollY > 200) {
        containerAside.classList.add('container-aside--show');
    } else {
        containerAside.classList.remove('container-aside--show');
    }
});