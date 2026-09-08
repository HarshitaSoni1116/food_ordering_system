/* =========================================
   FOODIE — PROFILE
========================================= */

document.addEventListener("DOMContentLoaded", function () {

    /* =========================
       EDIT PROFILE MODAL
    ========================= */

    const editBtn =
        document.getElementById("editProfileBtn");

    const profileModal =
        document.getElementById("profileModal");

    const closeProfileModal =
        document.getElementById("modalClose");


    if (editBtn && profileModal) {

        editBtn.addEventListener("click", function () {

            profileModal.classList.add("show");

        });

    }


    if (closeProfileModal && profileModal) {

        closeProfileModal.addEventListener("click", function () {

            profileModal.classList.remove("show");

        });

    }


    if (profileModal) {

        profileModal.addEventListener("click", function (event) {

            if (event.target === profileModal) {

                profileModal.classList.remove("show");

            }

        });

    }


    /* =========================
       ADD ADDRESS MODAL
    ========================= */

    const addAddressBtns =
        document.querySelectorAll("#addAddressBtn");

    const addressModal =
        document.getElementById("addressModal");

    const closeAddressModal =
        document.getElementById("closeAddressModal");


    /* Open Add Address Modal */

    addAddressBtns.forEach(function (button) {

        button.addEventListener("click", function () {

            addressModal.classList.add("show");

        });

    });


    /* Close Add Address Modal */

    if (closeAddressModal && addressModal) {

        closeAddressModal.addEventListener("click", function () {

            addressModal.classList.remove("show");

        });

    }


    /* Click Outside Address Modal */

    if (addressModal) {

        addressModal.addEventListener("click", function (event) {

            if (event.target === addressModal) {

                addressModal.classList.remove("show");

            }

        });

    }


    /* =========================
       LOGOUT
    ========================= */

    const logoutBtn =
        document.getElementById("logoutBtn");


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