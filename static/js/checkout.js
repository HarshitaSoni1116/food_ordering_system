/* =========================================
   FOODIE — CHECKOUT
========================================= */

document.addEventListener("DOMContentLoaded", function () {

    const paymentOptions =
        document.querySelectorAll(".payment-option");

    const placeOrderBtn =
        document.getElementById("placeOrderBtn");

    const checkoutForm =
        document.getElementById("checkoutForm");

    const successModal =
        document.getElementById("orderSuccess");


    /* Payment Selection */

    paymentOptions.forEach(option => {

        option.addEventListener("click", function () {

            paymentOptions.forEach(item => {
                item.classList.remove("active");
            });

            this.classList.add("active");

            const radio =
                this.querySelector("input[type='radio']");

            radio.checked = true;

        });

    });


    /* Place Order */

    placeOrderBtn.addEventListener("click", function () {

        if (!checkoutForm.checkValidity()) {

            checkoutForm.reportValidity();

            return;

        }

        window.location.href = "/order-confirmation/";
    });

});


/* Close Success */

function closeSuccess() {

    const successModal =
        document.getElementById("orderSuccess");

    successModal.classList.remove("show");

    window.location.href = "/";

}