<template>
    <div class="modal fade" id="recoverWarehouseModal" tabindex="-1" aria-labelledby="recoverWarehouseModalLabel" aria-modal="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
            <div class="modal-header bg-soft-warning" style="padding: 20px;">
                <h5 class="modal-title">Warehouse Information</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                <div class="mb-3">
                    <label for="branchName" class="form-label">Warehouse Name</label>
                    <input type="text" class="form-control mb-1" id="warehouse_name-recover" readonly>
                </div>
                <div class="mb-3">
                    <label for="location" class="form-label">Location</label>
                    <input type="text" class="form-control" id="warehouse-location-recover" readonly>
                </div>
                <div class="mb-3">
                    <label for="manager" class="form-label">Caretaker</label>
                    <input type="text" class="form-control" id="warehouse-caretaker-recover" readonly>
                </div>
                <div class="col-lg-12">
                    <div>
                        <button type="button" id="btn_update_info" class="btn btn-warning btn-block" @click="recoverWarehouse()">Recover</button>
                    </div>
                </div>
                </form>
            </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    props: ['selectedWarehouseId'],

    methods: {
    openAddModal() {
    $(this.$refs.modal).modal('show');
    },
    closeModal() {
    $(this.$refs.modal).modal('hide');
    },

    recoverWarehouse() {
    const warehouseId = this.selectedWarehouseId;
    const newStatus = 'Active';
    axios.get(`/api/warehouses/${warehouseId}`)
        .then(response => {
            const warehouseDetails = response.data;
            return axios.put(`/api/warehouses/${warehouseId}/`, {
                warehouse_name: warehouseDetails.warehouse_name,
                location: warehouseDetails.location,
                caretaker: warehouseDetails.caretaker,
                status: newStatus
            });
        })
        .then(response => {
            console.log(`Status of the warehouse with ID ${warehouseId} changed successfully`, response.data);
            this.$emit('warehouseRecover', response.data);
            this.closeModal();
            
            setTimeout(() => {
                location.reload();
            }, 500);
        })
        .catch(error => {
            console.error('Error recover warehouse:', error);
        });
        }
    }
};
</script>