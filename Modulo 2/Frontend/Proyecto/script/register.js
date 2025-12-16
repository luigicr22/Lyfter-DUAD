async function registerUser() {
    const name = document.getElementById('form-name').value;
    const email = document.getElementById('form-email').value;
    const password = document.getElementById('form-password').value;

    if (!name || !email || !password) {
        alert("Por favor, complete todos los campos del formulario.");
        return;
    }
    
    try{
        let listCategories = [
            {
                id: 0,
                name: "Sin categoría",
                backgroundColor: "#ffffff",
                color: "#ffffff"
            },
        ];
        const data = {"name":name,"data":{"email":email,"password":password,"categoryIdCounter" : 1, "listCategories" : listCategories, "taskIdCounter" : 1, "listTasks" : []}};
        const user = await postApi(data);
        navigator.clipboard.writeText(user.id);
        alert("Usuario registrado.\nID creado: " + user.id + "\n(copiado en el portapapeles)");
        window.location.href = "login.html";
    }
    catch (error){
        console.log("Error: ",error);
        alert("Error al registrar el usuario. Intente nuevamente.");
    };
}

const buttonRegister = document.getElementById('button-register');
buttonRegister.addEventListener('click', registerUser);
