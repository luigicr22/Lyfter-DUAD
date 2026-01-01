async function getApi (idUser){
    try{
        const response = await axios.get(`https://api.restful-api.dev/objects/${idUser}`);
        const userData = response.data;
        return userData;

    }catch (error) {
        throw error;
    };
};

async function postApi (data){
    try{
        const response = await axios.post("https://api.restful-api.dev/objects", data);
        const user = response.data;
        return user;
    }catch (error) {
        throw error;
    };
};

async function patchApi (){
    try{
        const dataApi = await getApi (sessionStorage.getItem("userId"));
        const data = {"data":{"email":dataApi.data.email,"password":dataApi.data.password,"categoryIdCounter" : Number(sessionStorage.getItem('categoryIdCounter')),
             "listCategories" : JSON.parse(sessionStorage.getItem('listCategories')), "taskIdCounter" : Number(sessionStorage.getItem('taskIdCounter')), "listTasks" : JSON.parse(sessionStorage.getItem('listTasks'))}};
        const response = await axios.patch(`https://api.restful-api.dev/objects/${dataApi.id}`, data);
        const updatedUser = response.data;
        return updatedUser;
    }catch (error) {
        throw error;
    };
};

function updateSessionStorage(userData){
    sessionStorage.setItem("userId", userData.id);
    sessionStorage.setItem("userName", userData.name);
    sessionStorage.setItem("userEmail", userData.data.email);
    sessionStorage.setItem("categoryIdCounter", String(userData.data.categoryIdCounter));
    sessionStorage.setItem("listCategories", JSON.stringify(userData.data.listCategories));
    sessionStorage.setItem("taskIdCounter", String(userData.data.taskIdCounter));
    sessionStorage.setItem("listTasks", JSON.stringify(userData.data.listTasks));
};

function isUserLoggedIn(){
    const isLoggedIn = sessionStorage.getItem("isLoggedIn");
    const userTimestamp = new Date (sessionStorage.getItem("userTimestamp"));
    const currentTime = new Date();
    const timeDifference = (currentTime - userTimestamp)/ (60 * 1000);

    if (isLoggedIn === "true" && timeDifference < 50){
        return true;
    }
    else{
        return false;
    };
};

function logoutUser(){
    sessionStorage.clear();
    window.location.href = "login.html";
};