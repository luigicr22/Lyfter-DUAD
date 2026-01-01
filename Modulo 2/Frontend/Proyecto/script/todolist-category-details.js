const categoriesList = document.getElementById('categories-list');
const categoryDetailsContainer = document.getElementById('category-details-container');
const categoryDetailsName = document.getElementById('category-details-name');
const categoryDetailsColor = document.getElementById('category-details-color');
const categoryDetailsTextColor = document.getElementById('category-details-text-color');
const buttonNewCategory = document.getElementById('button-new-category');
const buttonEditCategory = document.getElementById('button-edit-category');
const buttonSaveCategory = document.getElementById('button-save-category');
const buttonCancelCategory = document.getElementById('button-cancel-category');
const buttonEraseCategory = document.getElementById('button-erase-category');
const buttonCancelCategoriesList = document.getElementById('button-cancel-categories-list');
let categoryId = null;

function newCategoryDetails() {
    categoriesList.innerHTML = '';
    const listCategories = JSON.parse(sessionStorage.getItem('listCategories'));
    listCategories.forEach((category) => {
        if (category.id === 0) return;
        const categoryElement = document.createElement("span");
        categoryElement.id = category.id;
        categoryElement.textContent = category.name;
        categoryElement.style.backgroundColor = category.backgroundColor;
        categoryElement.style.color = category.color;
        categoriesList.appendChild(categoryElement);
    });
}

categoriesList.addEventListener('click', (event) => {
    categoryId = parseInt(event.target.id);
    const listCategories = JSON.parse(sessionStorage.getItem('listCategories'));
    const category = listCategories.find(cat => cat.id === categoryId);
    categoryDetailsName.value = category.name;
    categoryDetailsName.disabled = true;
    categoryDetailsColor.value = category.backgroundColor;
    categoryDetailsColor.disabled = true;
    categoryDetailsTextColor.value = category.color;
    categoryDetailsTextColor.disabled = true;
    buttonSaveCategory.disabled = true;
    buttonEditCategory.disabled = false;
    buttonEraseCategory.disabled = false;
    categoryDetailsContainer.style.display = "flex";
});

buttonCancelCategoriesList.addEventListener('click', () => {
    cleanWindow();
});

buttonCancelCategory.addEventListener('click', () => {
    categoryDetailsContainer.style.display = "none";
});

buttonNewCategory.addEventListener('click', () => {
    categoryDetailsName.value = "";
    categoryDetailsName.disabled = false;
    categoryDetailsColor.value = "";
    categoryDetailsColor.disabled = false;
    categoryDetailsTextColor.value = '#ffffff';
    categoryDetailsTextColor.disabled = false;
    buttonSaveCategory.disabled = false;
    buttonEditCategory.disabled = true;
    buttonEraseCategory.disabled = true;
    categoryDetailsContainer.style.display = "flex";
    categoryId = null;
});

buttonEditCategory.addEventListener('click', ()=>{
    categoryDetailsName.disabled = false;
    categoryDetailsColor.disabled = false;
    categoryDetailsTextColor.disabled = false;
    buttonSaveCategory.disabled = false;
    buttonEditCategory.disabled = true;
    buttonEraseCategory.disabled = true;
});

buttonSaveCategory.addEventListener('click', async ()=>{
    if (!categoryDetailsName.value){
        alert("Por favor, complete al menos el nombre de la categoría.");
        return;
    }
    if (categoryId === null){
        let listCategories = JSON.parse(sessionStorage.getItem('listCategories'));
        let categoryIdCounter = Number(sessionStorage.getItem('categoryIdCounter'));
        const newCategory = {
            id: categoryIdCounter,
            name: categoryDetailsName.value,
            backgroundColor: categoryDetailsColor.value,
            color: categoryDetailsTextColor.value,
        };
        listCategories.push(newCategory);
        categoryIdCounter++;
        sessionStorage.setItem("categoryIdCounter", String(categoryIdCounter));
        sessionStorage.setItem("listCategories", JSON.stringify(listCategories));
    }
    else{
        let listCategories = JSON.parse(sessionStorage.getItem('listCategories'));
        const category = listCategories.find(c => c.id === categoryId);
        category.name = categoryDetailsName.value;
        category.backgroundColor = categoryDetailsColor.value;
        category.color = categoryDetailsTextColor.value;
        sessionStorage.setItem("listCategories", JSON.stringify(listCategories));
    }
    await patchApi();
    categoryDetailsContainer.style.display = "none";
    refreshListCategories();
    alert("Cambios guardados correctamente.");
});

buttonEraseCategory.addEventListener('click', async () => {
    let listCategories = JSON.parse(sessionStorage.getItem('listCategories'));
    if (listCategories.find(cat => cat.id === categoryId)){
        if (confirm ("¿Está seguro que desea eliminar esta categoría?")){
            categoryToErase = listCategories.findIndex(cat => cat.id === categoryId);
            listCategories.splice (categoryToErase, 1);
            let listTasks = JSON.parse(sessionStorage.getItem('listTasks'));
            let newlistTasks = [];
            listTasks.forEach((task) => {
                if (task.category === categoryId){
                    task.category = 0;
                    newlistTasks.push(task);
                }
                else{
                    newlistTasks.push(task);
                }
            });
            listTasks = newlistTasks;
            sessionStorage.setItem("listTasks", JSON.stringify(listTasks));
            sessionStorage.setItem("listCategories", JSON.stringify(listCategories));
            await patchApi();
            refreshListCategories();
            alert ("Categoría eliminada correctamente.");
        }
    }
    else{
        alert("Error: La categoría no existe.");
    }
});

function refreshListCategories (){
    cleanWindow();
    fillTasksList();
    mainContainer.style.gridColumn = "span 1";
    categoriesContainer.style.display = "flex";
    newCategoryDetails();
    fillCategoriesNavbar()
};

