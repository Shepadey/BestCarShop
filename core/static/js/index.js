let testButton = document.getElementById(  'testButton' )
console.log(testButton)

testButton.addEventListener('click',function (event){
    event.preventDefault()

let url= 'http://127.0.0.1:8000/search-items';
axios.get(url,{
    params:{
        'one':1,
        'two':2,
        'three':3,
    }
}).then(function(response){
    
    console.log(response);
    })
})
let inputSearch = document.getElementById( 'inputWord');
console.log(inputSearch)
inputSearch.addEventListener('input', function(event) {
    event.preventDefault()

    let inputValue = document.getElementById( 'search' ).value

    axios.get('http://127.0.0.1:800/search-item/',{
        params:{
        searchWord:inputValue
        }
    })
    .then(function(response) {
    console.log(response)
    })
}).then(function)