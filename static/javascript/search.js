

const searchInput = document.querySelector("[data-search]")

let users = []

searchInput.addEventListener("input",(e) => {
  const value = e.target.value.toLowerCase()
  users.forEach(user =>{
    console.log(user)
    const isVisible = user.name.toLowerCase().includes(value) || user.phone.toString().includes(value)
    user.element.classList.toggle('hide',!isVisible)
  })
})





const userCardTemplate = document.querySelector('[data-user-template]')
const listElement = document.querySelector('.customers')
const customerTemplate = document.getElementById('customer')
const userCardContainer = document.querySelector('[data-user-cards-container]')


const xhr = new XMLHttpRequest();

xhr.open('GET',"http://127.0.0.1:8000/get-data/");

xhr.responseType = 'json';

xhr.onload = function(){
  users = xhr.response.map(user =>{
    const card = userCardTemplate.content.cloneNode(true).children[0]
    console.log(user)
    const name = card.querySelector("[data-name]")
    const phone_nr =card.querySelector("[data-phone]")
    const email = card.querySelector('[data-email]')
    name.textContent = user.name
    phone_nr.textContent = user.phone_nr
    if(user.email !== null){
      email.textContent = user.email
    }else{
      email.textContent = "N/A"
    }
    userCardContainer.append(card)
    return {name:user.name,phone:user.phone_nr, email:user.email ,element:card}
  })
};

xhr.send();

