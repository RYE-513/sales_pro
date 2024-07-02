<template>
    <div class="modal fade" id="editStaffModal" tabindex="-1" aria-labelledby="editStaffModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
            <div class="modal-header bg-soft-success" style="padding: 20px;">
                <h5 class="modal-title">Edit Staff</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-edit" name="id-edit" readonly hidden>
                    <div class="mb-3 row">
                        <div class="col-md-6">
                            <label for="firstName" class="form-label">First Name</label>
                            <input type="text" class="form-control mb-1" id="first_name-edit" v-model="first_name" name="first_name-edit" required>
                        </div>

                        <div class="col-md-6">
                            <label for="lastName" class="form-label">Last Name</label>
                            <input type="text" class="form-control mb-1" id="last_name-edit" v-model="last_name" name="last_name-edit" required>
                        </div>
                    </div>
        
                    <div class="mb-3 row">
                        <div class="col-md-6">
                            <label for="mobile_no" class="form-label">Contact Number</label> 
                            <div class="input-group"> 
                                <span class="input-group-text">(+63)</span> 
                                <input type="text" class="form-control" id="mobile_no-edit" v-model="mobile_no" name="mobile_no-edit" required> 
                            </div>
                        </div> 
        
                        <div class="col-md-6">
                            <label for="email" class="form-label">Email Address</label>
                            <input type="email" class="form-control" id="email-edit" v-model="email" name="email-edit" required>
                        </div>
        
                    </div>

                    <div class="mb-3">
                        <label for="roles" class="form-label">Roles</label>
                        <input type="roles" class="form-control" id="roles-edit" name="roles-edit" required>
                    </div>

                    <div class="col-lg-12">
                        <div>
                            <button type="button" id="btn_update_info" class="btn btn-success btn-block" @click="updateStaff()">Update</button>
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

    data() {
        return {
            staffId: '',
            first_name: '',
            last_name: '',
            mobile_no: '',
            email: '',
            role: '',
            selectedRole: []
        };
    },
    watch: {
        selectedStaffId: {
            immediate: true,
            handler(newVal) {
                if(newVal) {
                    this.fetchStaff(newVal);
                }
            }
        }
    },

    methods: {
        fetchStaff(selectedStaffId) {
            axios.get(`/api/staff/${selectedStaffId}`)
            .then(response => {
                const staffDetails = response.data;
                this.first_name = staffDetails.first_name;
                this.last_name = staffDetails.last_name;
                this.mobile_no = staffDetails.mobile_no;
                this.email = staffDetails.email;
                this.role = staffDetails.role;
            })
            .catch(error => {
                console.error('Error fetching Staff:', error);
            });
        },
        
        updateStaff() {
            axios.put(`/api/staff/${this.selectedStaffId}/`, {
                first_name: this.first_name,
                last_name: this.last_name,
                mobile_no: this.mobile_no,
                email: this.email,
                role: this.role
            })
            .then(response => {
                console.log(`Staff with ID ${this.selectedStaffId} updated successfully`, response.data);
                this.$emit ('StaffUpdated', response.data);
                // @ts-ignore
                $('#editStaffModal').modal('hide');

                setTimeout(function() {
                    location.reload();
                }, 500);
            })
            .catch(error => {
                console.error('Error Updating Staff:', error);
            });
        }
    }
};
</script>