console.log("Am incarcat fisierul medici.js");

var currentRecordClicked = null;

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }


function medicRecordClicked(event) {
    let cellToRemove = document.querySelector('#modifyButton');
    if (cellToRemove) {
        currentRecordClicked.removeChild(cellToRemove);
    }
    let clickedRow = event.target.parentElement;
    const newButtonElement = 
    `<td id="modifyButton">
        <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalModifyMedic" style="--bs-btn-padding-y: .1rem; --bs-btn-padding-x: .2rem; --bs-btn-font-size: 1rem;">
            <i class="bi bi-pencil"></i>
        </button>
        <button id="deleteMedicButton" class="btn btn-danger" style="--bs-btn-padding-y: .1rem; --bs-btn-padding-x: .2rem; --bs-btn-font-size: 1rem;">
            <i class="bi bi-trash"></i>
        </button>
    </td>`
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

    const deleteMedicButton = document.querySelector('#deleteMedicButton');
    deleteMedicButton.addEventListener('click', (event) => {
        event.preventDefault();
        let idToDelete = clickedRow.querySelector(".medicId").innerHTML;
        console.log(idToDelete);
        let csrftoken = getCookie('csrftoken');
        let response = fetch("", {
            method: 'POST',
            body: idToDelete,
            headers: {
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'test/plain',
                "X-CSRFToken": [csrftoken],
                "action" : "delete",
            },
        });
        alert(response)
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
