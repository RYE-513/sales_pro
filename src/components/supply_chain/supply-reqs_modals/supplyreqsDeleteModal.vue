<template>
    <div class="modal fade" id="deleteSupplyRequestModal" tabindex="-1" aria-labelledby="deleteSupplyRequestModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
        <div class="modal-header bg-soft-danger" style="padding: 20px;">
            <h5 class="modal-title">Delete Supply Request</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <form>
            <div class="row mb-3">
                <div class="col-md-6">
                    <label for="req_num" class="form-label" required>Request Number</label>
                    <input type="number" class="form-control" id="req_num-delete" name="req_num" readonly>
                </div>
                <div class="col-md-6">
                <label for="staff" class="form-label">Staff</label>
                <input type="text" class="form-control" id="staffsupply-delete" readonly>
                <!-- <select class="form-control" required>
                    <option value="">Select Staff</option>
                </select> -->
                </div>
            </div>
            <div class="row mb-3">
            <div class="col-md-6">
                <label for="manager" class="form-label">Branch</label>
                <input type="text" class="form-control" id="branchsupply-delete" readonly>
                <!-- <select class="form-control" required>
                    <option value="">Select Branch</option>
                </select> -->
            </div>
            <div class="col-md-6">
                <label for="description" class="form-label">Date Requested</label>
                <!-- <datepicker format="yyyy-MM-dd" input-class="form-control" required></datepicker> -->
                <input type="date" class="form-control" id="daterequestsupply-delete" name="date_requested" readonly/>
            </div>
            </div>
            <div class="row mb-3">
            <div class="col-md-6">
                <label for="staff" class="form-label">Driver</label>
                <input type="text" class="form-control" id="driver-delete" readonly>
                <!-- <select class="form-control" required>
                    <option value="">Select Driver</option>
                </select> -->
                </div>
                <div class="col-md-6">
                    <label for="description" class="form-label">Truck</label>
                    <input type="text" class="form-control" id="driver_truck-delete" name="driver_truck" readonly/>
                </div>
            </div>
            <div class="col-md-12">
                <label for="description" class="form-label">Date Delivered</label>
                <!-- <datepicker format="yyyy-MM-dd" input-class="form-control" required></datepicker> -->
                <input type="date" class="form-control" id="datedeliveredsupply-delete" name="date_requested" readonly/>
            </div>
            <br>
            <div>
                <button type="button" id="btn_update_info" class="btn btn-danger btn-block" @click="deleteSupplyReq()">Delete</button>
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
    props: ['selectedSupplyReqsId'],

    methods: {
    openAddModal() {
    // @ts-ignore
    $(this.$refs.modal).modal('show');
    },
    closeModal() {
    // @ts-ignore
    $(this.$refs.modal).modal('hide');
    },

    deleteSupplyReq() {
    const supplyreqId = this.selectedSupplyReqsId;
    const newStatus = 'Deleted';
    
    axios.get(`/api/supplyreqs/${supplyreqId}`)
        .then(response => {
            const supplyRequestDetails = response.data;
            return axios.put(`/api/supplyreqs/${supplyreqId}/`, {
                req_num: supplyRequestDetails.req_num,
                staff: supplyRequestDetails.staff,
                branch_name: supplyRequestDetails.branch_name,
                date_requested: supplyRequestDetails.date_requested,
                driver_staff: supplyRequestDetails.driver_staff,
                driver_truck: supplyRequestDetails.driver_truck,
                date_delivered: supplyRequestDetails.date_delivered,
                status: newStatus
            });
        })
        .then(response => {
            console.log(`Status of the Supply Request with ID ${supplyreqId} changed successfully`, response.data);
            this.$emit('SupplyRequestDeleted', response.data);
            this.closeModal();
            
            setTimeout(() => {
                location.reload();
            }, 500);
        })
        .catch(error => {
            console.error('Error deleting Supply Request:', error);
        });
        }
    }
};
</script>