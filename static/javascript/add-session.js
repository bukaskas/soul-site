// vars
const datalist = document.getElementById('customerList')
const addStudent = document.getElementById('addStudent')
const customerInput = document.getElementById('customerInput')
const form = document.getElementById('form')
const students = document.getElementById('session-students')
const nrOfStudents= document.getElementById('nrOfStudents')

let users = []

let sStudents = []

let studNr = 0

const deleteStudentCardHandler = (id) => {
  cardIndex = 0
  for(const student in sStudents){
    if(student.id = id){
      break
    }
    cardIndex++
  }
  console.log(cardIndex)
  // after finding remove item from the array of cardIndex
  sStudents.splice(cardIndex, 1)
  students.children[cardIndex].remove()
}


const createStudentCard = (name, id) =>{
  const studentDiv= document.createElement('div')
  studentDiv.setAttribute('class','student-label')
  studentDiv.setAttribute('id',`${id}`)
  studentDiv.innerHTML = `
    <label for="${id}">${name}</label>
    <input name='students' type="text" hidden value='${id}'/>
    <i class='remove-button'><ion-icon name="close-outline"></ion-icon></i>
  `

  studentDiv.addEventListener('click',deleteStudentCardHandler)
  
  students.appendChild(studentDiv)
}

customerInput.addEventListener('input',(e)=>{
  const value = e.target.value

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

let removeHandler = (e) => { 
  console.log(e)
}


xhr.send();

// get user input and select customer
addStudent.addEventListener('click',()=>{
  let user = users.find(user => user.phone === customerInput.value)
  // create an element to the form with input set to customer id
    createStudentCard(user.name,user.id)
    sStudents.push(user)
    customerInput.value = ''
})








// create add session button, that will make the form appear

// cancel button would remove the button

// show TOTALS

// for each instructor
// total hours done this week
// total hours done this month 

// for school
// total hours done this week
// total hours done this month 