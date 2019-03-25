let navigationBar = document.querySelector("#navigation")
console.log(navigationBar)
navigationBar.style.backgroudColor = "#fff!important"

let companyWorked = document.querySelectorAll(".company-worked .work-experience-description-container")
console.log(companyWorked)


companyWorked.forEach((container) => {
    container.style.opacity = "1"
})

