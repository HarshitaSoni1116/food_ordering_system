/* =========================================
   FOODIE — PROFILE
========================================= */

document.addEventListener("DOMContentLoaded", function () {

    const editBtn =
        document.getElementById("editProfileBtn");

    const modal =
        document.getElementById("profileModal");

    const closeBtn =
        document.getElementById("modalClose");

    const saveBtn =
        document.getElementById("saveProfileBtn");

    const logoutBtn =
        document.getElementById("logoutBtn");


    /* Open Modal */

    editBtn.addEventListener("click", function () {

        modal.classList.add("show");

    });


    /* Close Modal */

    closeBtn.addEventListener("click", function () {

        modal.classList.remove("show");

    });


    /* Click Outside */

    modal.addEventListener("click", function (event) {

        if (event.target === modal) {

            modal.classList.remove("show");

        }

    });


    /* Save Profile */

    saveBtn.addEventListener("click", function () {

        const name =
            document.getElementById("editName").value.trim();

        if (!name) {

            alert("Please enter your name.");

            return;

        }

        document.querySelector(
            ".profile-main-info h1"
        ).textContent = name;

        document.querySelector(
            ".info-item strong"
        ).textContent = name;

        modal.classList.remove("show");

        alert("Profile updated successfully!");

    });


    /* Logout */

    logoutBtn.addEventListener("click", function () {

        const confirmLogout =
            confirm("Are you sure you want to logout?");

        if (confirmLogout) {

            window.location.href = "/login/";

        }

    });

});