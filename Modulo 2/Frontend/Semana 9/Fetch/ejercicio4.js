async function userPost (name, email, password, address){
    try{
        const data = {"name":name,"data":{"email":email,"password":password,"address":address}};
        const requestOptions = {
            method:"POST",
            headers:{
                "Content-Type":"application/json",
            },
            body:JSON.stringify(data),
        }
        const response = await fetch("https://api.restful-api.dev/objects", requestOptions);
        const user = await response.json();
        
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
        const requestOptions = {
            method:"PATCH",
            headers:{
                "Content-Type":"application/json",
            },
            body:JSON.stringify(data),
        }
        const response = await fetch(`https://api.restful-api.dev/objects/${idUser}`, requestOptions);
        const user = await response.json();
        return user;
    }
    catch (error){
        console.log("Error: ",error);
    };
};

async function getUsersData (idUser){
    try{
        const response = await fetch(`https://api.restful-api.dev/objects/${idUser}`);
        if (response.status === 404){
            throw `ID ${idUser} (Objeto no encontrado)`;
        };
        const user = await response.json();
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