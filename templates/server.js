document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const ratingDiv = document.querySelector("#rating");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        const fileInput = document.querySelector("input[type='file']");
        const file = fileInput.files[0];
        const formData = new FormData();
        formData.append("image", file);

        fetch("/upload", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            ratingDiv.textContent = `Rating: ${data.rating}`;
        })
        .catch(error => console.error(error));
    });
});
