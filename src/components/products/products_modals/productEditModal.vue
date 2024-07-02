<template>
    <div class="modal fade" id="editProductsModal" tabindex="-1" aria-labelledby="editProductsModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
            <div class="modal-header bg-soft-success" style="padding: 15px;">
                <h5 class="modal-title">Edit Products</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-edit" name="id-edit" readonly hidden>
                    <div class="row">
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="product-name-edit" class="form-label">Products Name</label>
                                <input type="text" class="form-control" id="product-name-edit" name="product-name-edit" required>
                            </div>
                            <div class="col-md-6">
                                <label for="product-category-edit" class="form-label">Category</label>
                                <input type="text" class="form-control" id="product-category-edit" name="product-category-edit" required>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="product-package-edit" class="form-label">Package</label>
                                <input type="text" class="form-control" id="product-package-edit" name="product-package-edit" required>
                            </div>  
                            <div class="col-md-6">
                                <label for="product-price-edit" class="form-label">Price</label>
                                <input type="text" class="form-control" id="product-price-edit" name="product-price-edit" required>
                            </div>
                        </div>
                        <div class="col-lg-12">
                            <button type="submit" class="btn btn-success">Update</button>
                    </div>
                </div>
                </form>
            </div>
        </div>
    </div>
</div>
</template>

<script>
</script>