<template>
    <div class="modal fade" id="viewSupplierModal" tabindex="-1" aria-labelledby="viewSupplierModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
            <div class="modal-header bg-soft-success" style="padding: 15px;">
                <h5 class="modal-title">Supplier Information</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-view" name="id-view" readonly hidden>
                    <div class="row">
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="supplier-name-view" class="form-label">Supplier Name</label>
                                <input type="text" class="form-control" id="supplier-name-view" name="supplier-name-view" readonly>
                            </div>
                        
                            <div class="col-md-6">
                                <label for="supplier-location-view" class="form-label">Location</label>
                                <input type="text" class="form-control" id="supplier-location-view" name="supplier-location-view" readonly>
                            </div>
                        </div>

                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="supplier-contact_number-view" class="form-label">Contact Number</label>
                                <input type="text" class="form-control" id="supplier-contact_number-view" name="supplier-contact_number-view" readonly>
                            </div>  
                        
                            <div class="col-md-6">
                                <label for="supplier-contact_person-view" class="form-label">Contact Person</label>
                                <input type="text" class="form-control" id="supplier-contact_person-view" name="supplier-contact_person-view" readonly>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
</template>
