function toggleSidebar() {
    var sidebar = document.getElementById("mySidebar");
    var mainContent = document.querySelector(".main-content");

    if (sidebar.classList.contains("hidden")) {
        sidebar.classList.remove("hidden");
        mainContent.style.marginLeft = "200px";
    } else {
        sidebar.classList.add("hidden");
        mainContent.style.marginLeft = "0";
    }
}
