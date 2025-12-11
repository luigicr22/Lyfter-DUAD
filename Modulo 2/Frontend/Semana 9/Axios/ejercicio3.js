//Se instalo axios en la raiz del proyecto "npm install axios"
//Se importa usando CommonJS
const axios = require('axios'); 

async function getUsersData (idUser){
    try{
        const response = await axios.get(`https://api.restful-api.dev/objects/${idUser}`);
        const user = response.data;
        if (user.data !== null){
            console.log (`\n${user.name}:`);
            for (const key of Object.keys(user.data)){
                console.log (`\t${key}: ${user.data[key]}`);
            }
        }
        else{
            console.log (`${user.name} (Detalles no disponibles)`);
        };
    }
    catch (error){
        console.log (`Error: ${error}`);
    };
};

getUsersData(1);
getUsersData(45);