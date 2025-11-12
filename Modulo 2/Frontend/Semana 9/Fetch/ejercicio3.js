async function getUsersData (idUser){
    try{
        const response = await fetch(`https://api.restful-api.dev/objects/${idUser}`);
        if (response.status === 404){
            throw `ID ${idUser} (Objeto no encontrado)`;
        };
        const user = await response.json();
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