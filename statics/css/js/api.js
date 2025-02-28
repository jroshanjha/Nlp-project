/**
 * API Service for handling CRUD operations with the backend
 */
class ProductAPI {
    /**
     * Fetch all products
     * @returns {Promise} Promise object representing the products
     */
    static async getProducts() {
        try {
            const response = await fetch('/api/products');
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Error fetching products:', error);
            throw error;
        }
    }

    /**
     * Fetch a single product by ID
     * @param {number} id - The product ID
     * @returns {Promise} Promise object representing the product
     */
    static async getProduct(id) {
        try {
            const response = await fetch(`/api/products/${id}`);
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error(`Error fetching product ${id}:`, error);
            throw error;
        }
    }

    /**
     * Create a new product
     * @param {Object} productData - The product data
     * @returns {Promise} Promise object representing the created product
     */
    static async createProduct(productData) {
        try {
            const response = await fetch('/api/products', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCSRFToken()
                },
                body: JSON.stringify(productData)
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('Error creating product:', error);
            throw error;
        }
    }

    /**
     * Update an existing product
     * @param {number} id - The product ID
     * @param {Object} productData - The updated product data
     * @returns {Promise} Promise object representing the updated product
     */
    static async updateProduct(id, productData) {
        try {
            const response = await fetch(`/api/products/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCSRFToken()
                },
                body: JSON.stringify(productData)
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error(`Error updating product ${id}:`, error);
            throw error;
        }
    }

    /**
     * Delete a product
     * @param {number} id - The product ID
     * @returns {Promise} Promise object representing the operation result
     */
    static async deleteProduct(id) {
        try {
            const response = await fetch(`/api/products/${id}`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': this.getCSRFToken()
                }
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error(`Error deleting product ${id}:`, error);
            throw error;
        }
    }

    /**
     * Get CSRF token from the cookie
     * @returns {string} CSRF token
     */
    static getCSRFToken() {
        const name = 'csrf_token=';
        const decodedCookie = decodeURIComponent(document.cookie);
        const cookieArray = decodedCookie.split(';');
        
        for (let cookie of cookieArray) {
            while (cookie.charAt(0) === ' ') {
                cookie = cookie.substring(1);
            }
            
            if (cookie.indexOf(name) === 0) {
                return cookie.substring(name.length, cookie.length);
            }
        }
        
        // If no cookie found, try to get from the form
        const tokenInput = document.querySelector('input[name="csrf_token"]');
        return tokenInput ? tokenInput.value : '';
    }
}