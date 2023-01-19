
// Update the year under soul logo in the footer
const yearEl = document.querySelector('.year')
const currYear = new Date().getFullYear()
yearEl.textContent = currYear

// Open and close mobile navigation
const btnNav= document.querySelector('.btn--mobile-nav')

const header = document.querySelector('.header')

btnNav.addEventListener('click',function(){
  header.classList.toggle('nav-open')
})
///////////////////////////////////////////////////////////
// Fixing flexbox gap property missing in some Safari versions
function checkFlexGap() {
  var flex = document.createElement("div");
  flex.style.display = "flex";
  flex.style.flexDirection = "column";
  flex.style.rowGap = "1px";

  flex.appendChild(document.createElement("div"));
  flex.appendChild(document.createElement("div"));

  document.body.appendChild(flex);
  var isSupported = flex.scrollHeight === 1;
  flex.parentNode.removeChild(flex);


  if (!isSupported) document.body.classList.add("no-flexbox-gap");
}
checkFlexGap();

// Drop down button functionality

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
