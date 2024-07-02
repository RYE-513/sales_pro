<template>
    <div class="modal fade" id="deleteCategoryModal" tabindex="-1" aria-labelledby="deleteCategoryModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-md">
        <div class="modal-content">
            <div class="modal-header bg-soft-danger" style="padding: 15px;">
                <h5 class="modal-title" id="disableCategoryModalLabel">Disable Category</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
                            <div class="modal-body">
                                <p>Are you sure you want to disable this Category?</p>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                                <form id="disableCategoryForm" method="post">
                                    <input type="hidden" name="category_id" id="category_id_input" value="">
                                    <button type="submit" class="btn btn-danger" id="confirmCategoryDisableButton">Disable</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            
</template>

