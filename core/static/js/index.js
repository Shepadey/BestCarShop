
function createHtmlItems(response) {
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
}
let btnFilter = document.getElementById('btn-filter')
let inputSearch = document.getElementById('searchWord')

btnFilter.addEventListener('click', function(event) {
    let fromInput = dcument.querySelector('.from')
    let toInput = document.querySelector('.to')
    event.preventDefault()

    axios.get('http://127.0.0.1:800/search-items/',{
        params:{
        from: fromInput.value,
        to: toInput.value
        }
    }).then(createHtmlItems(response))
})

inputSearch.addEventListener('input',function(event) {
    event.preventDefault()

    let inputValue = document.getElementById('searchWord').value
    console.log(inputValue)
    axios.get('http://127.0.0.1:800/search-item/',{
        params:{
            searchWord: inputValue
        }
    }).then(createHtmlItems(response))
})