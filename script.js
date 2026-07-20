let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menu.onclick = () => {
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}

window.onscroll = () => {
    menu.classList.remove('bx-x');
    navbar.classList.remove('active');
}

const typed = new Typed('.multiple-text',  {
    strings: ['Physical Fitness', 'Weight Gain', 'Strength Training', 'Fat Lose', 'Weightlifting', 'Running'],
    typeSpeed: 60,
    backSpeed: 60,
    backDelay: 1000,
    loop: true,
});
document.addEventListener("DOMContentLoaded", function () {
    let carousel = document.querySelector("#carouselExampleCaptions");
    let titleElement = document.querySelector("#contentTitle");
    let textElement = document.querySelector("#contentText");

    let slides = [
        { title: "Title for Slide 1", text: "Description for Slide 1." },
        { title: "Title for Slide 2", text: "Description for Slide 2." },
        { title: "Title for Slide 3", text: "Description for Slide 3." }
    ];

    carousel.addEventListener("slid.bs.carousel", function (event) {
        let index = event.to;
        titleElement.innerText = slides[index].title;
        textElement.innerText = slides[index].text;
    });
});

AOS.init({
    offset: 300,
    duration: 1400,
});
$(document).ready(function () {
    $(".join-btn").click(function () {
        $("body > *:not(.overlay, .login-form)").addClass("blur");
        $("#overlay, #loginForm").fadeIn();
    });

    $("#closeLogin").click(function () {
        $("body > *:not(.overlay, .login-form)").removeClass("blur");
        $("#overlay, #loginForm").fadeOut();
    });

    $("#loginFormSubmit").submit(function (e) {
        e.preventDefault();
        alert("Login Successful!");
        $("body > *:not(.overlay, .login-form)").removeClass("blur");
        $("#overlay, #loginForm").fadeOut();
    });
});