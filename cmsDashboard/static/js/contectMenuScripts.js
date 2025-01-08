// Sidebar'ı açıp kapatma
function toggleSidebar() {
    const sidebar = document.getElementById('mySidebar');
    sidebar.classList.toggle('hidden');
}

// Accordion Menüler için
document.addEventListener('DOMContentLoaded', () => {
    const headers = document.querySelectorAll('h1');

    headers.forEach(header => {
        header.addEventListener('click', () => {
            // Tüm menüleri kapat
            headers.forEach(h => {
                if (h !== header) {
                    h.classList.remove('active');
                    const siblingContent = h.nextElementSibling;
                    if (siblingContent) siblingContent.style.display = 'none';
                }
            });

            // Tıklanan menüyü aç/kapat
            header.classList.toggle('active');
            const content = header.nextElementSibling;

            if (content) {
                if (header.classList.contains('active')) {
                    content.style.display = 'block';
                } else {
                    content.style.display = 'none';
                }
            }
        });
    });
});
