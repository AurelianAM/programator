
function setStartDate() {
    const currentDate = new Date();
    const day = 2;
    const month = currentDate.getMonth();
    const year = currentDate.getFullYear();
    return new Date(year, month, day);
}

function setEndDate() {
    const currentDate = new Date();
    const lastDayOfThisMonth = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1);
    return lastDayOfThisMonth;
}


console.log("Am incarcat fisierul home.js");
const printButton = document.getElementById('printButton');


const dates = document.getElementById('dates');
const startDateInput = document.getElementById('start-date');
const endDateInput = document.getElementById('end-date');


endDateInput.addEventListener('input', function (event) {
    event.preventDefault();
    dates.submit();
    console.log("Submited " + dates);
})



// startDateInput.value = setStartDate().toISOString().split('T')[0];
// endDateInput.value = setEndDate().toISOString().split('T')[0];