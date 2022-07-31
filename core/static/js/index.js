//let testButton = document.querySelector( selectors: '.testButton' )
console.log("hello");
const cards = document.querySelectorAll('.flipCard');
console.log("hello");
function flipCard(){
    event.target.parentElement.classList.tooggle('flip');  
}

cards.forEach(card => card.addEventListener('click',flipCard));


/*
testButton.addEventListener(type: 'click', listener: function (event:Event){
let url= 'http://127.0.0.1:8000/search-items';
axios.get(url).then(function(response){
    console.log(response);
    })
})*/
