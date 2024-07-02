<template>
    <div class="modal fade" tabindex="-1" role="dialog" ref="modal">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title">Add Packages</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
        </div>
        <div class="modal-body">
            <form @submit.prevent="submitForm">
            <div class="mb-3">
                <label for="packageName" class="form-label">Package Name</label>
                <input type="text" class="form-control mb-1" id="package_name" placeholder="Package Name"  v-model="formData.package_name">
            </div>


            <button type="submit" class="btn btn-primary">Add Package</button>
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
            package_name: '',
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
            axios.post('/api/packages/', this.formData)
                .then(response => {
                this.$emit('addRoleSuccess', response.data);
                this.closeModal();
                
                setTimeout(function() {
                location.reload();
                }, 500);
    
                })
                .catch(error => {
                console.error('Error adding role:', error);
                });
            }
        }
    };
</script>