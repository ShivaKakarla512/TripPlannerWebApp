/*===== FOCUS =====*/
const inputs = document.querySelectorAll(".form__input")

/*=== Add focus ===*/
function addfocus(){
    let parent = this.parentNode.parentNode
    parent.classList.add("focus")
}

/*=== Remove focus ===*/
function remfocus(){
    let parent = this.parentNode.parentNode
    if(this.value == ""){
        parent.classList.remove("focus")
    }
}

/*=== To call function===*/
inputs.forEach(input=>{
    input.addEventListener("focus", addfocus)
    input.addEventListener("blur", remfocus)
})

/*===== MENU SHOW Y HIDDEN =====*/
const navMenu = document.getElementById('nav-menu'),
    toggleMenu = document.getElementById('nav-toggle'),
    closeMenu = document.getElementById('nav-close')

// SHOW
toggleMenu.addEventListener('click', ()=>{
    navMenu.classList.toggle('show')
})

// HIDDEN
closeMenu.addEventListener('click', ()=>{
    navMenu.classList.remove('show')
})

const main = document.getElementById('main');

main.addEventListener('click', () => {
    navMenu.classList.remove('show')
})

/*===== MOUSEMOVE HOME IMG =====*/
document.addEventListener('mousemove', move);

function move(e){
    this.querySelectorAll('.move').forEach(layer =>{
        const speed = layer.getAttribute('data-speed')

        const x = (window.innerWidth - e.pageX*speed)/120
        const y = (window.innerHeight - e.pageY*speed)/120

        layer.style.transform = `translateX(${x}px) translateY(${y}px)`
    })
}


/*===== GSAP ANIMATION =====*/
TweenMax.to('.nav__logo, .nav__item, .nav__toggle, .home__title, .home__description, .home__button, .form__content, .plans, .img, .header, .secondheader', 0, {
    autoAlpha: 1
});

// NAV
gsap.from('.nav__logo, .nav__toggle', {opacity: 0, duration: 1, delay:.2, y: 10})
gsap.from('.nav__item', {opacity: 0, duration: 1, delay: .4, y: 30, stagger: 0.2,})

// HOME
gsap.from('.home__title', {opacity: 0, duration: 1, delay:.8, y: 30})
gsap.from('.home__description', {opacity: 0, duration: 1, delay:1, y: 30})
gsap.from('.home__button', {opacity: 0, duration: 1, delay:1.2, y: 30})

// LOGIN/REGISTER
gsap.from('.form__content', {opacity: 0, duration: 1, delay:.8, y: 30})
gsap.from('.img', {opacity: 0, duration: 1, delay:1, y: 30})

//PLANS
gsap.from('.header', {opacity: 0, duration: 1, delay:.7, y: 30})
gsap.from('.plans', {opacity: 0, duration: 1, delay: 1, y: 30, stagger: 0.3})

gsap.from('.secondheader', {opacity: 0, duration: 1, delay:.85, y: 30})

TweenMax.to('.home__img', 7, {
    autoAlpha: 1
});
