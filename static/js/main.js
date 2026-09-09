/* =========================================
   FOODIE - GLOBAL JAVASCRIPT
========================================= */

document.addEventListener("DOMContentLoaded", () => {

    console.log("Foodie frontend loaded successfully!");

    /* =====================================
       LOADER
    ===================================== */

    const loader = document.getElementById("foodieLoader");

    if (loader) {
        setTimeout(() => {
            loader.classList.add("hidden");
        }, 500);
    }


    /* =====================================
       SCROLL TO TOP
    ===================================== */

    const scrollTopBtn = document.getElementById("scrollTopBtn");

    if (scrollTopBtn) {

        window.addEventListener("scroll", () => {

            if (window.scrollY > 400) {
                scrollTopBtn.classList.add("show");
            } else {
                scrollTopBtn.classList.remove("show");
            }

        });

        scrollTopBtn.addEventListener("click", () => {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });

    }


    /* =====================================
       ACTIVE NAVBAR
    ===================================== */

    const currentPath = window.location.pathname;

    document.querySelectorAll(".navbar .nav-link").forEach(link => {

        const href = link.getAttribute("href");

        if (
            href &&
            href !== "/" &&
            currentPath.startsWith(href)
        ) {
            link.classList.add("active");
        }

    });


    /* =====================================
       CART COUNT
    ===================================== */

    updateCartCount();

});


/* =========================================
   TOAST
========================================= */

function showToast(message, type = "success") {

    const container = document.getElementById("toastContainer");

    if (!container) return;

    const toast = document.createElement("div");

    let icon = "bi-check-circle-fill";

    if (type === "error") {
        icon = "bi-exclamation-circle-fill";
    }

    if (type === "warning") {
        icon = "bi-exclamation-triangle-fill";
    }

    toast.className = "foodie-toast";

    toast.innerHTML = `
        <i class="bi ${icon}"></i>
        <span>${message}</span>
    `;

    container.appendChild(toast);

    setTimeout(() => {
        toast.classList.add("hide");

        setTimeout(() => {
            toast.remove();
        }, 300);

    }, 2500);
}


/* =========================================
   CART COUNT
========================================= */

function updateCartCount() {

    const cartCount = document.querySelector(".cart-count");

    if (!cartCount) return;

    const savedCart = JSON.parse(
        localStorage.getItem("foodieCart") || "[]"
    );

    let totalItems = 0;

    savedCart.forEach(item => {
        totalItems += Number(item.quantity || 1);
    });

    cartCount.textContent = totalItems;
}
function toggleUserMenu() {
    const dropdown = document.getElementById("userDropdown");

    if (dropdown) {
        dropdown.classList.toggle("show");
    }
}


// Close dropdown when clicking outside
document.addEventListener("click", function (event) {

    const userMenu = document.querySelector(".user-menu");
    const dropdown = document.getElementById("userDropdown");

    if (
        dropdown &&
        userMenu &&
        !userMenu.contains(event.target)
    ) {
        dropdown.classList.remove("show");
    }

});

document.addEventListener("DOMContentLoaded", function () {

    const addButtons = document.querySelectorAll(".add-food-btn");

    addButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const foodId = this.dataset.foodId;
            const foodName = this.dataset.foodName;
            const foodPrice = parseFloat(this.dataset.foodPrice);
            const foodImage = this.dataset.foodImage;
            const restaurant = this.dataset.restaurant;

            let cart = JSON.parse(localStorage.getItem("foodieCart")) || [];

            const existingItem = cart.find(
                item => String(item.id) === String(foodId)
            );

            if (existingItem) {
                existingItem.quantity += 1;
            } else {
                cart.push({
                    id: foodId,
                    name: foodName,
                    price: foodPrice,
                    image: foodImage,
                    restaurant: restaurant,
                    quantity: 1
                });
            }

            localStorage.setItem("foodieCart", JSON.stringify(cart));

            // Update navbar cart count
            if (typeof updateCartCount === "function") {
                updateCartCount();
            }

            // Button feedback
            const originalHTML = this.innerHTML;

            this.innerHTML = '<i class="bi bi-check-lg"></i> Added';
            this.classList.add("added");

            setTimeout(() => {
                this.innerHTML = originalHTML;
                this.classList.remove("added");
            }, 1200);
        });

    });

});