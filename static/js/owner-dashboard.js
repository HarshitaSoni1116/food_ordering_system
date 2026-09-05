/* =========================================
   FOODIE - OWNER DASHBOARD
========================================= */

document.addEventListener("DOMContentLoaded", () => {

    const sidebar = document.querySelector(".owner-sidebar");
    const toggle = document.getElementById("sidebarToggle");

    if (toggle && sidebar) {
        toggle.addEventListener("click", () => {
            sidebar.classList.toggle("show");
        });
    }


    // Quick action buttons
    document.querySelectorAll(".quick-actions button").forEach(button => {

        button.addEventListener("click", () => {

            const action = button.querySelector("span")?.textContent;

            if (action) {
                alert(`${action} will be available after backend integration.`);
            }

        });

    });


    // Notification
    const notificationBtn = document.querySelector(".notification-btn");

    if (notificationBtn) {

        notificationBtn.addEventListener("click", () => {
            alert("You have 5 new notifications.");
        });

    }


    // Manage restaurant
    const manageBtn = document.querySelector(".manage-btn");

    if (manageBtn) {

        manageBtn.addEventListener("click", () => {
            alert("Restaurant management will be connected to the backend later.");
        });

    }

});