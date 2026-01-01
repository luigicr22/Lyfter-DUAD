const mainContainer = document.getElementById("main-container");
const categoriesContainer = document.getElementById("categories-container");
const taskDetailsContainer = document.getElementById("task-details-container");
const logoutButton = document.getElementById('logout-button');

mainContainer.addEventListener("click", (e) => {
    if (e.target.classList.contains("task")) {
        if(e.target.classList.contains("selected")){
            cleanWindow();
        }
        else{
            cleanWindow();
            mainContainer.style.gridColumn = "span 1";
            e.target.classList.add("selected");
            e.target.parentElement.classList.add("selected");
            fillTaskDetails(e.target.parentElement.id);
            taskDetailsContainer.style.display = "flex";
        }   
    }

    if (e.target.classList.contains("status")){
        const task = e.target.parentElement;
        if (e.target.classList.contains("checked")){
            updateStatusTask(parseInt(e.target.parentElement.id), "pending");
            e.target.checked = false;
            e.target.classList.remove("checked");
            completedContainer.removeChild(task);
            pendingContainer.appendChild(task);
            cleanWindow();
            
        }
        else{
            updateStatusTask(parseInt(e.target.parentElement.id), "completed");
            e.target.checked = true;
            e.target.classList.add("checked");
            pendingContainer.removeChild(task);
            completedContainer.appendChild(task);
            cleanWindow();
        }
    }
});

logoutButton.addEventListener('click', logoutUser);


