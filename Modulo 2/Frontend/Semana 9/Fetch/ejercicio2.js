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

userPost("Luis","mail@gmail.com","123456","Calle falsa 123, Costa Rica").then(idUser => console.log(`Id Usuario Creado: ${idUser}`));