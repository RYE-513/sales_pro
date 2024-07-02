<template>
    <div class="modal fade" id="editSupplyRequestModal" tabindex="-1" aria-labelledby="editSupplyRequestModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
        <div class="modal-header bg-soft-success" style="padding: 20px;">
            <h5 class="modal-title">Edit Supply Request</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <form>
            <div class="row mb-3">
                <div class="col-md-6">
                    <label for="req_num" class="form-label" required>Request Number</label>
                    <input type="number" class="form-control" id="req_num-edit" name="req_num">
                </div>
                <div class="col-md-6">
                <label for="staff" class="form-label">Staff</label>
                <input type="text" class="form-control" id="staffsupply-edit">
                <!-- <select class="form-control" required>
                    <option value="">Select Staff</option>
                </select> -->
                </div>
            </div>
            <div class="row mb-3">
            <div class="col-md-6">
                <label for="manager" class="form-label">Branch</label>
                <input type="text" class="form-control" id="branchsupply-edit">
                <!-- <select class="form-control" required>
                    <option value="">Select Branch</option>
                </select> -->
            </div>
            <div class="col-md-6">
                <label for="description" class="form-label">Date Requested</label>
                <!-- <datepicker format="yyyy-MM-dd" input-class="form-control" required></datepicker> -->
                <input type="date" class="form-control" id="daterequestsupply-edit" name="date_requested"/>
            </div>
            </div>
            <div class="row mb-3">
            <div class="col-md-6">
                <label for="staff" class="form-label">Driver</label>
                <input type="text" class="form-control" id="driver-edit">
                <!-- <select class="form-control" required>
                    <option value="">Select Driver</option>
                </select> -->
                </div>
                <div class="col-md-6">
                    <label for="description" class="form-label">Truck</label>
                    <input type="text" class="form-control" id="driver_truck-edit" name="driver_truck"/>
                </div>
            </div>
            <div class="col-md-12">
                <label for="description" class="form-label">Date Delivered</label>
                <!-- <datepicker format="yyyy-MM-dd" input-class="form-control" required></datepicker> -->
                <input type="date" class="form-control" id="datedeliveredsupply-edit" name="date_requested"/>
            </div>
            <br>
            <div>
                <button type="button"class="btn btn-success">Update</button>
            </div>
            </form>
        </div>
        </div>
    </div>
    </div>
</template>