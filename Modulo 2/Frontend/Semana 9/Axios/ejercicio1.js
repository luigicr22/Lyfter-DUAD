//Se instalo axios en la raiz del proyecto "npm install axios"
//Se importa usando CommonJS
const axios = require('axios'); 

async function getUsersData (){
    try{
        const response = await axios.get("https://api.restful-api.dev/objects");
        const users = response.data;
        for (const user of users){
            if (user.data !== null){
                console.log (`\n${user.name}:`);
                for (const key of Object.keys(user.data)){
                    console.log (`\t${key}: ${user.data[key]}`);
                }
            };
        };
    }
    catch (error){
        console.log ("Error: ",error);
    };
};

getUsersData();