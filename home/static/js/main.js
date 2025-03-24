document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault();
    let email = document.querySelector("input[type='email']").value;

    fetch("/subscribe/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({ email: email })
    })
    .then(response => response.json())
    .then(data => alert(data.message || data.error))
    .catch(error => console.error("Error:", error));
});
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
      document.getElementById("toggleReviews").addEventListener("click", function() {
        var reviewsContainer = document.getElementById("reviewsContainer");
        var icon = document.getElementById("toggleReviews");

        if (reviewsContainer.style.display === "none") {
          reviewsContainer.style.display = "block";
          icon.classList.add("open");
        } else {
          reviewsContainer.style.display = "none";
          icon.classList.remove("open");
        }
      });


