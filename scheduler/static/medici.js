console.log("Am incarcat fisierul medici.js");

var actualSelectedRecord = null;

const mediciRecords = document.querySelectorAll('.medicRecord');
console.log(mediciRecords);

document.getElementById("root").addEventListener("mouseleave", (event) => {
    event.preventDefault();
    if (actualSelectedRecord) {
        let activeButtons = actualSelectedRecord.querySelectorAll('.context-button');
        activeButtons.forEach((activeButton) => {
            activeButton.classList.add('context-button-none');
        })
    };
})

mediciRecords.forEach((medicRecord) => {
    const editButton = medicRecord.querySelector('.medicEditButton');
    const deleteButton = medicRecord.querySelector('.medicDeleteButton');
    const acceptButton = medicRecord.querySelector('.medicAcceptButton');

    medicRecord.addEventListener('click', (event) => {
        if (actualSelectedRecord) {
            console.log(actualSelectedRecord);
            let activeButtons = actualSelectedRecord.querySelectorAll('.context-button');
            activeButtons.forEach((activeButton) => {
                activeButton.classList.add('context-button-none');
            })
        }
        editButton.classList.remove('context-button-none');
        deleteButton.classList.remove('context-button-none');
        actualSelectedRecord = medicRecord;
        })
    })

