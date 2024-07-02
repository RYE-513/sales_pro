<template>
    <div class="modal fade" id="recoverStaffModal" tabindex="-1" aria-labelledby="recoverStaffModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
            <div class="modal-header bg-soft-warning" style="padding: 20px;">
                <h5 class="modal-title">Staff Information</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-recover" name="id-recover" readonly hidden>
                    <div class="mb-3 row">
                        <div class="col-md-6">
                            <label for="firstName" class="form-label">First Name</label>
                            <input type="text" class="form-control mb-1" id="first_name-recover" name="first_name-recover" readonly>
                        </div>
                        <div class="col-md-6">
                            <label for="lastName" class="form-label">Last Name</label>
                            <input type="text" class="form-control mb-1" id="last_name-recover" name="last_name-recover" readonly>
                        </div>
                    </div>
                    <div class="mb-3 row">
                        <div class="col-md-6">
                            <label for="mobile_no" class="form-label">Contact Number</label> 
                            <div class="input-group"> 
                                <span class="input-group-text">(+63)</span> 
                                <input type="text" class="form-control" id="mobile_no-recover" name="mobile_no-recover" readonly> 
                            </div>
                        </div> 
                        <div class="col-md-6">
                            <label for="email" class="form-label">Email Address</label>
                            <input type="email" class="form-control" id="email-recover" name="email-recover" readonly>
                        </div>
                    </div>
                    <div class="mb-3">
                        <label for="roles" class="form-label">Roles</label>
                        <input type="roles" class="form-control" id="roles-recover" name="roles-recover" readonly>
                    </div>
                    <div class="col-lg-12">
                        <div>
                            <button type="button" id="btn_update_info" class="btn btn-warning btn-block" @click="recoverStaff()">Recover</button>
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
    props: ['selectedStaffId'],

    methods: {
    openAddModal() {
    $(this.$refs.modal).modal('show');
    },
    closeModal() {
    $(this.$refs.modal).modal('hide');
    },

    recoverStaff() {
    const staffId = this.selectedStaffId;
    const newStatus = 'Active';
    
    axios.get(`/api/staff/${staffId}`)
        .then(response => {
            const staffDetails = response.data;
            return axios.put(`/api/staff/${staffId}/`, {
                first_name: staffDetails.first_name,
                last_name: staffDetails.last_name,
                mobile_no: staffDetails.mobile_no,
                email: staffDetails.email,
                role: staffDetails.role,
                status: newStatus
            });
        })
        .then(response => {
            console.log(`Status of the staff with ID ${staffId} changed successfully`, response.data);
            this.$emit('staffRecover', response.data);
            this.closeModal();
            
            setTimeout(() => {
                location.reload();
            }, 500);
        })
        .catch(error => {
            console.error('Error recover staff:', error);
        });
        }
    }
};
</script>
