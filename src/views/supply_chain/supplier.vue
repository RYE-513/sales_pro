<script setup>
import Supplier from '/src/components/supply_chain/supplierTable.vue'
import PageTitle from '/src/components/supply_chain/supplierPageTitle.vue'
import AddDataModal from '/src/components/supply_chain/supplier_modals/supplierAddModal.vue'
import ViewDataModal from '/src/components/supply_chain/supplier_modals/supplierViewModal.vue'
import EditDataModal from '/src/components/supply_chain/supplier_modals/supplierEditModal.vue'
</script>

<template>
  <PageTitle/>
  <div class="row">
    <div class="col-lg-12">
      <div class="card">
        <div class="card-header">
          <div class="d-flex align-items-center">
            <div class="flex-grow-1">
                <h6 class="card-title mb-0">Supplier List</h6>
            </div>
            <div class="flex-shrink-0">
                <ul class="list-inline card-toolbar-menu d-flex align-items-center mb-0">
                    <li class="list-inline-item">
                      <button type="button" class="btn btn-success btn-label waves-effect waves-light btn-sm" @click="openAddModal">
                        <i class="ri-add-circle-line label-icon align-middle fs-16 me-2"></i>Add Supplier
                      </button>
                    </li>
                </ul>
            </div>
        </div>
        </div>
        <div class="card-body">
          <Supplier/>
        </div>
      </div>
      <AddDataModal ref="addDataModal" @addSupplier="addSupplier" />
      <ViewDataModal ref="viewDataModal" />
      <EditDataModal ref="editDataModal" />
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
  },
  methods: {
    openAddModal() {
      this.$refs.addDataModal.openAddModal();
    },
    openViewModal() {
      this.$refs.viewDataModal.openViewModal(); 
    },
    openEditModal() {
      this.$refs.editDataModal.openEditModal();
    },
    
    // ADD SUPPLIER
    addSupplier(SupplierData) {
      // Handle adding new branch here
      console.log('Adding new supplier:', SupplierData);
    }
  }
});
</script>