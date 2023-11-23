// payment
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

paypal.Buttons({

    style: {
        color: 'gold',
        shape: 'rect',
        label: 'paypal',
        layout: 'vertical'
    },

    // Sets up the transaction when a payment button is clicked

    createOrder: (data, actions) => { 
        return actions.order.create({    
            purchase_units: [{    
                amount: {
                    currency_code: 'USD',
                    value: document.querySelector('#total-price')
                }    
            }]    
        });    
    },

    // Finalize the transaction after payer approval    
    onApprove: (data, actions) => {    
        // let url = "{% url 'manager:complete-payment' %}";
        // return fetch(url, {
        //     method: "POST",
        //     header: {
        //         'content-type': 'application/json',
        //         'X-CSRFToken': csrftoken
        //     },
        //     body: JSON.stringify({
        //         orderID: data.orderID,
        //         package_id: '1',
        //         subscription_duration: '{{subscription_duration}}'
        //     })
        // }).then(() => {
        //     location.href = "./index.html";
        // })
    }

}).render('#paypal-button-container');
