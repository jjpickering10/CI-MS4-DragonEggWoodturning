const stripePublicKey = document.getElementById('id_stripe_public_key').textContent.slice(1, -1)
const clientSecret = document.getElementById('id_client_secret').textContent.slice(1, -1)

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

// Validate errors

card.addEventListener('change', function (e) {
    const errorDiv = document.getElementById('card-errors')
    if (e.error) {
        const html = `
            <span>
                <i class="fas fa-times"></i>
            </span>
            <span>
                ${e.error.message}
            </span>
        `
        errorDiv.innerHTML = html
    } else {
        errorDiv.textContent = ''
    }
})

// Handle form submission
var submitButton = document.getElementById('submit-button')
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
  ev.preventDefault();
  card.update({
      'disabled': true
  })
  submitButton.setAttribute('disabled', true)
  // If the client secret was rendered server-side as a data-secret attribute
  // on the <form> element, you can retrieve it here by calling `form.dataset.secret`
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
    }
  }).then(function(result) {
    const errorDiv = document.getElementById('card-errors')
    if (result.error) {
        const html = `
        <span>
            <i class="fas fa-times"></i>
        </span>
        <span>
            ${result.error.message}
        </span>
    `
        errorDiv.innerHTML = html
        card.update({
            'disabled': false
        })
        submitButton.removeAttribute('disabled')
    } else {
      // The payment has been processed!
      if (result.paymentIntent.status === 'succeeded') {
        // Show a success message to your customer
        // There's a risk of the customer closing the window before callback
        // execution. Set up a webhook or plugin to listen for the
        // payment_intent.succeeded event that handles any business critical
        // post-payment actions.
        form.submit()
      }
    }
  });
});