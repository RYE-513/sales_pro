<template>
  <div class="modal fade" id="BranchModal" tabindex="-1" aria-labelledby="viewBranchModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header bg-soft-success" style="padding: 20px;">
          <h5 class="modal-title">Branch Information</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="branchName" class="form-label">Branch Name</label>
              <input type="text" class="form-control mb-1" id="branch_name-view" readonly>
            </div>
            <div class="mb-3">
              <label for="location" class="form-label">Location</label>
              <input type="text" class="form-control" id="location-view" readonly>
            </div>
            <div class="mb-3">
              <label for="manager" class="form-label">Manager</label>
              <input type="text" class="form-control" id="manager-view" readonly>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>