
// MAKES LOGIN REQUEST FOR USER VERIFICATION 
// PLANTS COOKIES IF LOGIN IS SUCCESSFUL
function loginRequest(userEmail, password){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", '/login', true);
    //xhr.responseType='document';
    xhr.setRequestHeader('user_email', userEmail);
    xhr.setRequestHeader('password', password);
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                if (xhr.getResponseHeader('user_status')=='found'){
                    var uemail = xhr.getResponseHeader('user_email');
                    document.cookie = `user_email = ${uemail}; expires = Thu, 01 Jan 2060 00:00:00 UTC; path = /;`
                    window.location.replace("/dashboard");}
                else{alert('User not found. Check login credentials.');}
            } 
        }
    }

    xhr.onerror = function (e) {
    console.error(xhr.statusText);
    };
    xhr.send(null);
};


// MAKES REQUEST TO REGISTER USER
// PLANTS COOKIES IF REGISTERATION IS SUCCESSFUL
function registerRequest(userEmail, password){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", '/register', true);
    //xhr.responseType='document';
    xhr.setRequestHeader('user_email', userEmail);
    xhr.setRequestHeader('password', password);
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                if (xhr.getResponseHeader('user_status')=='registered'){
                    var uemail = xhr.getResponseHeader('user_email');
                    document.cookie = `user_email = ${uemail}; expires = Thu, 01 Jan 2060 00:00:00 UTC; path = /;`
                    window.location.replace("/dashboard");}
                else{alert(`User ${userEmail} already exists`);}
            } 
        }
    }

    xhr.onerror = function (e) {
    console.error(xhr.statusText);
    };
    xhr.send(null);
};

export {registerRequest, loginRequest};