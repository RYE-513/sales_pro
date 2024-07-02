<template>
    <div class="modal fade" id="deleteStaffModal" tabindex="-1" aria-labelledby="deleteStaffModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
            <div class="modal-header bg-soft-danger" style="padding: 20px;">
                <h5 class="modal-title">Delete Staff</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-delete" name="id-delete" readonly hidden>
                    <div class="mb-3 row">
                        <div class="col-md-6">
                            <label for="firstName" class="form-label">First Name</label>
                            <input type="text" class="form-control mb-1" id="first_name-delete" name="first_name-delete" readonly>
                        </div>

                        <div class="col-md-6">
                            <label for="lastName" class="form-label">Last Name</label>
                            <input type="text" class="form-control mb-1" id="last_name-delete" name="last_name-delete" readonly>
                        </div>
                    </div>
        
                    <div class="mb-3 row">
                        <div class="col-md-6">
                            <label for="mobile_no" class="form-label">Contact Number</label> 
                            <div class="input-group"> 
                                <span class="input-group-text">(+63)</span> 
                                <input type="text" class="form-control" id="mobile_no-delete" name="mobile_no-delete" readonly> 
                            </div>
                        </div> 
        
                        <div class="col-md-6">
                            <label for="email" class="form-label">Email Address</label>
                            <input type="email" class="form-control" id="email-delete" name="email-delete" readonly>
                        </div>
        
                    </div>

                    <div class="mb-3">
                        <label for="roles" class="form-label">Roles</label>
                        <input type="roles" class="form-control" id="roles-delete" name="roles-delete" readonly>
                    </div>

                    <div class="col-lg-12">
                        <div>
                            <button type="button" id="btn_update_info" class="btn btn-danger btn-block" @click="deleteStaff()">Delete</button>
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

    deleteStaff() {
    const staffId = this.selectedStaffId;
    const newStatus = 'Deleted';
    
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
            this.$emit('staffDeleted', response.data);
            this.closeModal();
            
            setTimeout(() => {
                location.reload();
            }, 500);
        })
        .catch(error => {
            console.error('Error deleting staff:', error);
        });
        }
    }
};
</script>
