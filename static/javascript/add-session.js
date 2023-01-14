// vars
const datalist = document.getElementById('customerList')
const addStudent = document.getElementById('addStudent')
const customerInput = document.getElementById('customerInput')
const form = document.getElementById('form')
const students = document.getElementById('session-students')
let users = []

customerInput.addEventListener('input',(e)=>{
  const value = e.target.value
  console.log(value)
})

console.log(customerInput.value)

const xhr = new XMLHttpRequest();

xhr.open('GET',"http://127.0.0.1:8000/get-data/");

xhr.responseType = 'json';

xhr.onload = function(){
  users = xhr.response.map(user =>{
    // console.log(user)
    let option = document.createElement('option')
    option.value = user.phone_nr
    option.textContent = `${user.name}`
    users.push(user)
    datalist.appendChild(option)
    return {name:user.name,phone:user.phone_nr,id:user.id}
  })
};

xhr.send();

// get user input and select customer
addStudent.addEventListener('click',()=>{
  let user = users.find(user => user.phone === customerInput.value)
  // create an element to the form with input set to customer id
    let label = document.createElement('label')
      label.setAttribute('for','student')
      label.innerText = user.name
  // create input element
    let input = document.createElement('input')
      input.setAttribute('value',user.id)
      input.setAttribute('name','students')
      input.textContent = user.name
      input.hidden = true
    // form.appendChild(input)
    students.appendChild(label)
    students.appendChild(input)
    customerInput.value = ''
})

// create an customer element


// edit set to false