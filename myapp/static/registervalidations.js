const form = document.getElementById('register-form')
const first_name = document.getElementById('first_name')
const last_name = document.getElementById('last_name')
const username = document.getElementById('username')
const email = document.getElementById('email')
const password1 = document.getElementById('password1')
const password2 = document.getElementById('password2')
var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;


const first_name_error = document.getElementById('first_name_error')
const last_name_error = document.getElementById('last_name_error')
const username_error = document.getElementById('username_error')
const email_error = document.getElementById('email_error')
const password1_error = document.getElementById('password1_error')
const password2_error = document.getElementById('password2_error')


form.addEventListener('submit',(e)=>{
    const msg_first_name = []
    const msg_last_name = []
    const msg_username = []
    const msg_email = []
    const msg_password1 = []
    const msg_password2 = []
    if(first_name.value === '' || first_name.value == null){
        msg_first_name.push('**please enter your first name')
    }if(last_name.value === '' || last_name.value == null){
        msg_last_name.push('**please enter your last name')
    }if(username.value === '' || username.value == null){
        msg_username.push('**please enter username')
    }else if(username.value.length<6){
        msg_username.push('**minimum 6 characters required')
    }
    if (email.value==='' || email.value == null){
        msg_email.push('**please enter email address')

    }else if(!email.value.match(mailformat)){
        msg_email.push("**invalid email address!");
    }if(password1.value === '' || password1.value == null){

            msg_password1.push('**please enter your password')
        
    }else if(password1.value.length<6 || password2.value.length<6){
            if(password1.value.length<6){
                msg_password1.push('minimum 6 charachter required')
            }
    }if(password2.value == '' || password2.value== null){
       
        if(password1.value.length>=6){
            msg_password2.push('**please enter your password again')
        }else{
            msg_password2.push('**please enter your password')
        }
    }else if(password2.value.length<6){
        msg_password2.push('**minimum 6 charachters required')
    }
    if (password1.value !== password2.value && msg_password1.length == 0 && msg_password2.length == 0){
        msg_password2.push("passwords are not matching")
    }
    if(msg_first_name.length>0){
        e.preventDefault()
        first_name_error.innerText = msg_first_name
        last_name_error.innerText = msg_last_name
        username_error.innerText = msg_username
        email_error.innerText = msg_email
        password1_error.innerText = msg_password1
        password2_error.innerText = msg_password2
    }
})