function updateAndFormat() {
  // resetTableRows();
  updateDraggable();
  formatWeekends()
  addEventsOnCardsAndCells();
}


function isWeekend(dateString) {
  var parts = dateString.split("/");
  var date = new Date(parts[2], parts[1] - 1, parts[0]);
  var day = date.getDay();
  return day === 0 || day === 6;
}

function addEventsOnCardsAndCells() {
  const cards = document.querySelectorAll('.card');
  cards.forEach((card) => {
    card.addEventListener('dragstart', handleDragStart);
  })
  const tdCells = document.querySelectorAll('.tdCell');
  tdCells.forEach((tdCell) => {
    // drag zone
    tdCell.addEventListener('dragstart', handleDragStart);
    // drop zone
    tdCell.addEventListener('dragover', handleDragOver);
    tdCell.addEventListener('dragleave', handleDragLeave);
    tdCell.addEventListener('drop', handleDrop);
  })
}

function resetTableRows() {
  const existingTableRows = document.querySelectorAll('.trRow');
  if (existingTableRows.length > 0) {
    existingTableRows.forEach(row => {
      row.remove();
    });
  }
}



// DRAG AND DROP events
function updateDraggable() {
  const tdCells = document.querySelectorAll('.tdCell');
  tdCells.forEach((tdCell) => {
    let x = tdCell.innerHTML.trim();
    if (x.length > 0) {
      tdCell.draggable = true;
      tdCell.classList.add('draggable');
    } else {
      tdCell.draggable = false;
      tdCell.classList.remove('draggable');
    }
  })
}

function formatWeekends() {
  const tdRows = document.querySelectorAll('.trRow');
  tdRows.forEach((tdRow) => {
    let date = tdRow.querySelectorAll(".tdCellDate")[0].innerHTML.trim();
    if (isWeekend(date)) {
      tds = tdRow.getElementsByTagName("td");
      for (let i = 0; i < tds.length; i++) {
        const element = tds[i];
        element.classList.add("weekend");
      }
    }
  })
}

function handleDragStart(event) {
  draggedElement = this;
  event.dataTransfer.setData('text/plain', draggedElement.id);
  if (draggedElement.classList.contains('tdCell')) {
    event.dataTransfer.effectAllowed = "move";
  } else {
    event.dataTransfer.effectAllowed = "copy";
  }
}

function handleDragOver(event) {
  event.preventDefault();
  targetElement = event.target;
  if (targetElement.classList.contains('tdCell')) {
    targetElement.classList.add('bg-primary');
  }
}

function handleDragLeave(event) {
  event.preventDefault();
  event.target.classList.remove('bg-primary');
}
function handleDrop(event) {
  event.preventDefault();
  const data = event.dataTransfer.getData('text/plain');
  const draggedElement = document.getElementById(data);
  const currentElement = event.target;
  let saveValue = currentElement.innerHTML;
  if (draggedElement.classList.contains('tdCell')) {
    currentElement.innerHTML = draggedElement.innerHTML;
    draggedElement.innerHTML = saveValue;
  } else {
    currentElement.innerHTML = draggedElement.innerHTML;
  }
  event.target.classList.remove('bg-primary');

  if (currentElement.innerHTML.trim() !== '') {
    currentElement.draggable = true;
    if (!currentElement.classList.contains('draggable')) {
      currentElement.classList.add('draggable');
    }
  } else {
    currentElement.draggable = false;
    currentElement.classList.remove('draggable');
  }

  if (draggedElement.innerHTML.trim() !== '') {
    draggedElement.draggable = true;
    if (!draggedElement.classList.contains('draggable')) {
      draggedElement.classList.add('draggable');
    }
  } else {
    draggedElement.draggable = false;
    draggedElement.classList.remove('draggable');
  }
  saveButton.disabled = false;
}

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
// function saveDatafromTable(event, form) {
//   event.preventDefault();
//   console.log('save button clicked');
  
//   fetch (form.action, {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//     },
//     body: JSON.stringify(dataJSON),
//   })
//   form.submit();
// }

function saveButtonClicked(params) {
  var dataJSON = {};
  const tdRows = document.getElementsByClassName('trRow');
  for (let index = 0; index < tdRows.length; index++) {
    let rand = tdRows[index];
    let data = rand.children[0].innerHTML.trim();
    let tura1 = rand.children[1].innerHTML.trim();
    let tura2 = rand.children[2].innerHTML.trim();
    let tura3 = rand.children[3].innerHTML.trim();
    dataJSON[data] = [tura1, tura2, tura3];
  }
  var data = JSON.stringify(dataJSON);
  let csrftoken = getCookie('csrftoken');
  let response = fetch("", {
    method: 'POST',
    body: data,
    headers: {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        "X-CSRFToken": [csrftoken],
        "action" : "save",
    },
  });
}


// // // // // MAIN PROGRAM // // // // //

// SAVE button management
const saveButton = document.getElementById('saveButton');
saveButton.addEventListener('click', saveButtonClicked);

// add listener for modifying #end_date
const dates = document.getElementById('dates');
const startDateInput = document.getElementById('start-date');
const endDateInput = document.getElementById('end-date');


endDateInput.addEventListener('input', function () {
    dates.submit();
})

updateAndFormat();

