<template>
    <div class="modal fade" id="deleteRolesModal" tabindex="-1" aria-labelledby="deleteRolesModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header bg-soft-danger" style="padding: 20px; ">
                <h5 class="modal-title">Delete Role</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-delete" name="id-delete" readonly hidden>
                        <div class="mb-3 row">
                            <div class="md-12">
                                <label for="role-name-delete" class="form-label">Role Name</label>
                                <input type="text" class="form-control" id="role-name-delete" name="role-name-delete" required>
                            </div>
                        </div>
                        
                        <div class="mb-3 row">
                            <div class="md-12">
                                <label for="description-delete" class="form-label">Description</label>
                                <input type="text" class="form-control" id="description-delete" name="description-delete" required>
                            </div>
                        </div>
                        
                        <div class="col-lg-12">
                            <div>
                                <button type="button" id="btn_update_info" class="btn btn-danger btn-block" @click="deleteRoles()">Delete</button>
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
    props: ['selectedRoleId'],

    methods: {
    openAddModal() {
    // @ts-ignore
    $(this.$refs.modal).modal('show');
    },
    closeModal() {
    // @ts-ignore
    $(this.$refs.modal).modal('hide');
    },

    deleteRoles() {
    const roleId = this.selectedRoleId;
    const newStatus = 'Deleted';
    
    axios.get(`/api/roles/${roleId}`)
        .then(response => {
            const roleDetails = response.data;
            return axios.put(`/api/roles/${roleId}/`, {
                role_name: roleDetails.role_name,
                description: roleDetails.description,
                status: newStatus
            });
        })
        .then(response => {
            console.log(`Status of the role with ID ${roleId} changed successfully`, response.data);
            this.$emit('roleDeleted', response.data);
            this.closeModal();
            
            setTimeout(() => {
                location.reload();
            }, 500);
        })
        .catch(error => {
            console.error('Error deleting roles:', error);
        });
        }
    }
 };
</script>
