

//CREATE BINDING FOR ELEMENTS
const logOutButton = document.getElementById('logOut');
const streetName = document.getElementById('streetName');
const streetNumber = document.getElementById('streetNumber');
const zipcode = document.getElementById('zip');
const estimateButton = document.getElementById('estimateButton');
const propertyType = document.getElementById('property_type');
const accomodates = document.getElementById('accomodates');
const bathrooms = document.getElementById('bathrooms');
const bedrooms = document.getElementById('bedrooms');
const beds = document.getElementById('beds');

// LOGOUT BUTTON CLICK EVENT HANDLER REMOVES `user_email` COOKIE AND REDIRECTS TO LOGIN PAGE
logOutButton.addEventListener('click', function (){
    document.cookie = "email_hash=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    document.cookie = "email=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    window.location.replace("/");
});

// ESTIMATE BUTTON CLICK EVENT HANDLER SENDS URL EMBEDDED DATA TO THE SERVER 
estimateButton.addEventListener('click', function (){
    
    var query = `/estimate/streetname=${streetName.value}&streetnum=${streetNumber.value}&zip=${zipcode.value}&ptype=${propertyType.value}&accom=${accomodates.value}&numbathrms=${bathrooms.value}&numbedrms=${bedrooms.value}&numbeds=${beds.value}&`;
    sendDataRequest(query);
});

// RETREIVES COOCKIE WITH GIVEN NAME

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return null;
  }



function sendDataRequest(query){
    var xhr = new XMLHttpRequest();
    xhr.open("GET", query, true);
    var userEmail = getCookie('email');
    var email_hash = getCookie('email_hash');
    xhr.setRequestHeader('user_email', userEmail);
    xhr.setRequestHeader('email_hash', email_hash);
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log('success');
            } 
        }
    }
    xhr.onerror = function (e) {
    console.error(xhr.statusText);
    };
    xhr.send(null);
};

