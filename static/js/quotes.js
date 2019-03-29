let multipleCars = document.querySelector("#id_multiple_cars")
let secondCarModel = document.querySelector("#id_second_car_model")
let thirdCarModel = document.querySelector("#id_third_car_model")

// console.log(multipleCars.value)

console.log(multipleCars)
console.log(secondCarModel)
console.log(thirdCarModel)

multipleCars.addEventListener('change', () => {
    // console.log("Changed")
    console.log(multipleCars.value)
    if(multipleCars.value == "S") {
        secondCarModel.style.display = "block";
        thirdCarModel.style.display = "block";
    } else if (multipleCars.value == "N") {
        secondCarModel.style.display = "none";
        thirdCarModel.style.display = "none";
    }
})