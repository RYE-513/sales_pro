<template>
    <div class="modal fade" tabindex="-1" role="dialog" ref="modal">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
        <div class="modal-header bg-soft-success" style="padding: 20px;">
            <h5 class="modal-title">Add New Item</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
        </div>
        <div class="modal-body">
            <form @submit.prevent="submitForm">
            <div class="mb-3">
                <label for="itemName" class="form-label">Item Name</label>
                <input type="text" class="form-control mb-1" id="item_name" placeholder="Item Name" v-model="formData.item_name">
            </div>
            <!-- <div class="mb-3">
                <label for="category" class="form-label">Product Category</label>
                <select class="form-control" v-model="formData.categories_id">
                    <option value="">Select Categories</option>
                    <option v-for="categories  in category_list " :key="categories.id" :value="categories.id">{{ categories.category_name  }}</option>
                </select>
            </div>
            <div class="mb-3">
                <label for="package" class="form-label">Product Package</label>
                <select class="form-control" v-model="formData.packages_id">
                    <option value="">Select Package</option>
                    <option v-for="packages in packages_list" :key="packages.id" :value="packages.id">{{ packages.packages_name }}</option>
                </select>
            </div> -->
            <button type="submit" class="btn btn-success">Add Items</button>
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
        }, 
        };
    },
    methods: {
        openAddModal() {
        $(this.$refs.modal).modal('show');
        },
        closeModal() {
        $(this.$refs.modal).modal('hide');
        },
    
        submitForm() {
            axios.post('/api/items/', this.formData)
                .then(response => {
                this.$emit('addItemsSuccess', response.data);
                this.closeModal();
                
                setTimeout(function() {
                location.reload();
                }, 500);
    
                })
                .catch(error => {
                console.error('Error adding item:', error);
                });
            }
        }
    };
</script>

<!-- <script>
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
        axios.get('/api/categories')
        .then(response => {
            this.categories = response.data;
        })
        .catch(error => {
            console.error('Error fetching categories:', error);
        });
    },
    fetchPackages() {
        axios.get('/api/packages')
        .then(response => {
            this.packages = response.data;
        })
        .catch(error => {
            console.error('Error fetching packages:', error);
        });
    },
    submitForm() {
        axios.post('/api/items', this.formData)
        .then(response => {
            console.log('Product added successfully:', response.data);
            this.closeModal();
        })
        .catch(error => {
            console.error('Error adding item:', error);
        });
    }
    },
    mounted() {
    this.fetchCategories();
    this.fetchPackages();
    }
};
</script> -->
