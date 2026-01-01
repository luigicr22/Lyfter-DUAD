const navbarCategoriesContainer = document.getElementById("navbar-categories-container");

const navbarSearch = document.getElementById("navbar-search");
const newTask = document.getElementById("new-task-button");
const newCategory = document.getElementById("categories-button");
const navbarDownload = document.getElementById("navbar-download");
const navbarDeleteCompleted = document.getElementById("navbar-delete-completed");
const navbarAlltasks = document.getElementById("navbar-alltasks");
const navbarPending = document.getElementById("navbar-pending");
const navbarCompleted = document.getElementById("navbar-completed");
const navbarExpired = document.getElementById("navbar-expired");
const navbarToday = document.getElementById("navbar-today");
const navbarWeek = document.getElementById("navbar-week");
const navbarMonth = document.getElementById("navbar-month");
const navbarWithCategory = document.getElementById("navbar-with-category");

navbarSearch.addEventListener("input", () => {
    cleanWindow();
    mainTitle.textContent = "Búsqueda Palabra Clave";
    pendingContainer.innerHTML = "";
    completedContainer.innerHTML = "";

    const listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
    listTasks.forEach ((task) => {        
        const title = task.title.toLowerCase();
        const description = task.description.toLowerCase();
        if (title.includes(navbarSearch.value.toLowerCase()) || description.includes(navbarSearch.value.toLowerCase())){
            const taskElement = createTaskElement(task);            
            if (task.status === "completed") {
                completedContainer.appendChild(taskElement);
            } else {
                pendingContainer.appendChild(taskElement);
            }
        };
    });
});

navbarSearch.addEventListener("click", () =>  {
    navbarSearch.value = "";
});

newTask.addEventListener("click", (e) => {
    cleanWindow();
    mainContainer.style.gridColumn = "span 1";
    taskDetailsContainer.style.display = "flex";
    newTaskDetails();    
});

newCategory.addEventListener("click", (e) => {
    cleanWindow();
    mainContainer.style.gridColumn = "span 1";
    categoriesContainer.style.display = "flex";
    newCategoryDetails();
});

navbarDownload.addEventListener('click', () => {
    const data = sessionStorage.getItem('listTasks');
    const blob = new Blob([data], { type: 'application/json' });
    
    const url = URL.createObjectURL(blob);

    const link = document.createElement('a');
    link.href = url;
    link.download = 'TaskList.json';

    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    URL.revokeObjectURL(url);
});

navbarDeleteCompleted.addEventListener('click', async() => {
    const confirmed = confirm("¿Estás seguro de que deseas eliminar todas las tareas completadas?");
    if (confirmed){
        let listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
        let newListTasks = [];
        listTasks.forEach ((task) => {
            if (task.status === "pending"){
                newListTasks.push(task);
            }
        });
        listTasks = newListTasks;
        sessionStorage.setItem("listTasks", JSON.stringify(listTasks));
        alert("Tareas completadas eliminadas correctamente.");
        await patchApi();
    }
    cleanWindow();
    fillTasksList();
});

navbarAlltasks.addEventListener('click', () => {
    cleanWindow();
    fillTasksList();
})

navbarPending.addEventListener('click',() => {
    cleanWindow();
    mainTitle.textContent = "Tareas Pendientes";
    completedContainer.innerHTML = "";
    completedContainer.style.display = 'none';
    document.getElementById('completed-container-title').style.display = 'none';
    pendingContainer.innerHTML = "";

    const listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
    listTasks.forEach((task) => {
        if (task.status === "pending"){
            const taskElement = createTaskElement(task);
            pendingContainer.appendChild(taskElement);
        }
    });
});

navbarCompleted.addEventListener('click',() => {
    cleanWindow();
    mainTitle.textContent = "Tareas Completadas";
    pendingContainer.innerHTML = "";
    pendingContainer.style.display = 'none';
    document.getElementById('pending-container-title').style.display = 'none';
    completedContainer.innerHTML = "";

    const listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
    listTasks.forEach((task) => {
        if (task.status === "completed"){
            const taskElement = createTaskElement(task);
            completedContainer.appendChild(taskElement);
        }
    });
});

