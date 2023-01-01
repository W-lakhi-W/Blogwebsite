data = document.getElementById('search-data')

form = document.getElementById('search-form')
console.log(form)
form.addEventListener('submit',(e)=>{
    if(data.value.length==0 || data.value == null){
        e.preventDefault()
    }
})