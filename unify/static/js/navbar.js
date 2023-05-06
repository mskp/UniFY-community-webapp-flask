const activePage = location.href
const links = document.querySelectorAll(".nav-links li a")

links.forEach(link => {
    if (link.href === activePage)
        link.classList.add('active-nav')
})

const menuBtn = document.querySelector('.menu-btn')
const navLinks = document.querySelector('.nav-links')
const body = document.querySelector('body')

menuBtn.addEventListener('click', () => {
    menuBtn.classList.toggle('active')
    navLinks.classList.toggle('active')
    body.classList.toggle('overflow-hide')
})

document.querySelectorAll('.nav-links li').forEach(i => {
    i.addEventListener('click', () => {
        menuBtn.classList.remove('active')
        navLinks.classList.remove('active')
    })
})