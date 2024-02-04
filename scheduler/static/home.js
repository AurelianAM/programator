
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

function printElement(element) {
    window.print();
}

function getWeekDay(strDate) {
    day = new Date(strDate).getDay();
    switch (day) {
        case 0:
            return 'Du';
        case 1:
            return 'Lu';
        case 2:
            return 'Ma';
        case 3:
            return 'Mi';
        case 4:
            return 'Jo';
        case 5:
            return 'Vi';
        case 6:
            return 'Sa';
    }
}

function setWeekDays(params) {
    let allDates = document.querySelectorAll('.tdCellDate');
    for (let index = 0; index < allDates.length; index++) {
        strDate = allDates[index].innerHTML;
        allDates[index].innerHTML = strDate + '  ' + getWeekDay(strDate);

    }
}



console.log("Am incarcat fisierul home.js");
const printButton = document.getElementById('printButton');
printButton.addEventListener('click', printElement);


const dates = document.getElementById('dates');
const startDateInput = document.getElementById('start-date');
const endDateInput = document.getElementById('end-date');



endDateInput.addEventListener('input', function (event) {
    event.preventDefault();
    dates.submit();
})


// $(document).ready(function () {
//     setWeekDays();
// })



// const table = document.getElementById('table');
// table.onchange = function (event) {
//     console.log("changed");
// }

// startDateInput.value = setStartDate().toISOString().split('T')[0];
// endDateInput.value = setEndDate().toISOString().split('T')[0];