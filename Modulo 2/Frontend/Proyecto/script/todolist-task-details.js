const cancelButton = document.getElementById("task-details-cancel-button");
const saveButton = document.getElementById("task-details-save-button");
const deleteButton = document.getElementById("task-details-delete-button");

let taskId = null;

function fillTaskDetails(idTask){
    try{
        deleteButton.style.display = "";
        taskId = parseInt(idTask);
        const listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
        const task = listTasks.find(t => t.id === taskId);
        taskDetailsContainer.querySelector("#task-details-title").textContent = "Detalles de la Tarea";
        taskDetailsContainer.querySelector("#task-details-task-title").value = task.title;

        fillCategories();
        taskDetailsContainer.querySelector("#task-details-category").value = task.category;

        if(task.status === "completed"){
            taskDetailsContainer.querySelector("#task-details-completed").checked = true;
        }
        else{
            taskDetailsContainer.querySelector("#task-details-pending").checked = true;
        }

        taskDetailsContainer.querySelector("#task-details-due-date").value = task.dueDate;
        taskDetailsContainer.querySelector("#task-details-description").value = task.description;
    }
    catch(error){
        alert("Error al cargar los detalles de la tarea.");
    }
}

function fillCategories(){
    const categorySelect = taskDetailsContainer.querySelector("#task-details-category");
    categorySelect.innerHTML = `
        <option value="" disabled selected>--Seleccione una categoría--</option>`;

    const listCategories = JSON.parse(sessionStorage.getItem('listCategories'));
    listCategories.forEach(category => {
        const option = document.createElement("option");
        option.value = category.id;
        option.textContent = category.name;
        categorySelect.appendChild(option);
    });
}

cancelButton.addEventListener("click", (e) => {
    cleanWindow();
});

saveButton.addEventListener("click", async (e) => {
    if (!taskDetailsContainer.querySelector("#task-details-task-title").value || !taskDetailsContainer.querySelector("#task-details-category").value) {
        alert("Por favor, complete al menos el titulo y la categoría de la tarea.");
        return;
    }
    if (taskId === null){
        const listCategories = JSON.parse(sessionStorage.getItem('listCategories'));
        const newTaskCategory = listCategories.find(c => c.id === parseInt(taskDetailsContainer.querySelector("#task-details-category").value));
        let newTaskStatus = "";
        if (taskDetailsContainer.querySelector("#task-details-completed").checked){
                newTaskStatus = "completed";
            }
            else{
                newTaskStatus = "pending";
            }
        let taskIdCounter = Number(sessionStorage.getItem('taskIdCounter'));
        const newTask = {
            id: taskIdCounter,
            title: taskDetailsContainer.querySelector("#task-details-task-title").value,
            category: newTaskCategory.id,            
            status: newTaskStatus,
            dueDate: taskDetailsContainer.querySelector("#task-details-due-date").value,
            description: taskDetailsContainer.querySelector("#task-details-description").value,
        };
        let listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
        listTasks.push(newTask);
        taskIdCounter++;
        sessionStorage.setItem("taskIdCounter", String(taskIdCounter));
        sessionStorage.setItem("listTasks", JSON.stringify(listTasks));
        await patchApi();
    }
    else{
        let listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
        const task = listTasks.find(t => t.id === taskId);
        task.title = taskDetailsContainer.querySelector("#task-details-task-title").value;

        const listCategories = JSON.parse(sessionStorage.getItem('listCategories'));
        const category = listCategories.find(c => c.id === parseInt(taskDetailsContainer.querySelector("#task-details-category").value));
        task.category = category.id;
        
        if (taskDetailsContainer.querySelector("#task-details-completed").checked){
            task.status = "completed";
        }
        else{
            task.status = "pending";
        }
        task.dueDate = taskDetailsContainer.querySelector("#task-details-due-date").value;
        task.description = taskDetailsContainer.querySelector("#task-details-description").value;
        sessionStorage.setItem("listTasks", JSON.stringify(listTasks));
        await patchApi();
    }
    cleanWindow();
    fillTasksList();
    alert("Cambios guardados correctamente.");
});

function newTaskDetails(){
    taskId = null;
    taskDetailsContainer.querySelector("#task-details-title").textContent = "Nueva Tarea";
    taskDetailsContainer.querySelector("#task-details-task-title").value = "";
    taskDetailsContainer.querySelector("#task-details-category").value = "";
    fillCategories();
    taskDetailsContainer.querySelector("#task-details-completed").checked = false;
    taskDetailsContainer.querySelector("#task-details-pending").checked = false;
    taskDetailsContainer.querySelector("#task-details-due-date").value = "";
    taskDetailsContainer.querySelector("#task-details-description").value = "";
    deleteButton.style.display = "none";
}

deleteButton.addEventListener('click', async () => {
    const confirmed = confirm("¿Estás seguro de que deseas eliminar esta tarea?");
    if (confirmed){
        deleteTask(taskId);
        cleanWindow();
        fillTasksList();
        alert("Tarea eliminada correctamente.");
    }
});