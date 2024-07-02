<template>
    <div class="modal fade" id="recoverSupplyRequestModal" tabindex="-1" aria-labelledby="recoverSupplyRequestModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
        <div class="modal-header bg-soft-warning" style="padding: 20px;">
            <h5 class="modal-title">Recover Supply Request</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <form>
            <div class="row mb-3">
                <div class="col-md-6">
                    <label for="req_num" class="form-label" required>Request Number</label>
                    <input type="number" class="form-control" id="req_num-recover" name="req_num" readonly>
                </div>
                <div class="col-md-6">
                <label for="staff" class="form-label">Staff</label>
                <input type="text" class="form-control" id="staffsupply-recover" readonly>
                <!-- <select class="form-control" required>
                    <option value="">Select Staff</option>
                </select> -->
                </div>
            </div>
            <div class="row mb-3">
            <div class="col-md-6">
                <label for="manager" class="form-label">Branch</label>
                <input type="text" class="form-control" id="branchsupply-recover" readonly>
                <!-- <select class="form-control" required>
                    <option value="">Select Branch</option>
                </select> -->
            </div>
            <div class="col-md-6">
                <label for="description" class="form-label">Date Requested</label>
                <!-- <datepicker format="yyyy-MM-dd" input-class="form-control" required></datepicker> -->
                <input type="date" class="form-control" id="daterequestsupply-recover" name="date_requested" readonly/>
            </div>
            </div>
            <div class="row mb-3">
            <div class="col-md-6">
                <label for="staff" class="form-label">Driver</label>
                <input type="text" class="form-control" id="driver-recover" readonly>
                <!-- <select class="form-control" required>
                    <option value="">Select Driver</option>
                </select> -->
                </div>
                <div class="col-md-6">
                    <label for="description" class="form-label">Truck</label>
                    <input type="text" class="form-control" id="driver_truck-recover" name="driver_truck" readonly/>
                </div>
            </div>
            <div class="col-md-12">
                <label for="description" class="form-label">Date Delivered</label>
                <!-- <datepicker format="yyyy-MM-dd" input-class="form-control" required></datepicker> -->
                <input type="date" class="form-control" id="datedeliveredsupply-recover" name="date_requested" readonly/>
            </div>
            <br>
            <div>
                <button type="button" id="btn_update_info" class="btn btn-warning btn-block" @click="recoverSupplyRequest()">Recover</button>
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
    props: ['selectedSupplyReqId'],

    methods: {
    openAddModal() {
    $(this.$refs.modal).modal('show');
    },
    closeModal() {
    $(this.$refs.modal).modal('hide');
    },

    recoverSupplyRequest() {
    const supplyreqId = this.selectedSupplyReqId;
    const newStatus = 'Active';
    axios.get(`/api/supplyreqs/${supplyreqId}`)
        .then(response => {
            const supplyreqsDetails = response.data;
            return axios.put(`/api/supplyreqs/${supplyreqId}/`, {
                req_num: supplyreqsDetails.req_num,
                staff: supplyreqsDetails.staff,
                branch_name: supplyreqsDetails.branch_name,
                date_requested: supplyreqsDetails.date_requested,
                driver_staff: supplyreqsDetails.driver_staff,
                driver_truck: supplyreqsDetails.driver_truck,
                date_delivered: supplyreqsDetails.date_delivered,
                status: newStatus
            });
        })
        .then(response => {
            console.log(`Status of the Supply Request with ID ${supplyreqId} changed successfully`, response.data);
            this.$emit('SupplyRequestRecover', response.data);
            this.closeModal();
            
            setTimeout(() => {
                location.reload();
            }, 500);
        })
        .catch(error => {
            console.error('Error recover Supply Request:', error);
        });
        }
    }
};
</script>