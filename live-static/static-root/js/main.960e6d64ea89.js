let navigationBar = document.querySelector("#navigation")

window.onscroll = function (e) {
    if(window.scrollY >= 200) {
        navigationBar.style.opacity = "0"
        navigationBar.style.transform = "translateY(-60px)"
        navigationBar.style.transition = "all 0.2s ease-in-out"
    } else {
        navigationBar.style.opacity = "1"
        navigationBar.style.transform = "translateY(0px)"
        navigationBar.style.transition = "all 0.2s ease-in-out"
    }
};
