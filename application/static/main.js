const logOutButton = document.getElementById('logOut');

// LOGOUT BUTTON CLICK EVENT HANDLER REMOVES `user_email` COOKIE AND REDIRECTS TO LOGIN PAGE
logOutButton.addEventListener('click', function (){
    document.cookie = "user_email=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    window.location.replace("/");
});
