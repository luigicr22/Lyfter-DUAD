function cancel() {
    window.location.href = "myprofile.html";
}

function checkLogin(){
    if (!isUserLoggedIn()){
        alert("Sesión expirada.");
        sessionStorage.clear();
        window.location.href = "login.html";
    }
};

async function changePassword() {
    const currentPassword = document.getElementById("form-current-password").value;
    const newPassword = document.getElementById("form-new-password").value;
    const confirmPassword = document.getElementById("form-confirm-password").value;

    if (!currentPassword || !newPassword || !confirmPassword) {
        alert("Por favor, complete todos los campos.");
        return;
    }
    try{
        if (newPassword === confirmPassword) {
            const dataApi = await getApi (sessionStorage.getItem("userId"));
            if (dataApi.data.password === currentPassword) {
                const data = {"name":sessionStorage.getItem("name"),"data":{"email":sessionStorage.getItem("email"),"password":newPassword,"address":sessionStorage.getItem("address")}};
                const userData = await putApi(sessionStorage.getItem("userId"),data);
                alert("Contraseña Actualizada.");
                window.location.href = "myprofile.html";
            }
            else {
                alert("La contraseña actual es incorrecta.");
            }
        } else {
            alert("La nueva contraseña no coincide con la confirmación.");
        };
    } catch (error) {
        console.error("Error al cambiar la contraseña:", error);
        alert("Ocurrió un error al cambiar la contraseña.");
        //Para el punto 1.4 de Ejercicios de Requests y DOM, como se toma el id del SessionStorage ya se valida que exista.
        //De igual manera la contraseña se valida contra la API.
    };
}

checkLogin();
const buttonChange = document.getElementById("button-change");
const buttonCancel = document.getElementById("button-cancel");
buttonCancel.addEventListener("click", cancel);
buttonChange.addEventListener("click", changePassword);