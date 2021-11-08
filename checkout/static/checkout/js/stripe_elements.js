const stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1)
const clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1)

console.log(stripePublicKey);
console.log(clientSecret);

const stripe = Stripe(stripePublicKey)
const elements = stripe.elements()
const card = elements.create('card', {
    style: {
      base: {
        iconColor: '#000',
        color: '#000',
        fontWeight: '500',
        fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        ':-webkit-autofill': {
          color: '#fce883',
        },
        '::placeholder': {
          color: '#87BBFD',
        },
      },
      invalid: {
        iconColor: '#FFC7EE',
        color: '#FFC7EE',
      },
    },
  })
card.mount('#card-element')