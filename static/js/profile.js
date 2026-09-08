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

    const logoutBtn =
        document.getElementById("logoutBtn");


    /* =========================
       OPEN MODAL
    ========================= */

    if (editBtn && modal) {

        editBtn.addEventListener("click", function () {

            modal.classList.add("show");

        });

    }


    /* =========================
       CLOSE MODAL
    ========================= */

    if (closeBtn && modal) {

        closeBtn.addEventListener("click", function () {

            modal.classList.remove("show");

        });

    }


    /* =========================
       CLICK OUTSIDE MODAL
    ========================= */

    if (modal) {

        modal.addEventListener("click", function (event) {

            if (event.target === modal) {

                modal.classList.remove("show");

            }

        });

    }


    /* =========================
       LOGOUT
    ========================= */

    if (logoutBtn) {

        logoutBtn.addEventListener("click", function () {

            const confirmLogout =
                confirm("Are you sure you want to logout?");

            if (confirmLogout) {

                window.location.href = "/logout/";

            }

        });

    }

});