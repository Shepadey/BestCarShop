let testButton = document.querySelector( selectors: '.testButton' )
const cards = document.querySelectorAll('.flipCard');
function flipCard(event){
    event.target.parentElement.classList.tooggle('flip');  
    

ards.forEach(card => card.addEventListener('click',flipCard));
}



testButton.addEventListener(type: 'click', listener: function (event:Event){
let url= 'http://127.0.0.1:8000/search-items';
axios.get(url).then(function(response){
    console.log(response);
    })
})
