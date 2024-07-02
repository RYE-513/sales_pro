<template>
    <div class="modal fade" id="editCategoryModal" tabindex="-1" aria-labelledby="editCategoryModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header bg-soft-success" style="padding: 15px;">
                <h5 class="modal-title">Edit Category</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-edit" name="id-edit" readonly hidden>
                    <div class="">
                        <div class="mb-3">
                            <label for="product-category-edit" class="form-label">Category Name</label>
                            <input type="text" class="form-control" v-model="category_name" name="product-category-edit" required>
                        </div>
                    </div>
                    <div class="col-lg-12">
                        <div class="hstack gap-2 justify-content-end">
                            <button type="button" id="btn_update_info" class="btn btn-success btn-block" @click="editCategory()">Save</button>
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
    props: ['selectedCategoryId'],

    data() {
        return {
            categoryId: '',
            category_name: '',
            description: ''
        };
    },
    watch: {
        selectedCategoryId: {
            immediate: true,
            handler(newVal) {
                if(newVal) {
                    this.fetchCategory(newVal);
                }
            }
        }
    },
    methods: {
        fetchCategory(selectedCategoryId) {
            axios.get(`api/categories/${selectedCategoryId}/`)
                .then(response => {
                    const categoryDetails = response.data;
                    this.category_name = categoryDetails.category_name;
                    this.description = categoryDetails.description;
                })
                .catch(error => {
                    console.error('Error fetching Categories', error);
                });
        },

        editCategory() {
            axios.put(`/api/categories/${this.selectedCategoryId}/`, {
                category_name: this.category_name,
                description: this.description,
            })
            .then(response => {
                console.log(`Category with Id ${this.selectedCategoryId} updated successfully`, response.data);
                this.$emit('CategoryUpdated', response.data);
                $('#editCategoryModal').modal('hide');

                setTimeout(function() {
                    location.reload();
                }, 500);
            })
            .catch(error => {
                console.error('Error updating category:', error);
            });
        }
    }
};
</script>