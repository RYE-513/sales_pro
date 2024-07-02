<template>
    <div class="modal fade" id="viewProductsModal" tabindex="-1" aria-labelledby="viewProductsModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
            <div class="modal-header bg-soft-success" style="padding: 15px;">
                <h5 class="modal-title">Products Information</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-view" name="id-view" readonly hidden>
                    <div class="row">
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="product-name-view" class="form-label">Products Name</label>
                                <input type="text" class="form-control" id="product-name-view" name="product-name-view" readonly>
                            </div>
                        
                            <div class="col-md-6">
                                <label for="product-category-view" class="form-label">Category</label>
                                <input type="text" class="form-control" id="product-category-view" name="product-category-view" readonly>
                            </div>
                        </div>

                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="product-package-view" class="form-label">Package</label>
                                <input type="text" class="form-control" id="product-package-view" name="product-package-view" readonly>
                            </div>  
                        
                            <div class="col-md-6">
                                <label for="product-price-view" class="form-label">Price</label>
                                <input type="text" class="form-control" id="product-price-view" name="product-price-view" readonly>
                            </div>
                        </div>
                    
                </div>
                </form>
            </div>
        </div>
    </div>
</div>
</template>
