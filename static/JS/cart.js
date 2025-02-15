// var updateBtns = document.getElementsByClassName('update-cart');

// for (var i = 0; i < updateBtns.length; i++) {
//     updateBtns[i].addEventListener('click', function() {
//         var productId = this.dataset.product;
//         var action = this.dataset.action;
//         console.log('productId:', productId, 'action:', action);
//     });
// }

 



document.addEventListener('DOMContentLoaded', function() {
    var updateBtns = document.getElementsByClassName('update-cart');

    if (updateBtns.length === 0) {
        console.log('No update-cart buttons found.');
    } else {
        for (var i = 0; i < updateBtns.length; i++) {
            updateBtns[i].addEventListener('click', function() {
                var productId = this.dataset.product;
                var action = this.dataset.action;
                console.log('productId:', productId, 'action:', action);

                console.log('USER:', user)
                if(user === 'AnonymousUser')
                    {
                    console.log(' User is Not login')
                    }
                else
                {
                    updateUserOrder(productId, action)
                }    
            });

        }
    }
});


function updateUserOrder(productId, action)
{
    console.log('User is login, sending data..')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action':action})
    })

    .then((Response) =>{
        return Response.json()
    })

    .then((data)=>{
        console.log('data:', data)
        location.reload()
    })
}
