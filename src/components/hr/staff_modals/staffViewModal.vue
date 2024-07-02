<template>
    <div class="modal fade" id="viewStaffModal" tabindex="-1" aria-labelledby="viewStaffModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
            <div class="modal-header bg-soft-success" style="padding: 20px;">
                <h5 class="modal-title">Staff Information</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-view" name="id-view" readonly hidden>
                    <div class="mb-3 row">
                        <div class="col-md-6">
                            <label for="firstName" class="form-label">First Name</label>
                            <input type="text" class="form-control mb-1" id="first_name-view" name="first_name-view" readonly>
                        </div>

                        <div class="col-md-6">
                            <label for="lastName" class="form-label">Last Name</label>
                            <input type="text" class="form-control mb-1" id="last_name-view" name="last_name-view" readonly>
                        </div>
                    </div>
        
                    <div class="mb-3 row">
                        <div class="col-md-6">
                            <label for="mobile_no" class="form-label">Contact Number</label> 
                            <div class="input-group"> 
                                <span class="input-group-text">(+63)</span> 
                                <input type="text" class="form-control" id="mobile_no-view" name="mobile_no-view" readonly> 
                            </div>
                        </div> 
        
                        <div class="col-md-6">
                            <label for="email" class="form-label">Email Address</label>
                            <input type="email" class="form-control" id="email-view" name="email-view" readonly>
                        </div>
        
                    </div>

                    <div class="mb-3">
                        <label for="roles" class="form-label">Roles</label>
                        <input type="roles" class="form-control" id="roles-view" name="roles-view" readonly>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
</template>

<script>

</script>
