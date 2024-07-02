<template>
    <div class="modal fade" id="viewPurchaseModal" tabindex="-1" aria-labelledby="viewPurchaseModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
            <div class="modal-header bg-soft-success" style="padding: 15px;">
                <h5 class="modal-title">Purchase Information</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>  
            <div class="modal-body">
                <form>
                    <input type="" id="id-view" name="id-view" readonly hidden>
                    <div class="row">
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="purchase-name-view" class="form-label">Supplier Name</label>
                                <input type="text" class="form-control" id="purchase-view" name="purchase-name-view" readonly>
                            </div>
                        
                            <div class="col-md-6">
                                <label for="po-view" class="form-label">PO Number</label>
                                <input type="text" class="form-control" id="po-view" name="po-view" readonly>
                            </div>
                        </div>

                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="deliveryaddress-view" class="form-label">Delivery Address</label>
                                <input type="text" class="form-control" id="deliveryaddress-view" name="deliveryaddress-view" readonly>
                            </div>  
                        
                            <div class="col-md-6">
                                <label for="deliverydate-view" class="form-label">Delivery Date</label>
                                <input type="text" class="form-control" id="deliverydate-view" name="deliverydate-view" readonly>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
</template>