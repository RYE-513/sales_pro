<script setup>
  import deletedHR from '/src/components/hr/deletedTable.vue'
  import PageTitle from '/src/components/hr/deletedPageTitle.vue'
  import ViewDataModal from '/src/components/hr/role_modals/rolesViewModal.vue'
  import RecoverRolesDataModal from '/src/components/hr/role_modals/rolesRecoverModal.vue'
  import ViewStaffModal from '/src/components/hr/staff_modals/staffViewModal.vue'
  import RecoverStaffDataModal from '/src/components/hr/staff_modals/staffRecoverModal.vue'
</script>

<template>
  <PageTitle/>
  <div class="row">
    <div class="col-lg-12">
      <div class="card">
        <div class="card-body">
          <deletedHR/>
        </div>
      </div>
      <ViewDataModal ref="viewDataModal" />
      <RecoverRolesDataModal ref="recoverRolesDataModal"/>
      <ViewStaffModal ref="ViewStaffModal"/>
      <RecoverStaffDataModal ref="recoverStaffDataModal"/>
    </div>
  </div>
</template>