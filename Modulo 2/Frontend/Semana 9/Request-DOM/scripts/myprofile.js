function fillProfile(){
    if (isUserLoggedIn()){
        document.getElementById('form-id').value = sessionStorage.getItem('userId');
        formName.value = sessionStorage.getItem('userName');
        formEmail.value = sessionStorage.getItem('userEmail');
        formAddress.value = sessionStorage.getItem('userAddress');
    }
    else{
        alert("Sesión expirada.");
        logoutUser();
    }
};

function editProfile(){
    formName.disabled = false;
    formEmail.disabled = false;
    formAddress.disabled = false;

    buttonLogout.disabled = true;
    buttonPassword.disabled = true;
    buttonEdit.disabled = true;
    buttonSave.disabled = false;
}

async function saveProfile(){
    if (!formName.value || !formEmail.value || !formAddress.value) {
        alert("Por favor, complete todos los campos del formulario.");
        return;
    }
    try{
        const dataApi = await getApi (sessionStorage.getItem("userId"));
        const data = {"name":formName.value,"data":{"email":formEmail.value,"password":dataApi.data.password,"address":formAddress.value}};
        const userData = await putApi(sessionStorage.getItem("userId"),data);
        alert("Usuario Actualizado.");
        updateSessionStorage(userData);
        fillProfile();
    }
    catch (error){
        console.log("Error: ",error);
        alert("Error al registrar el usuario. Intente nuevamente.");
        fillProfile();
    }
    finally{
        formName.disabled = true;
        formEmail.disabled = true;
        formAddress.disabled = true;
        
        buttonLogout.disabled = false;
        buttonPassword.disabled = false;
        buttonEdit.disabled = false;
        buttonSave.disabled = true;
    };
};

function logoutUser(){
    sessionStorage.clear();
    window.location.href = "login.html";
};

function changePassword(){
    window.location.href = "adminpassword.html";
};

const formName = document.getElementById('form-name');
const formEmail = document.getElementById('form-email');
const formAddress = document.getElementById('form-address');

const buttonEdit = document.getElementById('button-edit');
const buttonSave = document.getElementById('button-save');
const buttonPassword = document.getElementById('button-password');
const buttonLogout = document.getElementById('button-logout');

buttonEdit.addEventListener('click', editProfile);
buttonSave.addEventListener('click', saveProfile);
buttonPassword.addEventListener('click', changePassword);
buttonLogout.addEventListener('click', logoutUser);

fillProfile();