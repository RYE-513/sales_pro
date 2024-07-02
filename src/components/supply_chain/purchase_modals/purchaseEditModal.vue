<template>
    <div class="modal fade" id="editPurchaseModal" tabindex="-1" aria-labelledby="editPurchaseModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
            <div class="modal-header bg-soft-success" style="padding: 15px;">
                <h5 class="modal-title">Edit Purchase Information</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-view" name="id-view" readonly hidden>
                    <div class="row">
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="purchase-name-view" class="form-label">Supplier Name</label>
                                <input type="text" class="form-control" v-model="supplier" required>
                            </div>
                        
                            <div class="col-md-6">
                                <label for="po-view" class="form-label">PO Number</label>
                                <input type="text" class="form-control" v-model="po_number" required>
                            </div>
                        </div>

                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="deliveryaddress-view" class="form-label">Delivery Address</label>
                                <input type="text" class="form-control" v-model="delivery_address" required>
                            </div>  
                        
                            <div class="col-md-6">
                                <label for="deliverydate-view" class="form-label">Delivery Date</label>
                                <input type="date" class="form-control" v-model="delivery_date" required>
                            </div>
                        </div>
                    </div>
                    <button type="submit" class="btn btn-success btn-block" @click="updatePurchase()">Update</button>
                </form>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
export default {
    props: ['selectedPurchaseId'],
    data() {
        return {
            purchaseid: '',
            supplier: '',
            po_number: '',
            delivery_address: '',
            delivery_date: ''
        };
    },
    watch: {
        selectedPurchaseId: {
            immediate: true,
            handler(newVal){
                if(newVal) {
                    this.fetchPurchase(newVal);
                }
            }
        }
    },
    methods: {
        fetchPurchase(selectedPurchaseId) {
            axios.get(`/api/purchase/${selectedPurchaseId}/`)
            .then(response => {
                const purchaseDetails = response.data;
                this.supplier = purchaseDetails.supplier;
                this.po_number = purchaseDetails.po_number;
                this.delivery_address = purchaseDetails.delivery_address;
                this.delivery_date = purchaseDetails.delivery_date;
            })
            .catch(error => {
                console.error('Error fetching Purchase:', error);
            });
        },

        updatePurchase() {
            axios.put(`/api/purchase/${this.selectedPurchaseId}/`, {
                supplier: this.supplier,
                po_number: this.po_number,
                delivery_address: this.delivery_address,
                delivery_date: this.delivery_date
            })
            .then(response => {
                console.log(`Purchase with ID ${this.selectedPurchaseId} updated successfully`, response.data);
                this.$emit('purchaseUpdated', response.data);
                $('#editPurchaseModal').modal('hide');

                setTimeout(function() {
                    location.reload();
                }, 500);
            })
            .catch(error => {
                console.error('Error updating purchase:', error);
            });
        }
    }
};
</script>