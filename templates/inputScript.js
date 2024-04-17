
function handleSubmit(e) {
    e.preventDefault();
    let formData = new FormData(this);
    let temperature = formData.get('temperature');
    let wind = formData.get('wind');
    let humidity = formData.get('humidity');
    let plantMoisture = formData.get('plant-moisture');
    let soilMoisture = formData.get('soil-moisture');
    console.log(temperature, wind, humidity, plantMoisture, soilMoisture);
    if (Math.random() > 0.5) {
        myForm.innerHTML = '<img src="./assets/noActionNeeded.jpg" alt="Action Needed" style="width: 400px; height: 400px; border-radius: 10px;"><p class="noActionNeeded">No Action Needed !</p>'
    }
    else {
        myForm.innerHTML = '<img src="./assets/actionNeeded.jpg" alt="Action Needed" style="width: 100%; height: auto; border-radius: 10px;"><p class="actionNeeded">Action Needed !</p>'
    }
}

const myForm = document.getElementById('myForm');
myForm.addEventListener('submit', handleSubmit);