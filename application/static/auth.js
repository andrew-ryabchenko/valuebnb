import { loginRequest, registerRequest } from "./auth_requests.js";

const inputEmail = document.getElementById('uname');
const inputPassword = document.getElementById('password');
const loginButton = document.getElementById('login');
const registerButton = document.getElementById('register');


loginButton.addEventListener('click', function (){
    const email = inputEmail.value;
    const passwd = inputPassword.value;
    if (!checkEmail(email)){
        alert('Invalid email')
        return null
    } 
    else if (!checkPassword(passwd)){
        alert('Password must be longer than 6 characters')
        return null
    } else {loginRequest(email, passwd)}

});

registerButton.addEventListener('click', function (){
    const email = inputEmail.value;
    const passwd = inputPassword.value;
    if (!checkEmail(email)){
        alert('Invalid email')
        return null
    }
    else if (!checkPassword(passwd)){
        alert('Password must be longer than 6 characters')
        return null
    } else {registerRequest(email, passwd)}
    

});

// REGEX EMAIL CHECK
function checkEmail(email){
    var regex = new RegExp("[a-zA-Z!#\$%&'\*\+\-/=\?\^_`\{\|\.]+@[a-zA-Z!#\$%&'\*\+\-/=\?\^_`\{\|\.]+\.[a-zA-Z]+")
    var matches = regex.exec(email)
    if (matches){
        if (matches[0]==email){return true}    
        
        else{return false}
    
    }else{return false}
} 

// PASSWORD VERIFICATION
function checkPassword(passwd){
    if (passwd.length<6) {return false}
    else{return true}
}

