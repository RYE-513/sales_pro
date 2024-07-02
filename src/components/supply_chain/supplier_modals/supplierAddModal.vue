<template>
    <div class="modal fade" tabindex="-1" role="dialog" ref="modal">
        <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content">
            <div class="modal-header bg-soft-success" style="padding: 20px;">
                <h5 class="modal-title">Add New Supplier</h5>
                <button type="button" class="btn-close" @click="closeModal"></button>
            </div>
        <div class="modal-body">
            <form @submit.prevent="submitForm">
            <div class="mb-3 row">
                <div class="col-md-6">
                    <label for="supplier_name" class="form-label">Supplier Name</label>
                    <input type="text" class="form-control mb-1" id="supplier_name" placeholder="Supplier Name" v-model="formData.supplier_name">
                </div>
                <div class="col-md-6">
                    <label for="location" class="form-label">Location</label>
                    <input type="text" class="form-control mb-1" id="location" placeholder="Location" v-model="formData.location">
                </div>
            </div>
            <div class="mb-3 row">
                <div class="col-md-6">
                    <label for="contact_number" class="form-label">Contact Number</label>
                    <div class="input-group">
                        <span class="input-group-text">(+63)</span>
                        <input type="text" class="form-control" id="contact_number" name="contact_number" required>
                    </div>
                </div>
                <div class="col-md-6">
                    <label for="contact_person" class="form-label">Contact Person</label>
                    <input type="text" class="form-control mb-1" id="contact_person" placeholder="Contact Person" v-model="formData.contact_person">
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Add Supplier</button>
            </form>
        </div>
    </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
    return {
        formData: {
        item_name: '',
        categories_id: '',
        packages_id: '',
        },
        categories: [],
        packages: []
    };
    },
    methods: {
    openModal() {
        $(this.$refs.modal).modal('show');
    },
    closeModal() {
        $(this.$refs.modal).modal('hide');
    },
    fetchCategories() {
        // Assuming you have an endpoint for fetching categories
        axios.get('/api/categories')
        .then(response => {
            this.categories = response.data;
        })
        .catch(error => {
            console.error('Error fetching categories:', error);
        });
    },
    fetchPackages() {
        // Assuming you have an endpoint for fetching packages
        axios.get('/api/packages')
        .then(response => {
            this.packages = response.data;
        })
        .catch(error => {
            console.error('Error fetching packages:', error);
        });
    },
    submitForm() {
        // Assuming you have an endpoint for adding products
        axios.post('/api/items', this.formData)
        .then(response => {
            // Handle success
            console.log('Product added successfully:', response.data);
            this.closeModal();
        })
        .catch(error => {
            console.error('Error adding item:', error);
        });
    }
    },
    mounted() {
      // Fetch categories and packages when the component is mounted
    this.fetchCategories();
    this.fetchPackages();
    }
};
</script>
