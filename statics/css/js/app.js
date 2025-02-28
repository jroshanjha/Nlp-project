// static/js/app.js

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips and popovers
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));

    // Add responsive behavior for product cards on small screens
    function adjustCardLayout() {
        const windowWidth = window.innerWidth;
        const productCards = document.querySelectorAll('.product-card');
        
        if (windowWidth < 576) {  // Bootstrap's sm breakpoint
            productCards.forEach(card => {
                const footer = card.querySelector('.card-footer');
                const buttons = footer.querySelectorAll('.btn');
                
                buttons.forEach(btn => {
                    btn.classList.add('btn-block', 'mb-2');
                    btn.classList.remove('btn-sm');
                });
                
                footer.classList.add('d-block');
                footer.classList.remove('d-flex', 'justify-content-between');
            });
        } else {
            productCards.forEach(card => {
                const footer = card.querySelector('.card-footer');
                const buttons = footer.querySelectorAll('.btn');
                
                buttons.forEach(btn => {
                    btn.classList.remove('btn-block', 'mb-2');
                    btn.classList.add('btn-sm');
                });
                
                footer.classList.remove('d-block');
                footer.classList.add('d-flex', 'justify-content-between');
            });
        }
    }

    // Call on page load and when window resizes
    adjustCardLayout();
    window.addEventListener('resize', adjustCardLayout);

    // Dynamic content loading for the product list
    const productContainer = document.getElementById('products-container');
    if (productContainer) {
        // Implement lazy loading of products
        let page = 1;
        let loading = false;
        const loadMoreProducts = async () => {
            if (loading) return;
            
            try {
                loading = true;
                const products = await ProductAPI.getProducts();
                // In a real app, you'd use pagination with page parameter
                
                if (products.length === 0) {
                    // No more products to load
                    window.removeEventListener('scroll', handleScroll);
                    return;
                }
                
                // Render additional products
                products.forEach(product => {
                    // Logic to render products dynamically would go here
                });
                
                page++;
            } catch (error) {
                console.error('Failed to load more products:', error);
            } finally {
                loading = false;
            }
        };
        
        const handleScroll = () => {
            const { scrollTop, scrollHeight, clientHeight } = document.documentElement;
            
            if (scrollTop + clientHeight >= scrollHeight - 20) {
                loadMoreProducts();
            }
        };
        
        // Uncomment to enable infinite scrolling
        // window.addEventListener('scroll', handleScroll);
    }
});