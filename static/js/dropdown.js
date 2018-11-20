// Code from https://www.w3schools.com/howto/howto_js_dropdown.asp

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function showThemeSelect() {
    document.getElementById("themeDropdown-Content").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.themeButton')) {

    var dropdowns = document.getElementById("themedropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
