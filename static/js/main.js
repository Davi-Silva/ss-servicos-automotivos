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

companyWorked[0].addEventListener('mouseover', () => {
    console.log(companyWorked)
    companyWorked[0].style.opacity = "1"
    companyWorked[0].style.transition = "all 0.4s ease-in-out"
})

companyWorked[0].addEventListener('mouseout', () => {
    console.log(companyWorked)
    companyWorked[0].style.opacity = "0"
    companyWorked[0].style.transition = "all 0.4s ease-in-out"
})

companyWorked[1].addEventListener('mouseover', () => {
    console.log(companyWorked)
    companyWorked[1].style.opacity = "1"
    companyWorked[1].style.transition = "all 0.4s ease-in-out"
})

companyWorked[1].addEventListener('mouseout', () => {
    console.log(companyWorked)
    companyWorked[1].style.opacity = "0"
    companyWorked[1].style.transition = "all 0.4s ease-in-out"
})

companyWorked[2].addEventListener('mouseover', () => {
    console.log(companyWorked)
    companyWorked[2].style.opacity = "1"
    companyWorked[2].style.transition = "all 0.4s ease-in-out"
})

companyWorked[2].addEventListener('mouseout', () => {
    console.log(companyWorked)
    companyWorked[2].style.opacity = "0"
    companyWorked[2].style.transition = "all 0.4s ease-in-out"
})

companyWorked[3].addEventListener('mouseover', () => {
    console.log(companyWorked)
    companyWorked[3].style.opacity = "1"
    companyWorked[3].style.transition = "all 0.4s ease-in-out"
})

companyWorked[3].addEventListener('mouseout', () => {
    console.log(companyWorked)
    companyWorked[3].style.opacity = "0"
    companyWorked[3].style.transition = "all 0.4s ease-in-out"
})

