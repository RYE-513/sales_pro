<script setup>
import Items from '/src/components/products/itemTable.vue'
import PageTitle from '/src/components/products/itemPageTitle.vue'
import AddDataModal from '/src/components/products/items_modals/itemAddModal.vue'
import ViewDataModal from '/src/components/products/items_modals/itemViewModal.vue'
import EditDataModal from '/src/components/products/items_modals/itemEditModal.vue'
import DeleteDataModal from '/src/components/products/items_modals/itemDeleteModal.vue'

</script>
<template>
  <PageTitle/>
  <div class="row">
    <div class="col-lg-12">
      <div class="card">
        <div class="card-header">
          <div class="d-flex align-items-center">
            <div class="flex-grow-1">
                <h6 class="card-title mb-0">Item List</h6>
            </div>
            <div class="flex-shrink-0">
                <ul class="list-inline card-toolbar-menu d-flex align-items-center mb-0">
                    <li class="list-inline-item">
                      <button type="button" class="btn btn-success btn-label waves-effect waves-light btn-sm" @click="openAddModal">
                        <i class="ri-add-circle-line label-icon align-middle fs-16 me-2"></i>Add Item
                      </button>
                    </li>
                </ul>
            </div>
        </div>
        </div>
        <div class="card-body">
          <Items/>
        </div>
      </div>
      <AddDataModal ref="addDataModal" @addItems="addItem" />
      <ViewDataModal ref="viewDataModal" />
      <EditDataModal ref="editDataModal" />
      <DeleteDataModal ref="deleteDataModal" />
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
  },
  methods: {
    openAddModal() {
      this.$refs.addDataModal.openModal();
    },
    openViewModal() {
    this.$refs.viewDataModal.openModal();
    },
    openEditModal() {
    this.$refs.editDataModal.openModal();
    },
    openDeleteModal() {
    this.$refs.deleteDataModal.openModal();
    },
    addItem(itemsData) {
      // Handle adding new branch here
      console.log('Adding new item:', itemsData);
    }
  }
});
</script>