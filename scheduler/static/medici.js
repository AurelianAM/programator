console.log("Am incarcat fisierul medici.js");

var currentRecordClicked = null;

function medicRecordClicked(event) {
    let cellToRemove = document.querySelector('#modifyButton');
    if (cellToRemove) {
        currentRecordClicked.removeChild(cellToRemove);
    }
    let clickedRow = event.target.parentElement;
    const newButtonElement = 
    `<td id="modifyButton"><button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalModifyMedic" style="--bs-btn-padding-y: .1rem; --bs-btn-padding-x: .2rem; --bs-btn-font-size: 1rem;">
        <i class="bi bi-pencil"></i>
    </button></td>`
    clickedRow.insertAdjacentHTML('beforeend', newButtonElement);

    const modalWindow = document.querySelector('#modalModifyMedic');
    const formModifieMedicForm = modalWindow.querySelector('#formModifieMedic');
    const cancelButton = modalWindow.querySelector('#cancelButton');
    const saveChangesButton = modalWindow.querySelector('#saveChangesButton');

    const inputmodifieNickname = modalWindow.querySelector('#modifiedNickname');
    const inputmodifieFirstName = modalWindow.querySelector('#modifiedFirstName');
    const inputmodifieLastName = modalWindow.querySelector('#modifiedLastName');
    const inputactualMedicId = modalWindow.querySelector('#actualMedicId');

    inputactualMedicId.value = clickedRow.querySelector(".medicId").innerHTML;
    inputmodifieNickname.value = clickedRow.querySelector(".medicNickname").innerHTML;
    inputmodifieFirstName.value = clickedRow.querySelector(".medicFirstName").innerHTML;
    inputmodifieLastName.value = clickedRow.querySelector(".medicLastName").innerHTML;


    cancelButton.addEventListener('click', () => {
        let cellToRemove = document.querySelector('#modifyButton');
        if (cellToRemove) {
            clickedRow.removeChild(cellToRemove);
        }
    })

    saveChangesButton.addEventListener('click', (event) => {
        event.preventDefault();
        formModifieMedicForm.submit();
    })

    currentRecordClicked = clickedRow;
}

const medicRecords = document.querySelectorAll('.medicRecord');
medicRecords.forEach((medicRecord) => {
    medicRecord.addEventListener("click", medicRecordClicked);
});

const addNewMedicButton = document.querySelector('#addNewMedicButton');
addNewMedicButton.addEventListener('click', () => {
    const modalWindow = document.querySelector('#modalAddNewMedic');
    const formAddNewMedicForm = modalWindow.querySelector('#formAddNewMedic');
    // const cancelButton = modalWindow.querySelector('#cancelNewButton');
    const saveNewButton = modalWindow.querySelector('#saveNewButton');

    // const inputNewNickname = modalWindow.querySelector('#newNickname');
    // const inputNewFirstName = modalWindow.querySelector('#newFirstName');
    // const inputNewLastName = modalWindow.querySelector('#newFirstName');

    saveNewButton.addEventListener('click', (event) => {
        event.preventDefault();
        formAddNewMedicForm.submit();
    })
})
