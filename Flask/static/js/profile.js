//Navsssssssss
remindernav = document.getElementById("remindernav")
medicalhistorynav = document.getElementById("medicalhistorynav")
userinfonav = document.getElementById("userinfonav")

navs = [remindernav, medicalhistorynav, userinfonav]

//Content
reminders = document.getElementById("reminders")
medical_history = document.getElementById("medicalhistory")
updateuserinfo = document.getElementById("updateuserinfo")

content = [reminders, medical_history, updateuserinfo]

function clickmedhist(n) {
    for(i = 0; i < navs.length; i++){
        navs[i].className = "nav-link"
        content[i].style.display = "none"
    }
    navs[n].className = "nav-link active"
    content[n].style.display = "block"
    content[n].className = "row justify-content-center"

}