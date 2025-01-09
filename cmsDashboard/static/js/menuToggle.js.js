document.addEventListener("DOMContentLoaded", function () {
    const headers = document.querySelectorAll("h1");

    headers.forEach((header) => {
        header.addEventListener("click", function () {
            const content = this.nextElementSibling;
            if (content) {
                content.classList.toggle("active");
            }
        });
    });
});
