<template>
    <div class="modal fade" id="viewPackageModal" tabindex="-1" aria-labelledby="viewPackageModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header bg-soft-success" style="padding: 15px;">
                <h5 class="modal-title">Package Information</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-edit" name="id-edit" readonly hidden>
                        <div class=" mb-3">
                            <label for="product-package-edit" class="form-label">Package</label>
                            <input type="text" class="form-control" id="product-package-view" name="product-package-view" readonly>
                        </div>
                </form> 
                </div>
            </div>
        </div>
    </div>
</template>