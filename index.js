// your code goes here
const form = document.getElementById("contactForm");
const message = document.getElementById("formMessage");

form.addEventListener("submit", function(event) {
    event.preventDefault();

    message.textContent =
        "Thanks! Your message has been received.";

    form.reset();
});
