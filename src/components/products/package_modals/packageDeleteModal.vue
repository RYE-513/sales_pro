<template>
    <div class="modal fade" id="deletePackageModal" tabindex="-1" aria-labelledby="deletePackageModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-md">
        <div class="modal-content">
            <div class="modal-header bg-soft-danger" style="padding: 15px;">
                <h5 class="modal-title" id="disablePackageModalLabel">Disable Package</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
                            <div class="modal-body">
                                <p>Are you sure you want to disable this Package?</p>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                                <form id="disablePackageForm" method="post">
                                    <input type="hidden" name="package_id" id="package_id_input" value="">
                                    <button type="submit" class="btn btn-danger" id="confirmPackageDisableButton">Disable</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            
</template>

