async function getUsersData (){
    try{
        const response = await fetch("https://api.restful-api.dev/objects");
        const users = await response.json();
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