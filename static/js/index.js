'use strict';

const btnMenu = document.getElementById('btn-menu');
const navMainMenu = document.getElementById('nav-main');
const containerHeader = document.getElementById('header');
const body = document.getElementById('body');
const listOptionsMenu = document.querySelectorAll('.container-element-nav');
const containerAside = document.getElementById('container-aside');
const btnThemeMode = document.getElementById('btn-theme-mode');
const rootStyles = document.documentElement.style;

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

// Cambiar tema del portafolio
btnThemeMode.addEventListener('click', () => {
    body.classList.toggle('body--light');
    btnThemeMode.classList.toggle('fa-sun');

    if (body.classList.contains('body--light')) {
        rootStyles.setProperty('--color-primary', '#444444');
        rootStyles.setProperty('--bgcolor-secundary', '#FCFCFC');
        rootStyles.setProperty('--box-shadow', 'rgba(100, 100, 111, 0.2) 0px 7px 29px 0px');
    } else {
        rootStyles.setProperty('--color-primary', 'rgb(205, 205, 255)');
        rootStyles.setProperty('--bgcolor-secundary', 'rgb(42, 47, 76)');
        rootStyles.setProperty('--box-shadow', 'rgba(0, 0, 0, 0.16) 0px 10px 36px 0px, rgba(0, 0, 0, 0.06) 0px 0px 0px 1px');
    }
});