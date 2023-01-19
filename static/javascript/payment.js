const cartTotal = document.getElementById('cart-total')
const splitPaymentElements = document.querySelectorAll('.split-payment')
const splitPaymentButton = document.getElementById('show-payments')
const oneTypePayment = document.getElementById('payment-type')
const totalAmt = document.getElementById('cart_total').textContent






const showSplitPaymentHandler = () => {
for(const payment of splitPaymentElements){
   payment.classList.toggle('open')
  }
  oneTypePayment.classList.toggle('hidden')
}

const visaPayment = () =>{
  const visaInput = document.getElementById('id_visa')
  visaInput.value = parseInt(totalAmt)
}

splitPaymentButton.addEventListener('click',showSplitPaymentHandler)



