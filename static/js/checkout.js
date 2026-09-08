console.log("CHECKOUT JS LOADED!");

document.addEventListener("DOMContentLoaded", function () {

    console.log("CHECKOUT DOM LOADED!");

    const form = document.getElementById("checkoutForm");
    const cartData = document.getElementById("cartData");
    const placeOrderBtn = document.getElementById("placeOrderBtn");

    const checkoutItems = document.getElementById("checkoutItems");
    const checkoutItemCount = document.getElementById("checkoutItemCount");

    const checkoutSubtotal = document.getElementById("checkoutSubtotal");
    const checkoutDeliveryFee = document.getElementById("checkoutDeliveryFee");
    const checkoutDiscount = document.getElementById("checkoutDiscount");
    const checkoutTotal = document.getElementById("checkoutTotal");


    /* ================================
       SAFETY CHECK
    ================================= */

    if (!form || !checkoutItems || !checkoutSubtotal) {
        console.error("Checkout elements not found!");
        return;
    }


    /* ================================
       GET CART
    ================================= */

    function getCart() {

        const savedCart = localStorage.getItem("foodieCart");

        console.log("SAVED CART:", savedCart);

        if (!savedCart) {
            return [];
        }

        try {
            return JSON.parse(savedCart);
        } catch (error) {
            console.error("Cart JSON error:", error);
            return [];
        }
    }


    /* ================================
       DISPLAY CHECKOUT
    ================================= */

    function displayCheckout() {

        const cart = getCart();

        console.log("CART ON CHECKOUT:", cart);


        if (!Array.isArray(cart) || cart.length === 0) {

            checkoutItems.innerHTML = `
                <div class="empty-checkout">
                    <i class="bi bi-cart-x"></i>
                    <p>Your cart is empty.</p>
                </div>
            `;

            checkoutItemCount.textContent = "0 items";
            checkoutSubtotal.textContent = "₹0.00";
            checkoutDeliveryFee.textContent = "₹0.00";
            checkoutDiscount.textContent = "- ₹0.00";
            checkoutTotal.textContent = "₹0.00";

            if (placeOrderBtn) {
                placeOrderBtn.disabled = true;
            }

            return;
        }


        checkoutItems.innerHTML = "";

        let subtotal = 0;
        let quantityTotal = 0;


        /* ================================
           CART ITEMS
        ================================= */

        cart.forEach(function (item) {

            const price = Number(item.price) || 0;
            const quantity = Number(item.quantity) || 1;

            const itemTotal = price * quantity;

            subtotal += itemTotal;
            quantityTotal += quantity;


            const itemDiv = document.createElement("div");

            itemDiv.className = "summary-item";


            itemDiv.innerHTML = `
                <div class="item-image">

                    ${
                        item.image
                        ?
                        `<img src="${item.image}" alt="${item.name}">`
                        :
                        `
                        <div class="item-image-placeholder">
                            <i class="bi bi-image"></i>
                        </div>
                        `
                    }

                </div>

                <div class="item-details">

                    <h4>${item.name}</h4>

                    <span>Qty: ${quantity}</span>

                </div>

                <strong>
                    ₹${itemTotal.toFixed(2)}
                </strong>
            `;


            checkoutItems.appendChild(itemDiv);

        });


        /* ================================
           DELIVERY FEE
        ================================= */

        let deliveryFee = 0;

        if (subtotal > 0 && subtotal < 499) {
            deliveryFee = 40;
        }


        /* ================================
           DISCOUNT
        ================================= */

        const discount = 0;


        /* ================================
           TOTAL
        ================================= */

        const total =
            subtotal +
            deliveryFee -
            discount;


        /* ================================
           UPDATE SUMMARY
        ================================= */

        checkoutItemCount.textContent =
            quantityTotal +
            (quantityTotal === 1 ? " item" : " items");

        checkoutSubtotal.textContent =
            "₹" + subtotal.toFixed(2);

        checkoutDeliveryFee.textContent =
            "₹" + deliveryFee.toFixed(2);

        checkoutDiscount.textContent =
            "- ₹" + discount.toFixed(2);

        checkoutTotal.textContent =
            "₹" + total.toFixed(2);


        if (placeOrderBtn) {
            placeOrderBtn.disabled = false;
        }


        console.log("SUBTOTAL:", subtotal);
        console.log("DELIVERY FEE:", deliveryFee);
        console.log("TOTAL:", total);

    }


    /* ================================
       PAYMENT OPTIONS
    ================================= */

    const paymentOptions =
        document.querySelectorAll(".payment-option");


    paymentOptions.forEach(function (option) {

        option.addEventListener("click", function () {

            paymentOptions.forEach(function (item) {
                item.classList.remove("active");
            });

            this.classList.add("active");

            const radio =
                this.querySelector("input[type='radio']");

            if (radio) {
                radio.checked = true;
            }

        });

    });


    /* ================================
       PLACE ORDER
    ================================= */

    form.addEventListener("submit", function (event) {

        const cart = getCart();

        console.log("SUBMIT CART:", cart);


        if (!form.checkValidity()) {

            event.preventDefault();

            form.reportValidity();

            return;
        }


        if (!cart.length) {

            event.preventDefault();

            alert("Your cart is empty!");

            window.location.href = "/cart/";

            return;
        }


        cartData.value = JSON.stringify(cart);

        console.log(
            "CART DATA SENT TO DJANGO:",
            cartData.value
        );

    });


    /* ================================
       INITIAL LOAD
    ================================= */

    displayCheckout();

});


/* ================================
   CLOSE SUCCESS
================================ */

function closeSuccess() {

    const modal =
        document.getElementById("orderSuccess");

    if (modal) {
        modal.classList.remove("show");
    }

    window.location.href = "/";

}