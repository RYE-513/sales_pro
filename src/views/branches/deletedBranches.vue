<script setup>
  import deletedBranches from '/src/components/branches/deletedTable.vue'
  import PageTitle from '/src/components/branches/deletedPageTitle.vue'
  import ViewDataModal from '/src/components/branches/branch_modals/branchViewModal.vue'
  import RecoverDataModal from '/src/components/branches/branch_modals/branchRecoverModal.vue'
</script>

<template>
  <PageTitle/>
  <div class="row">
    <div class="col-lg-12">
      <div class="card">
        <div class="card-header">
          <div class="d-flex align-items-center">
            <div class="flex-grow-1">
                <h6 class="card-title mb-0">Deleted Branch List</h6>
            </div>
            <div class="flex-shrink-0">
            </div>
        </div>
        </div>
        <div class="card-body">
          <deletedBranches/>
        </div>
      </div>
        <ViewDataModal ref="viewDataModal" />
        <RecoverDataModal ref="RecoverDataModal" />
    </div>
  </div>
  
</template>