<template>
    <div class="modal fade" tabindex="-1" role="dialog" ref="modal">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title">Add Categories </h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
        </div>
        <div class="modal-body">
            <form @submit.prevent="submitForm">
            <div class="mb-3">
                <label for="categoryName" class="form-label">Category Name</label>
                <input type="text" class="form-control mb-1" id="category_name" placeholder="Category Name"  v-model="formData.category_name">
            </div>

            <div class="mb-3">
                <label for="description" class="form-label">Description</label>
                <input type="text" class="form-control mb-1" id="description" placeholder="description"  v-model="formData.description">
            </div>

            <button type="submit" class="btn btn-primary">Add Category</button>
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
        category_name: '',
        description: '',
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
    fetchCategories() {
        axios.get('/api/categories/')
        .then(response => {
            this.categories = response.data;
        })
        .catch(error => {
            console.error('Error fetching categories:', error);
        });
    },
    submitForm() {
        axios.post('/api/categories/', this.formData)
                .then(response => {
                this.$emit('addCategorySuccess', response.data);
                this.closeModal();
                
                setTimeout(function() {
                location.reload();
                }, 500);
    
                })
                .catch(error => {
                console.error('Error adding category:', error);
                });
    }
    },
    mounted() {
      // Fetch categories and packages when the component is mounted
    this.fetchCategories();
    }
};
</script>
