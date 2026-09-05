document.addEventListener("DOMContentLoaded", () => {

    const sidebar = document.querySelector(".admin-sidebar");
    const menuBtn = document.getElementById("adminMenuBtn");

    if (menuBtn && sidebar) {
        menuBtn.addEventListener("click", () => {
            sidebar.classList.toggle("show");
        });
    }

    document.querySelectorAll(".admin-actions button").forEach(button => {
        button.addEventListener("click", () => {
            alert("This feature will be connected to the Django backend.");
        });
    });

    const notification = document.querySelector(".admin-notification");

    if (notification) {
        notification.addEventListener("click", () => {
            alert("You have 8 new admin notifications.");
        });
    }

});