<template>
<div class="modal fade" id="recoverBranchModal" tabindex="-1" aria-labelledby="recoverBranchModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
        <div class="modal-header bg-soft-warning" style="padding: 20px;">
            <h5 class="modal-title">Branch Information</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <form>
            <div class="mb-3">
                <label for="branchName" class="form-label">Branch Name</label>
                <input type="text" class="form-control mb-1" id="branch_name-recover" readonly>
            </div>
            <div class="mb-3">
                <label for="location" class="form-label">Location</label>
                <input type="text" class="form-control" id="location-recover" readonly>
            </div>
            <div class="mb-3">
                <label for="manager" class="form-label">Manager</label>
                <input type="text" class="form-control" id="manager-recover" readonly>
                <!-- <select class="form-control" readonly>
                </select> -->
            </div>
            <div class="col-lg-12">
                <div>
                    <button type="button" id="btn_update_info" class="btn btn-warning btn-block" @click="recoverBranch()">Recover</button>
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

    recoverBranch() {
    const branchId = this.selectedBranchId;
    const newStatus = 'Active';
    
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
            this.$emit('branchRecover', response.data);
            this.closeModal();
            
            setTimeout(() => {
                location.reload();
            }, 500);
        })
        .catch(error => {
            console.error('Error recover branch:', error);
        });
        }
    }
};
</script>