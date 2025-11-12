async function loginUser() {
    const user = document.getElementById("form-user").value;
    const password = document.getElementById("form-password").value;

    if (!user || !password) {
        alert("Por favor, complete todos los campos.");
        return;
    }

    try{
        const userData = await getApi (user);
        
        if (password === userData.data.password){
            updateSessionStorage(userData);
            sessionStorage.setItem("userTimestamp", new Date().toISOString());
            sessionStorage.setItem("isLoggedIn", "true");
            window.location.href = "myprofile.html";
            //Para el punto 1.2 de Ejercicios de Requests y DOM, todo lo que diga sessionStorage se cambia a localStorage.
            //Esto hace que la sesion persista aunque se cierre el navegador.
        }
        else{
            alert("Contraseña incorrecta. Intente nuevamente.");
        }

    }
    catch (error){
        if (error.response.status === 404){
            alert("Usuario no encontrado. Por favor, registrese.");
        } else {
            alert("Ocurrió un error al intentar iniciar sesión. Por favor, intente nuevamente más tarde.");
            console.log("Error: ", error);
        }        
    }
}

const loginButton = document.getElementById("login-button");
loginButton.addEventListener("click", loginUser);