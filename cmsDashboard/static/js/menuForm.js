function toggleMenu() {
    const menu = document.getElementById("galleryMenu");
    const overlay = document.getElementById("overlay");
    
    // Eğer menü gizli ise, menüyü göster ve arka planı karart
    if (menu.style.display === "none" || menu.style.display === "") {
        menu.style.display = "block"; // Menü görünür hale gelir
        overlay.style.display = "block"; // Arka plan karartılır
        
        // Animasyonu başlatmak için
        setTimeout(() => {
            menu.style.transform = "translateY(0)"; // Menü aşağı kayar
            menu.style.opacity = "1"; // Menü görünür hale gelir
        }, 10); // Geçişin başlaması için küçük bir zaman aralığı bırakıyoruz
    } else {
        // Menü kapanırken animasyon
        menu.style.transform = "translateY(-20px)"; // Menü yukarı kayar
        menu.style.opacity = "0"; // Menü kaybolur
        
        // Menü ve karartmayı gizleme
        setTimeout(() => {
            menu.style.display = "none"; // Menü gizlenir
            overlay.style.display = "none"; // Karartma kalkar
        }, 500); // Animasyonun bitmesi için 500ms bekleriz
    }
}

// Karartma alanına tıklanarak menüyü kapatmak için
document.getElementById("overlay").addEventListener("click", function () {
    const menu = document.getElementById("galleryMenu");
    const overlay = document.getElementById("overlay");
    
    menu.style.transform = "translateY(-20px)"; // Menü yukarı kayar
    menu.style.opacity = "0"; // Menü kaybolur
    
    // Menü ve karartmayı gizleme
    setTimeout(() => {
        menu.style.display = "none"; // Menü gizlenir
        overlay.style.display = "none"; // Karartma kalkar
    }, 500); // Animasyonun bitmesi için 500ms bekleriz
});
