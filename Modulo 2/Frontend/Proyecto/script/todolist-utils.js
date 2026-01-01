const pendingContainer = document.getElementById("pending-container");
const completedContainer = document.getElementById("completed-container");
const mainTitle = document.getElementById("main-title");

checkUser();


function checkUser(){
    if (isUserLoggedIn()){
        fillTasksList();
        fillCategoriesNavbar();
        document.getElementById("user-name").textContent = sessionStorage.getItem("userName");
    }
    else{
        alert("Sesión expirada.");
        logoutUser();
    }
};

function cleanWindow(){
    taskDetailsContainer.style.display = "none";
    categoriesContainer.style.display = "none";
    categoryDetailsContainer.style.display = "none";
    pendingContainer.style.display = '';
    document.getElementById('pending-container-title').style.display = '';
    completedContainer.style.display = '';
    document.getElementById('completed-container-title').style.display = '';

    mainContainer.style.gridColumn = "span 2";
    mainContainer.querySelectorAll(".task").forEach((cell) => {
        cell.classList.remove("selected");
        cell.parentElement.classList.remove("selected");
    });
};

function fillTasksList(){
    pendingContainer.innerHTML = "";
    completedContainer.innerHTML = "";
    mainTitle.textContent = "Todas Las Tareas";

    const listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
    listTasks.forEach((task) => {
        const taskElement = createTaskElement(task);
        if (task.status === "completed") {
            completedContainer.appendChild(taskElement);
        } else {
            pendingContainer.appendChild(taskElement);
        }
    });
};

function createTaskElement(task) {
    const taskElement = document.createElement("div");
    taskElement.classList.add("task-container");
    taskElement.id = task.id;

    const statusCheckbox = document.createElement("input");
    statusCheckbox.type = "checkbox";
    statusCheckbox.classList.add("status");
    if (task.status === "completed") {
        statusCheckbox.checked = true;
        statusCheckbox.classList.add("checked");
    }
    taskElement.appendChild(statusCheckbox);

    const taskLabel = document.createElement("label");
    taskLabel.classList.add("task");
    taskLabel.textContent = task.title;
    const todayDate = new Date();
    todayDate.setHours(0,0,0,0);
    const dueDate = new Date(task.dueDate + 'T00:00:00');
    if (dueDate.getTime() < todayDate.getTime()){
        taskLabel.style.color = "red";
    }
    taskElement.appendChild(taskLabel);

    if (task.category != 0) {
        const categorySpan = document.createElement("span");
        const listCategories = JSON.parse(sessionStorage.getItem('listCategories'));
        const category = listCategories.find(c => c.id === task.category);
        categorySpan.textContent = category.name;
        categorySpan.style.backgroundColor = category.backgroundColor;
        categorySpan.style.color = category.color;
        taskElement.appendChild(categorySpan);
    }
    return taskElement;
};

async function deleteTask(idTask){
    let listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
    const indexTask = listTasks.findIndex(t => t.id === idTask);
    if (indexTask !== -1) {
        listTasks.splice(indexTask, 1);
    };
    sessionStorage.setItem("listTasks", JSON.stringify(listTasks));
    await patchApi();
};

async function updateStatusTask(idTask, status){
    let listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
    const task = listTasks.find(t => t.id === idTask);
    task.status = status;
    sessionStorage.setItem("listTasks", JSON.stringify(listTasks));
    await patchApi();
};
