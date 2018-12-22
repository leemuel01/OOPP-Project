current_tab = 0
//Get all the tabs
tab = document.getElementsByClassName("signuptab")

function showtab(n) {


    //closes tabs
    for (i = 0; i < tab.length; i++) {
        tab[i].style.display = "none"
    }


    //shows the tab
    tab[n].style.display = "block"
}

function nextPrev(a) {
    if (validate()) {
        current_tab = current_tab + a

        if (current_tab > tab.length) {
            current_tab = 0
        }
        else if (current_tab < 0) {
            current_tab = tab.length
        }

        showtab(current_tab)
    }
}

function Prevtab(a){
    current_tab = current_tab + a
    showtab(current_tab)
}

function validate() {
    inputs = tab[current_tab].getElementsByTagName("input")

    for (i = 0; i < inputs.length; i++) {
        if (inputs[i].value == "") {
            return false
        }
    }

    return true
}

showtab(current_tab)

//===================================================== Sign up and login ==========================================

signuptab = document.getElementById("modal_sign_up")
logintab = document.getElementById("modal_sign_in")

//Shows the signup page
function show_signup_or_login() {
    if (signuptab.style.display != "block") {
        signuptab.style.display = "block"
        logintab.style.display = "none"
    }
    else {
        signuptab.style.display = "none"
        logintab.style.display = "block"
    }

}


