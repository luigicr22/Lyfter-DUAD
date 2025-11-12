//Se instalo axios en la raiz del proyecto "npm install axios"
//Se importa usando CommonJS
const axios = require('axios'); 

const axiosInstance = axios.create({baseURL: "https://api.restful-api.dev/objects"});

async function userPost (name, email, password, address){
    try{
        const data = {"name":name,"data":{"email":email,"password":password,"address":address}};
        const response = await axiosInstance.post("",data);
        const user = response.data;
        return user.id;
    }
    catch (error){
        console.log("Error: ",error);
    };
};

async function userAddressUpdate (idUser, newAddress){
    try{
        const userData = await getUsersData (idUser);
        const data = {"data":{"email":userData.data.email,"password":userData.data.password,"address":newAddress}};
        const response = await axiosInstance.patch(`/${idUser}`, data);
        const user = response.data;
        return user;
    }
    catch (error){
        console.log("Error: ",error);
    };
};

async function getUsersData (idUser){
    try{
        const response = await axiosInstance.get(`/${idUser}`);
        const user = response.data;
        return user;
    }
    catch (error){
        console.log (`Error: ${error}`);
    };
};

userPost("Luis","mail@gmail.com","123456","Calle falsa 123, Costa Rica")
    .then(id => {
        console.log(`Id Usuario Creado: ${id}`);
        return userAddressUpdate(id, "Calle falsa 123, Springfield");
    })
    .then(user => {
        console.log(`Usuario actualizado: ${JSON.stringify(user)}`);
    });