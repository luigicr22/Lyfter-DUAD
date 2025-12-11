let currentPage = 0;
let objectsApi = [];


async function getUsersData() {
    try {
        const response = await axios.get("https://api.restful-api.dev/objects");
        const objects = response.data;
        return objects;
    } catch (error) {
        console.log("Error: ", error);
    }
}

function objectsToPage (page, objects){
    const objectsToPage = objects.slice(page*5,(page*5)+5);
    const cardsContainer = document.getElementById("cards-container");
    cardsContainer.innerHTML = "";
    let newCards = "";

    for (const object of objectsToPage){
        let cardContainer = '<div class="card-container"><h3 id="card-product-name">'+object.name+'</h3><p><b>Id: </b>'+object.id+'</p>';
        if (object.data !== null){
            for (const key of Object.keys(object.data)){
                cardContainer += '<p><b>'+key+': </b>'+object.data[key]+'</p>';
            }
        }
        else{
            cardContainer += '<p>(Detalles no disponibles)</p>';
        };
        cardContainer += '</div>';
        newCards += cardContainer;
    };
    cardsContainer.innerHTML += newCards;
    
    const cards = document.getElementsByClassName("card-container");
    for (const card of cards) {
        requestAnimationFrame(() => {
            card.classList.add("show");
        });
    }

}

function nextPage () {
    if ((objectsApi.length-((currentPage+1)*5))>0){
        currentPage += 1;
        objectsToPage (currentPage, objectsApi)
    }
}

function previusPage() {
    if (currentPage > 0) {
        currentPage -= 1;
        objectsToPage(currentPage, objectsApi);
    }
}

getUsersData().then((response) => {objectsApi = response; objectsToPage(currentPage, objectsApi)});