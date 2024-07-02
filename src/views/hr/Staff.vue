<script setup>
  import Staff from '/src/components/hr/staffTable.vue'
  import PageTitle from '/src/components/hr/staffPageTitle.vue'
  import AddDataModal from '/src/components/hr/staff_modals/staffAddModal.vue'
  import ViewDataModal from '/src/components/hr/staff_modals/staffViewModal.vue'
  import EditDataModal from '/src/components/hr/staff_modals/staffEditModal.vue'
  import DeleteDataModal from '/src/components/hr/staff_modals/staffDeleteModal.vue'
  import RecoverDataModal from '/src/components/hr/staff_modals/staffRecoverModal.vue'
</script>

<template>
  <PageTitle/>
  <div class="row">
    <div class="col-lg-12">
      <div class="card">
        <div class="card-header">
          <div class="d-flex align-items-center">
            <div class="flex-grow-1">
                <h6 class="card-title mb-0">Staff List</h6>
            </div>
            <div class="flex-shrink-0">
                <ul class="list-inline card-toolbar-menu d-flex align-items-center mb-0">
                    <li class="list-inline-item">
                      <button type="button" class="btn btn-success btn-label waves-effect waves-light btn-sm" @click="openAddModal">
                        <i class="ri-add-circle-line label-icon align-middle fs-16 me-2"></i>Add Staff
                      </button>
                    </li>
                </ul>
            </div>
        </div>
        </div>

        <div class="card-body">
          <Staff/>
        </div>

      </div>
      <AddDataModal ref="addDataModal" @addStaff="addStaff"/>
      <ViewDataModal ref="viewDataModal"/>
      <EditDataModal ref="editDataModal"/>
      <DeleteDataModal ref="deleteDataModal"/>
      <RecoverDataModal ref="recoverDataModal"/>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import AddDataModal from '/src/components/hr/staff_modals/staffAddModal.vue';

export default defineComponent({
  components: {
    AddDataModal,
    ViewDataModal,
    EditDataModal,
    DeleteDataModal,
    RecoverDataModal,
  },
  methods: {

  // ADD STAFF

  addStaff(staffData) {
    console.log('Adding new staff:', staffData);
  },

  // MODALS
  openAddModal() {
    this.$refs.addDataModal.openAddModal();
  },
  openViewModal() {
      this.$refs.viewDataModal.openViewModal(); 
  },
  openEditModal() {
    this.$refs.editDataModal.openEditModal();
  },
  openDeleteModal() {
    this.$refs.deleteDataModal.openDeleteModal();
  },
  openRecoverModal() {
    this.$refs.deleteDataModal.openRecoverModal();
  },

  }
});

</script>