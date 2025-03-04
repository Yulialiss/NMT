document.addEventListener("DOMContentLoaded", function () {
    const loadingScreen = document.getElementById("loadingScreen");

    loadingScreen.style.display = "flex";

    setTimeout(() => {
        loadingScreen.style.display = "none";
    }, 3000);
});

function openPaymentForm(bankName) {
    localStorage.setItem("selectedBank", bankName);
    window.location.href = "payment.html";
}

