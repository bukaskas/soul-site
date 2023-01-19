


const xhr = new XMLHttpRequest();

xhr.open('GET',"https://soul-kitesurfing.up.railway.app/get-data/");

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

