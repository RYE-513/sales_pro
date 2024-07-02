<template>
    <div class="modal fade" id="recoverRolesModal" tabindex="-1" aria-labelledby="recoverRolesModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header bg-soft-warning" style="padding: 20px;">
                <h5 class="modal-title">Role Information</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-recover" name="id-recover" readonly hidden>
                        <div class="mb-3 row">
                            <div class="md-12">
                                <label for="role-name-recover" class="form-label">Role Name</label>
                                <input type="text" class="form-control" id="role_name-recover" name="role_name-recover" readonly>
                            </div>
                        </div>
                        <div class="mb-3 row">
                            <div class="md-12">
                                <label for="description-recover" class="form-label">Description</label>
                                <input type="text" class="form-control" id="description-recover" name="description-recover" readonly>
                            </div>
                        </div>
                        <div class="col-lg-12">
                            <div>
                                <button type="button" id="btn_update_info" class="btn btn-warning btn-block" @click="recoverRole()">Recover</button>
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
    $(this.$refs.modal).modal('show');
    },
    closeModal() {
    $(this.$refs.modal).modal('hide');
    },

    recoverRole() {
    const roleId = this.selectedRoleId;
    const newStatus = 'Active';
    
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
            this.$emit('roleRecover', response.data);
            this.closeModal();
            
            setTimeout(() => {
                location.reload();
            }, 500);
        })
        .catch(error => {
            console.error('Error recover role:', error);
        });
        }
    }
};
</script>
