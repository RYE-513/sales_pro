<template>
    <div class="modal fade" id="deleteProductsModal" tabindex="-1" aria-labelledby="deleteProductsModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-md">
        <div class="modal-content">
            <div class="modal-header bg-soft-danger" style="padding: 15px;">
                <h5 class="modal-title" id="disableProductsModalLabel">Disable Products</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
                            <div class="modal-body">
                                <p>Are you sure you want to disable this Products?</p>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                                <form id="disableProductsForm" method="post">
                                    <input type="hidden" name="products_id" id="products_id_input" value="">
                                    <button type="submit" class="btn btn-danger" id="confirmProductsDisableButton" @click="deleteProduct()">Disable</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
</template>

<script>
import axios from 'axios';
export default {
    props: ['selectedProductId'],

    methods: {
    openAddModal() {
    $(this.$refs.modal).modal('show');
    },
    closeModal() {
    $(this.$refs.modal).modal('hide');
    },

    deleteProduct() {
    const productId = this.selectedProductId;
    const newStatus = 'Disabled';
    
    axios.get(`/api/products/${productId}`)
        .then(response => {
            const productDetails = response.data;
            return axios.put(`/api/products/${productId}/`, {
                product_name: productDetails.product_name,
                product_category: productDetails.product_category,
                product_package: productDetails.product_package,
                current_price: productDetails.current_price,
                status: newStatus
            });
        })
        .then(response => {
            console.log(`Status of the products with ID ${productId} changed successfully`, response.data);
            this.$emit('productsDeleted', response.data);
            this.closeModal();
            
            setTimeout(() => {
                location.reload();
            }, 500);
        })
        .catch(error => {
            console.error('Error deleting products:', error);
        });
        }
    }
};
</script>