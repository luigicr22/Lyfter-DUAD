function promiseResource (resourceType, resourceName) {
    return new Promise(resolve => {
        setTimeout(() => resolve({type : resourceType, name :resourceName}), Math.floor(Math.random() * 1000));
    });
}

async function loadSite (){
    try{
        const images = await Promise.all ([promiseResource("Image","image1.jpg"),promiseResource("Image","image2.jpg")]);
        console.log(images);
        const script1 = await promiseResource("Script","script1.jpg");
        console.log(script1);
        const script2 = await promiseResource("Script","script2.jpg");
        console.log(script2);
    }
    catch (error){
        console.log('Error:',error);
    }
}

loadSite().finally(() => console.log("Site cargado"));

