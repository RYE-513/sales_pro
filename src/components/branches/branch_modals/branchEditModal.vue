<template>
    <div class="modal fade" id="editBranchModal" tabindex="-1" aria-labelledby="editBranchModalLabel" aria-modal="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header bg-soft-success" style="padding: 20px;">
                    <h5 class="modal-title">Edit Branch</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
            <form @submit.prevent="updateBranch">
            <div class="mb-3">
                <label for="branchName" class="form-label">Branch Name</label>
                <input type="text" class="form-control mb-1" v-model="branchName" required>
            </div>
            <div class="mb-3">
                <label for="location" class="form-label">Location</label>
                <input type="text" class="form-control" v-model="location" required>
            </div>
            <div class="mb-3">
                <label for="manager" class="form-label">Manager</label>
                <input type="text" class="form-control" id="manager-edit" required>
                <!-- <select id="" class="form-control"v-model="manager" required>
                     <option value="">Select Manager</option>
                     <option v-for="manager in managerList" :key="staff.id" :value="staff.id">{{ staff.first_name }} {{ staff.last_name }}</option>
                </select> -->
            </div>
            <button type="submit" id="btn_update_info" class="btn btn-success" @click="updateBranch()">Update</button>
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

    data() {
        return {
            branchId: '',
            branchName: '',
            location: '',
            secretary: '',
            selectedManager: '',
            managerList: [],
        };
    },
    watch: {
        selectedBranchId: {
            immediate: true,
            handler(newVal) {
                if (newVal) {
                    this.fetchBranch(newVal);
                }
            }
        }
    },

    methods: {
        fetchBranch(selectedBranchId) {
            axios.get(`/api/branches/${selectedBranchId}/`)
                .then(response => {
                    const branchDetails = response.data;
                    this.branchName = branchDetails.branch_name;
                    this.location = branchDetails.location;
                    this.secretary = branchDetails.secretary;
                })
                .catch(error => {
                    console.error('Error fetching branch:', error);
                });
        },

        updateBranch() {
            axios.put(`/api/branches/${this.selectedBranchId}/`, {
                branch_name: this.branchName,
                location: this.location,
                secretary: this.secretary
            })
            .then(response => {
                console.log(`Branch with ID ${this.selectedBranchId} updated successfully`, response.data);
                this.$emit('branchUpdated', response.data);
                $('#editBranchModal').modal('hide');

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

<!-- <script>
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
        editBranch() {
        const branchId = this.selectedBranchId;
        const branch_name = '';
        const location = '';
        const manager = '';

        axios.get(`/api/branches/${branchId}`)
        .then(response => {
            const branchDetails = response.data;
            return axios.put(`/api/branches/${branchId}/` , {
                branch_name: branchDetails.branch_name,
                location: branchDetails.location,
                manager: branchDetails.manager
            });
        })
        .then(response => {
            console.log(`the Branch with the ID ${branchId} has been Updated succesfully`, response.data);
            this.$emit('BranchUpdated', response.data);
            this.closeModal();

            setTimeout(() => {
                location.reload();
            }, 500);
        })
        .catch(error => {
            console.error('Error Updating Branch:', error);
        });
        }
    }
};
</script> -->