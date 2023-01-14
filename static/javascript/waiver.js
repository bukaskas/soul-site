
const waiverButton = document.getElementById('show-waiver')



waiverButton.addEventListener('click',() =>{
  let waiverContent = document.querySelector('.waiver-content')
  waiverContent.classList.toggle('waiver-open')

})