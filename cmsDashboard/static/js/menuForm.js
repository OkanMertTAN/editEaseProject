document.addEventListener('DOMContentLoaded', () => {
    function toggleCustomMenu(menuId) {
        const menu = document.getElementById(menuId);
        if (menu) {
            const isHidden = menu.style.display === 'none' || !menu.style.display;
            menu.style.display = isHidden ? 'block' : 'none';

            // Close other menus
            document.querySelectorAll('.form-container').forEach(container => {
                if (container.id !== menuId) {
                    container.style.display = 'none';
                }
            });
        }
    }

    // Initially hide all form containers
    document.querySelectorAll('.form-container').forEach(container => {
        container.style.display = 'none';
    });

    // Add click events to menu items dynamically
    document.querySelectorAll('.menu-item').forEach(item => {
        const targetMenu = item.getAttribute('data-target');
        if (targetMenu) {
            item.addEventListener('click', () => toggleCustomMenu(targetMenu));
        }
    });
});