navbarExpired.addEventListener('click',() => {
    cleanWindow();
    mainTitle.textContent = "Tareas Vencidas";
    pendingContainer.innerHTML = "";
    completedContainer.innerHTML = "";
    const todayDate = new Date();
    todayDate.setHours(0,0,0,0);

    const listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
    listTasks.forEach((task) => {
        const dueDate = new Date(task.dueDate + 'T00:00:00');
        if (dueDate.getTime() < todayDate.getTime()){
            const taskElement = createTaskElement(task);            
            if (task.status === "completed") {
                completedContainer.appendChild(taskElement);
            } else {
                pendingContainer.appendChild(taskElement);
            }
        }
    });
});

navbarToday.addEventListener('click',() => {
    cleanWindow();
    mainTitle.textContent = "Tareas Para Hoy";
    pendingContainer.innerHTML = "";
    completedContainer.innerHTML = "";
    const todayDate = new Date();
    todayDate.setHours(0,0,0,0);

    const listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
    listTasks.forEach((task) => {
        const dueDate = new Date(task.dueDate + 'T00:00:00');
        if (dueDate.getTime() == todayDate.getTime()){
            const taskElement = createTaskElement(task);            
            if (task.status === "completed") {
                completedContainer.appendChild(taskElement);
            } else {
                pendingContainer.appendChild(taskElement);
            }
        }
    });
});

navbarWeek.addEventListener('click',() => {
    cleanWindow();
    mainTitle.textContent = "Tareas Para Esta Semana";
    pendingContainer.innerHTML = "";
    completedContainer.innerHTML = "";
    const todayDate = new Date();
    const weekLaterDate = new Date();
    weekLaterDate.setDate(todayDate.getDate() + 7);
    todayDate.setHours(0,0,0,0);
    weekLaterDate.setHours(0,0,0,0);

    const listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
    listTasks.forEach((task) => {
        const dueDate = new Date(task.dueDate + 'T00:00:00');
        if (dueDate.getTime() >= todayDate.getTime() && dueDate.getTime() <= weekLaterDate.getTime()){
            const taskElement = createTaskElement(task);            
            if (task.status === "completed") {
                completedContainer.appendChild(taskElement);
            } else {
                pendingContainer.appendChild(taskElement);
            }
        }
    });
});

navbarMonth.addEventListener('click',() => {
    cleanWindow();
    mainTitle.textContent = "Tareas Para Este Mes";
    pendingContainer.innerHTML = "";
    completedContainer.innerHTML = "";
    const todayDate = new Date();
    const thisMonthDate = new Date();
    todayDate.setHours(0,0,0,0);
    thisMonthDate.setHours(0,0,0,0);

    const listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
    listTasks.forEach((task) => {
        const dueDate = new Date(task.dueDate + 'T00:00:00');
        if (dueDate.getMonth() == todayDate.getMonth() && dueDate.getFullYear() == todayDate.getFullYear()){
            const taskElement = createTaskElement(task);            
            if (task.status === "completed") {
                completedContainer.appendChild(taskElement);
            } else {
                pendingContainer.appendChild(taskElement);
            }
        }
    });
});

navbarWithCategory.addEventListener('click',() => {
    cleanWindow();
    pendingContainer.innerHTML = "";
    mainTitle.textContent = "Tareas Con Categoría";
    completedContainer.innerHTML = "";

    const listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
    listTasks.forEach((task) => {
        if (task.category != 0){
            const taskElement = createTaskElement(task);            
            if (task.status === "completed") {
                completedContainer.appendChild(taskElement);
            } else {
                pendingContainer.appendChild(taskElement);
            }
        }
    });
});

navbarCategoriesContainer.addEventListener('click',(e)=>{
    cleanWindow();
    pendingContainer.innerHTML = "";
    completedContainer.innerHTML = "";
    categoryId = parseInt(e.target.id);

    const listCategories = JSON.parse(sessionStorage.getItem('listCategories'));
    mainTitle.textContent = "Tareas " + listCategories.find(c => c.id === categoryId).name;

    const listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
    listTasks.forEach((task) => {
        if (task.category == categoryId){
            const taskElement = createTaskElement(task);            
            if (task.status === "completed") {
                completedContainer.appendChild(taskElement);
            } else {
                pendingContainer.appendChild(taskElement);
            }
        }
    });
});

function fillCategoriesNavbar(){
    navbarCategoriesContainer.innerHTML = "";
    const listCategories = JSON.parse(sessionStorage.getItem('listCategories'));
    listCategories.forEach(category => {
        const button = document.createElement("button");
        button.textContent = category.name;
        button.id = category.id;
        button.classList.add("category");
        navbarCategoriesContainer.appendChild(button);
    });
}