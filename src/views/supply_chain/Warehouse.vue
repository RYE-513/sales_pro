<script setup>
import Warehouse from '/src/components/supply_chain/warehouseTable.vue'
import PageTitle from '/src/components/supply_chain/warehousePageTitle.vue'
import AddDataModal from '/src/components/supply_chain/warehouse_modals/warehouseAddModal.vue'
import ViewDataModal from '/src/components/supply_chain/warehouse_modals/warehouseViewModal.vue'
import EditDataModal from '/src/components/supply_chain/warehouse_modals/warehouseEditModal.vue'
import DeleteDataModal from '/src/components/supply_chain/warehouse_modals/warehouseDeleteModal.vue'
import RecoverDataModal from '/src/components/supply_chain/warehouse_modals/warehouseRecoverModal.vue'
</script>

<template>
<PageTitle/>
<div class="row">
    <div class="col-lg-12">
    <div class="card">
        <div class="card-header">
        <div class="d-flex align-items-center">
            <div class="flex-grow-1">
                <h6 class="card-title mb-0">Warehouse List</h6>
            </div>
            <div class="flex-shrink-0">
                <ul class="list-inline card-toolbar-menu d-flex align-items-center mb-0">
                    <li class="list-inline-item">
                    <button type="button" class="btn btn-success btn-label waves-effect waves-light btn-sm" @click="openAddModal">
                        <i class="ri-add-circle-line label-icon align-middle fs-16 me-2"></i>Add Warehouse
                    </button>
                    </li>
                </ul>
            </div>
        </div>
        </div>
        <div class="card-body">
        <Warehouse/>
        </div>
    </div>
    <AddDataModal ref="addDataModal" @addWarehouse="addWarehouse" />
    <ViewDataModal ref="viewDataModal" />
    <EditDataModal ref="editDataModal" />
    <DeleteDataModal ref="deleteDataModal" />
    <RecoverDataModal ref="RecoverDataModal" />
    </div>
</div>

</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  components: {
    AddDataModal,
    ViewDataModal,
    EditDataModal,
    DeleteDataModal,
    RecoverDataModal,
  },

  methods: {

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
    this.$refs.recoverDataModal.openRecoverModal();
  },

    // ADD WAREHOUSE
    addWarehouse(warehouseData) {
      // Handle adding new branch here
      console.log('Adding new warehouse:', warehouseData);
    }
  }
});
</script>