<template>
    <div class="modal fade" id="editSupplierModal" tabindex="-1" aria-labelledby="editSupplierModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
            <div class="modal-header bg-soft-success" style="padding: 15px;">
                <h5 class="modal-title">Supplier Information</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-edit" name="id-edit" readonly hidden>
                    <div class="row">
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="supplier-name-edit" class="form-label">Supplier Name</label>
                                <input type="text" class="form-control" v-model="supplier_name" name="supplier-name-edit" required>
                            </div>
                        
                            <div class="col-md-6">
                                <label for="supplier-location-edit" class="form-label">Location</label>
                                <input type="text" class="form-control" v-model="location" name="supplier-location-edit" required>
                            </div>
                        </div>

                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="supplier-contact_number-edit" class="form-label">Contact Number</label>
                                <input type="text" class="form-control" v-model="contact_number" name="supplier-contact_number-edit" required>
                            </div>  
                        
                            <div class="col-md-6">
                                <label for="supplier-contact_person-edit" class="form-label">Contact Person</label>
                                <input type="text" class="form-control" v-model="contact_person" name="supplier-contact_person-edit" required>
                            </div>
                        </div>
                    
                        <div class="col-lg-12">
                            <button type="submit" class="btn btn-success" @click="updateSupplier()">Update</button>
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
    props: ['selectedSupplierId'],

    data() {
        return{
        supplierId: '',
        supplier_name: '',
        location: '',
        contact_number: '',
        contact_person: ''
    };
    },
    watch: {
        selectedSupplierId: {
            immediate: true,
            handler(newVal) {
                if(newVal) {
                    this.fetchSupplier(newVal);
                }
            }
        }
    },

    methods: {
        fetchSupplier(selectedSupplierId) {
            axios.get(`/api/supplier/${selectedSupplierId}/`)
            .then(response => {
                const supplierDetails = response.data;
                this.supplier_name = supplierDetails.supplier_name;
                this.location = supplierDetails.location;
                this.contact_number = supplierDetails.contact_number;
                this.contact_person = supplierDetails.contact_person;
            })
            .catch(error => {
                console.error('Error fetching supplier', error);
            });
        },
        updateSupplier() {
            axios.put(`/api/supplier/${this.selectedSupplierId}/`, {
                supplier_name: this.supplier_name,
                location: this.location,
                contact_number: this.contact_number,
                contact_person: this.contact_person
            })
            .then(response => {
                console.log(`Supplier with ID ${this.selectedSupplierId} updated successfully`, response.data);
                this.$emit('supplierUpdated', response.data);
                $('#editSupplierModal').modal('hide');

                setTimeout(function() {
                    location.reload();
                }, 500);
            })
            .catch(error => {
                console.error('Error updating supplier', error);
            });
        }
    }
};
</script>