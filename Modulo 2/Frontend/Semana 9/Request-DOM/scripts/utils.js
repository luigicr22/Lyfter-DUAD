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

async function putApi (idUser, data){
    try{
        const response = await axios.put(`https://api.restful-api.dev/objects/${idUser}`, data);
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
    sessionStorage.setItem("userAddress", userData.data.address);
};

function isUserLoggedIn(){
    const isLoggedIn = sessionStorage.getItem("isLoggedIn");
    const userTimestamp = new Date (sessionStorage.getItem("userTimestamp"));
    const currentTime = new Date();
    const timeDifference = (currentTime - userTimestamp)/ (60 * 1000);

    if (isLoggedIn === "true" && timeDifference < 5){
        return true;
    }
    else{
        return false;
    };
};