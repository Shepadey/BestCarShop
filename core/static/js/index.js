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
}).then(function(response) {
    let allItems=document.querySelectorAll('.item')
    allItems.forEach(item=>item.remove())

    let data = response.data

    for(let index in data){
        let div = document.createElement('div')
        let h4 = document.createElement('h4')
        let p = document.createElement('p')
        let h3 = document.createElement('h3')
        let img = document.createElement('img')

        img.setAttribute('src', data[index].image)

        div.classList.add('item')
        h4.innerText = data[index].name
        p.innerText = data[index].color
        h3.innerText = '${data[index].cost}'

        div.appendChild(img)
        div.appendChild(h4)
        div.appendChild(p)
        div.appendChild(h3)

        document.querySelector('.items').appendChild(div)
    }
})
})
