
<template>
    <div class="modal fade" id="viewRolesModal" tabindex="-1" aria-labelledby="viewRolesModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header bg-soft-success" style="padding: 20px;">
                <h5 class="modal-title">Role Information</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-view" name="id-view" readonly hidden>
                        <div class="mb-3 row">
                            <div class="md-12">
                                <label for="role-name-view" class="form-label">Role Name</label>
                                <input type="text" class="form-control" id="role_name-view" name="role_name-view" readonly>
                            </div>
                        </div>
                        
                        <div class="mb-3 row">
                            <div class="md-12">
                                <label for="description-view" class="form-label">Description</label>
                                <input type="text" class="form-control" id="description-view" name="description-view" readonly>
                            </div>
                        </div>

                        <div class="mb-3 row">
                            <div class="md-12">
                                <label for="status-view" class="form-label">Status</label>
                                <input type="text" class="form-control" id="status-view" name="status-view" readonly>
                            </div>
                        </div>
                        
                </form>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {
    props: ['selectedRole']
};
</script>