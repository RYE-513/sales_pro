<template>
    <div class="modal fade" id="editWarehouseModal" tabindex="-1" aria-labelledby="editWarehouseModalLabel" aria-modal="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header bg-soft-success" style="padding: 20px;">
                    <h5 class="modal-title">Edit Warehouse</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
            <form>
            <div class="mb-3">
                <label for="warehouseName" class="form-label">Branch Name</label>
                <input type="text" class="form-control mb-1" v-model="warehouse_name" required>
            </div>
            
            <div class="mb-3">
                <label for="location" class="form-label">Location</label>
                <input type="text" class="form-control" v-model="location" required>
            </div>
            
            <div class="mb-3">
                <label for="manager" class="form-label">Caretaker</label>
                <input type="text" class="form-control" id="warehouse-caretaker-edit" required>
                <!-- <select class="form-control" required>
                    <option value="">Select Manager</option>
                     <option v-for="staff in staffList" :key="staff.id" :value="staff.id">{{ staff.first_name }} {{ staff.last_name }}</option>
                </select> -->
            </div>
            <button type="submit" class="btn btn-success" @click="editWarehouse()">Update</button>
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
    data() {
        return {
            id: '',
            warehouse_name: '',
            location: '',
            caretaker: ''
        };
    },
    watch: {
        selectedWarehouseId: {
            immediate: true,
            handler(newVal) {
                if(newVal) {
                    this.fetchWarehouse(newVal);
                }
            }
        }
    },
    methods: {
        fetchWarehouse(selectedWarehouseId) {
            axios.get(`/api/warehouses/${selectedWarehouseId}/`)
            .then(response => {
                const warehouseDetails = response.data;
                this.warehouse_name = warehouseDetails.warehouse_name;
                this.location = warehouseDetails.location;
                this.caretaker = warehouseDetails.caretaker;
            })
            .catch(error => {
                console.error('Error fetching warehouse:', error);
            });
        },
        editWarehouse() {
            axios.put(`/api/warehouses/${this.selectedWarehouseId}/`, {
                warehouse_name: this.warehouse_name,
                location: this.location,
                caretaker: this.caretaker
            })
            .then(response => {
                console.log(`Warehouse with ID ${this.selectedWarehouseId} updated successfully`, response.data);
                this.$emit('warehouseUpdated'. response.data);
                $('#editWarehouseModal').modal('hide');

                setTimeout(function() {
                    location.reload();
                }, 500);
            })
            .catch(error => {
                console.error('Error updating warehouse:', error);
            });
        }
    }
};
</script>