const email = document.getElementById('email')
const password = document.getElementById('password')
const form = document.getElementById('form')
const errorElement = document.getElementById('error1')
const errorElement2 = document.getElementById('error2')
var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

form.addEventListener('submit',(e)=>{
    let message1 = []
    let message2 = []
    if (email.value==='' || email.value == null){
        message1.push('**Please enter email address')

    }else if(!email.value.match(mailformat)){
        message1.push("**invalid email address!");
    }if(password.value==='' || password.value==null){
        message2.push('**please enter password')
    }else if(password.value.length <6){
        message2.push('**please enter 6 charachter password minimum')
    }
    if (message1.length>0 || message2.length>0){
        e.preventDefault()
        errorElement.innerText = message1
        errorElement2.innerText=message2
    }
})