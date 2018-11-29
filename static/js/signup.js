current_tab = 0

function showtab(n){
    //Get all the tabs
    tab = document.getElementsByClassName("signuptab")

    for(i = 0; i < tab.length; i++){
        tab[i].style.display = "none"
    }

    //shows the tab
    tab[n].style.display = "block"
}

function nextPrev(n) {
    tab = document.getElementsByClassName("signuptab")

    tabnum = current_tab + n
    showtab(tabnum)
    
  }

//Shows the signup page
function showsignup(){
    signuptab = document.getElementById("modal_sign_up")
    logintab = document.getElementById("modal_sign_in")

    signuptab.style.display = "block"
    logintab.style.display = "none"

}

showtab(current_tab)