var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i
var fileInput = document.getElementById('change-pic')
const form = document.getElementById('change-photo')

const picerror = document.getElementById('upload-error')

form.addEventListener('submit',(e)=>{

    var msg = []

    if(fileInput.value === '' || fileInput.value == null){
        msg.push('**please choose image for blog')
    }else if (!allowedExtensions.exec(fileInput.value)) {
        msg.push('Invalid file type');
        fileInput.value = '';
    }
    if(msg.length>0){
        e.preventDefault()
        picerror.innerText = msg
    }
})