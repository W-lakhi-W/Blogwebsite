let blogheading = document.getElementById('blogheading')
let blogpic = document.getElementById('blogpic')
let blog = document.getElementById('blog')
var fileInput = document.getElementById('blogpic');

// Allowing file type
var allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
const form = document.getElementById('upload-form')

const headingerro = document.getElementById('heading_error')
const picerror = document.getElementById('pic_error')
const blogerror = document.getElementById('blog_error')
form.addEventListener('submit',(e)=>{
    var blogheadmsg = []
    var blogpicmsg = []
    var blogmsg = []
    if(blogheading.value == '' || blogheading.value == null){
        blogheadmsg.push('**please enter blog heading')
    }else if(blogheading.length < 10){
        blogheadmsg.push('**please enter 10 charachter minimum')
    }if(blogpic.value === '' || blogpic.value == null){
        blogpicmsg.push('**please choose image for blog')
    }else if (!allowedExtensions.exec(blogpic.value)) {
        blogpicmsg.push('Invalid file type');
        fileInput.value = '';
    }if(blog.value.length<500 || blog.value==null){
        blogmsg.push('**please enter 150 words minimum')
    }


    if(blogheadmsg.length>0 || blogpicmsg.length >0 || blogmsg.length>0){
        e.preventDefault()
        headingerro.innerText= blogheadmsg
        picerror.innerText = blogpicmsg
        blogerror.innerText= blogmsg
    }
})