/* =========================================
   FOODIE — MY ORDERS
========================================= */

document.addEventListener("DOMContentLoaded", function () {

    const tabs =
        document.querySelectorAll(".order-tab");

    const cards =
        document.querySelectorAll(".order-card");

    const searchInput =
        document.getElementById("orderSearch");

    const emptyState =
        document.getElementById("ordersEmpty");


    let currentFilter = "all";


    function filterOrders() {

        const search =
            searchInput.value.toLowerCase().trim();

        let visibleCount = 0;


        cards.forEach(card => {

            const status =
                card.dataset.status;

            const text =
                card.dataset.search.toLowerCase();

            const filterMatch =
                currentFilter === "all" ||
                (currentFilter === "active" &&
                 status === "active") ||
                (currentFilter === "delivered" &&
                 status === "delivered") ||
                (currentFilter === "cancelled" &&
                 status === "cancelled");

            const searchMatch =
                text.includes(search);


            if (filterMatch && searchMatch) {

                card.style.display = "block";
                visibleCount++;

            } else {

                card.style.display = "none";

            }

        });


        if (visibleCount === 0) {

            emptyState.classList.add("show");

        } else {

            emptyState.classList.remove("show");

        }

    }


    /* Filter Tabs */

    tabs.forEach(tab => {

        tab.addEventListener("click", function () {

            tabs.forEach(item => {
                item.classList.remove("active");
            });

            this.classList.add("active");

            currentFilter =
                this.dataset.filter;

            filterOrders();

        });

    });


    /* Search */

    searchInput.addEventListener(
        "input",
        filterOrders
    );


    /* Track Order */

    document
        .querySelectorAll(".track-btn")
        .forEach(button => {

            button.addEventListener("click", function () {

                alert(
                    "Your order is currently being prepared. 🚚"
                );

            });

        });


    /* Reorder */

    document
        .querySelectorAll(".reorder-btn")
        .forEach(button => {

            button.addEventListener("click", function () {

                this.innerHTML =
                    '<i class="bi bi-check-lg"></i> Added';

                setTimeout(() => {

                    this.innerHTML =
                        '<i class="bi bi-arrow-repeat"></i> Reorder';

                }, 1500);

            });

        });


    /* View Details */

    document
        .querySelectorAll(".details-btn")
        .forEach(button => {

            button.addEventListener("click", function () {

                alert(
                    "Order details will be available here."
                );

            });

        });


    filterOrders();

});