<template>
<div class="modal fade" id="deleteBranchModal" tabindex="-1" aria-labelledby="deleteBranchModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
        <div class="modal-header bg-soft-danger" style="padding: 20px; ">
            <h5 class="modal-title">Delete Branch</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <form @submit.prevent="deleteBranch">
            <div class="mb-3">
                <label for="branchName" class="form-label">Branch Name</label>
                <input type="text" class="form-control mb-1" id="branch_name-delete" readonly>
            </div>
            
            <div class="mb-3">
                <label for="location" class="form-label">Location</label>
                <input type="text" class="form-control" id="location-delete" readonly>
            </div>
            
            <div class="mb-3">
                <label for="manager" class="form-label">Manager</label>
                <input type="text" class="form-control" id="manager-delete" readonly>
                <!-- <select class="form-control" readonly>
                </select> -->
            </div>

            <div class="col-lg-12">
                <div>
                    <button type="button" id="btn_delete_info" class="btn btn-danger btn-block" @click="deleteBranch()">Delete</button>
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
    props: ['selectedBranchId'],

    methods: {
    openAddModal() {
    $(this.$refs.modal).modal('show');
    },
    closeModal() {
    $(this.$refs.modal).modal('hide');
    },

    deleteBranch() {
    const branchId = this.selectedBranchId;
    const newStatus = 'Deleted';
    
    axios.get(`/api/branches/${branchId}`)
        .then(response => {
            const branchDetails = response.data;
            return axios.put(`/api/branches/${branchId}/`, {
                branch_name: branchDetails.branch_name,
                location: branchDetails.location,
                status: newStatus
            });
        })
        .then(response => {
            console.log(`Status of the branch with ID ${branchId} changed successfully`, response.data);
            this.$emit('branchDeleted', response.data);
            this.closeModal();
            
            setTimeout(() => {
                location.reload();
            }, 500);
        })
        .catch(error => {
            console.error('Error deleting branch:', error);
        });
        }
    }
};
</script>