function toggleMenu(menuId) {
    const menus = [
        document.getElementById("anaSayfaMenu"),
        document.getElementById("galleryMenu"),
        document.getElementById("anaSayfaPersonelMenu"),
        document.getElementById("hakkimizdaMenu"),
        document.getElementById("referansMenu"),
        document.getElementById("servisMenu"),
        document.getElementById("contactMenu"),
        document.getElementById("mediaMenu"),
    ];
    const overlay = document.getElementById("overlay");

    // Tüm menüleri kapat
    menus.forEach(menu => {
        if (menu.id !== menuId) {
            menu.style.transform = "translateY(-20px)";
            menu.style.opacity = "0";
            setTimeout(() => {
                menu.style.display = "none";
            }, 500);
        }
    });

    // Tıklanan menüyü aç/kapat
    const menu = document.getElementById(menuId);
    if (menu.style.display === "none" || menu.style.display === "") {
        menu.style.display = "block"; // Menü görünür hale gelir
        overlay.style.display = "block"; // Karartma görünür hale gelir
        setTimeout(() => {
            menu.style.transform = "translateY(0)";
            menu.style.opacity = "1";
        }, 10);
    } else {
        menu.style.transform = "translateY(-20px)";
        menu.style.opacity = "0";
        setTimeout(() => {
            menu.style.display = "none";
            overlay.style.display = "none";
        }, 500);
    }
}

// Karartma alanına tıklanarak tüm menüleri kapatmak için
document.getElementById("overlay").addEventListener("click", function () {
    const menus = [
        document.getElementById("anaSayfaMenu"),
        document.getElementById("galleryMenu"),
        document.getElementById("anaSayfaPersonelMenu"),
        document.getElementById("hakkimizdaMenu"),
        document.getElementById("referansMenu"),
        document.getElementById("servisMenu"),
        document.getElementById("contactMenu"),
        document.getElementById("mediaMenu"),
    ];
    const overlay = document.getElementById("overlay");

    menus.forEach(menu => {
        menu.style.transform = "translateY(-20px)";
        menu.style.opacity = "0";
        setTimeout(() => {
            menu.style.display = "none";
        }, 500);
    });

    overlay.style.display = "none";
});
