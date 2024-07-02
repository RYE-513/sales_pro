<template>
    <div class="modal fade" id="editRolesModal" tabindex="-1" aria-labelledby="editRolesModalLabel" aria-modal="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header bg-soft-success" style="padding: 20px;">
                    <h5 class="modal-title">Edit Role</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form @submit.prevent="updateRole">
                        <input type="hidden" v-model="roleId">
                        <div class="mb-3">
                            <label for="role-name-edit" class="form-label">Role Name</label>
                            <input type="text" class="form-control" v-model="roleName" required>
                        </div>
                        <div class="mb-3">
                            <label for="description-edit" class="form-label">Description</label>
                            <input type="text" class="form-control" v-model="description" required>
                        </div>
                        <button type="submit" class="btn btn-success btn-block">Update</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    props: ['selectedRoleId'],

    data() {
        return {
            roleId: '',
            roleName: '',
            description: ''
        };
    },

    watch: {
        selectedRoleId: {
            immediate: true, // Fetch role immediately when component is mounted
            handler(newVal) {
                if (newVal) {
                    this.fetchRole(newVal);
                }
            }
        }
    },

    methods: {
        fetchRole(selectedRoleId) {
            axios.get(`/api/roles/${selectedRoleId}/`)
                .then(response => {
                    const roleDetails = response.data;
                    this.roleName = roleDetails.role_name;
                    this.description = roleDetails.description;
                })
                .catch(error => {
                    console.error('Error fetching role:', error);
                });
        },

        updateRole() {
            axios.put(`/api/roles/${this.selectedRoleId}/`, {
                role_name: this.roleName,
                description: this.description
            })
            .then(response => {
                console.log(`Role with ID ${this.selectedRoleId} updated successfully`, response.data);
                this.$emit('roleUpdated', response.data);
                $('#editRolesModal').modal('hide');

                setTimeout(function() { 
                location.reload();
                }, 500);
            })
            .catch(error => {
                console.error('Error updating role:', error);
            });
        }
    }
};
</script>