<template>
    <div class="modal fade" id="viewItemsModal" tabindex="-1" aria-labelledby="viewItemsModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header bg-soft-success" style="padding: 15px;">
                <h5 class="modal-title">Items Information</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-view" name="id-view" readonly hidden>
                    <div class="row">
                        <div class=" mb-3">
                            <label for="items-name-view" class="form-label">Items</label>
                            <input type="text" class="form-control" id="items-name-view" name="items-name-view" readonly>
                        </div>
                </div>
                </form>
            </div>
        </div>
    </div>
</div>
</template>
