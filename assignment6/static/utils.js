let selectStartYear = document.getElementById('selectStartYear');
let selectEndYear = document.getElementById('selectEndYear');
let selectMonth = document.getElementById('selectMonth');

for (let i = 1816; i<=2012; i++){
    let opt = document.createElement('option');
    opt.value = i;
    opt.innerHTML = i;
    selectStartYear.appendChild(opt);
}

for (let i = 1816; i<=2012; i++){
    let opt = document.createElement('option');
    opt.value = i;
    opt.innerHTML = i;
    selectEndYear.appendChild(opt);
}

let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"];
for (let i = 0; i < 12; i++) {
    let opt = document.createElement('option');
    opt.value = months[i];
    opt.innerHTML = months[i];
    selectMonth.appendChild(opt);
}

function showTemperatureForm() {
    document.getElementById('co2_form').style.display ='none';
    document.getElementById('temperature_form').style.display ='block';
}

function showCo2Form() {
    document.getElementById('temperature_form').style.display ='none';
    document.getElementById('co2_form').style.display ='block';
}
