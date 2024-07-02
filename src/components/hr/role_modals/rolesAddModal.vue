<template>
    <div class="modal fade" tabindex="-1" role="dialog" ref="modal">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
        <div class="modal-header bg-soft-success" style="padding: 20px;">
            <h5 class="modal-title">Add New Role</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
        </div>
        <div class="modal-body">
            <form @submit.prevent="submitForm">
            <div class="mb-3">
                <label for="roleName" class="form-label">Role Name</label>
                <input type="text" class="form-control mb-1" id="role_name" name="role_name" placeholder="Roles" v-model="formData.role_name" required>
            </div>

            <div class="mb-3">
                <label for="description" class="form-label">Description</label>
                <input type="text" class="form-control mb-1" id="description" name="description" placeholder="Description" v-model="formData.description" required>
            </div>
            <button type="submit" class="btn btn-success">Add Role</button>
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
        role_name: '',
        description: '',
    }
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
        axios.post('http://merge.localhost:8000/api/roles/', this.formData)
            .then(response => {
            this.$emit('addRoleSuccess', response.data); // Emit event with new role data
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

