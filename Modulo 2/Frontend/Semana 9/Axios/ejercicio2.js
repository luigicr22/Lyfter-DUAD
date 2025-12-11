//Se instalo axios en la raiz del proyecto "npm install axios"
//Se importa usando CommonJS
const axios = require('axios'); 

async function userPost (name, email, password, address){
    try{
        const data = {"name":name,"data":{"email":email,"password":password,"address":address}};
        const response = await axios.post("https://api.restful-api.dev/objects", data);
        const user = response.data;
        return user.id;
    }
    catch (error){
        console.log("Error: ",error);
    };
};

userPost("Luis","mail@gmail.com","123456","Calle falsa 123, Costa Rica").then(idUser => console.log(`Id Usuario Creado: ${idUser}`));