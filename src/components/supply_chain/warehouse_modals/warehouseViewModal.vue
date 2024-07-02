<template>
<div class="modal fade" id="viewWarehouseModal" tabindex="-1" aria-labelledby="viewWarehouseModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
        <div class="modal-header bg-soft-success" style="padding: 20px;">
        <h5 class="modal-title">Warehouse Information</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
        <form>
            <div class="mb-3">
                <label for="warehouseName" class="form-label">Warehouse Name</label>
                <input type="text" class="form-control mb-1" id="warehouse_name-view" readonly>
            </div>
            <div class="mb-3">
                <label for="location" class="form-label">Location</label>
                <input type="text" class="form-control" id="warehouse-location-view" readonly>
            </div>
            <div class="mb-3">
                <label for="manager" class="form-label">Caretaker</label>
                <input type="text" class="form-control" id="warehouse-caretaker-view" readonly>
                <!-- <select class="form-control" readonly>
                </select> -->
            </div>
        </form>
        </div>
    </div>
    </div>
</div>
</template>