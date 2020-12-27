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
    } else {logRegRequest('/login', email, passwd)}
    if (!checkPassword(passwd)){
        alert('Password must be longer than 6 characters')
        return null
    }

});

registerButton.addEventListener('click', function (){
    const email = inputEmail.value;
    const passwd = inputPassword.value;
    if (!checkEmail(email)){
        alert('Invalid email')
        return null
    }
    if (!checkPassword(passwd)){
        alert('Password must be longer than 6 characters')
        return null
    }
    

});

// ASYNC REQUEST WITH CREDENTIALS FOR DATABASE VERIFICATION

function logRegRequest(route, userEmail, password){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", route, true);
    xhr.responseType='document';
    xhr.setRequestHeader('user_email', userEmail);
    xhr.setRequestHeader('password', password);
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                var uemail = xhr.getResponseHeader('user_email');
                
                
                
            } else {
            
            }
        }
    }

    xhr.onerror = function (e) {
    console.error(xhr.statusText);
    };
    xhr.send(null);
};

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

