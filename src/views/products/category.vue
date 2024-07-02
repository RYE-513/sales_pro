<script setup>
import Category from '/src/components/products/categoryTable.vue'
import PageTitle from '/src/components/products/categoryPageTitle.vue'
import AddDataModal from '/src/components/products/category_modals/categoryAddModal.vue'
import ViewDataModal from '/src/components/products/category_modals/categoryViewModal.vue'
import EditDataModal from '/src/components/products/category_modals/categoryEditModal.vue'
import DeleteDataModal from '/src/components/products/category_modals/categoryDeleteModal.vue'
</script>
<template>
<PageTitle/>
<div class="row">
    <div class="col-lg-12">
    <div class="card">
        <div class="card-header">
        <div class="d-flex align-items-center">
            <div class="flex-grow-1">
                <h6 class="card-title mb-0">Category List</h6>
            </div>
            <div class="flex-shrink-0">
                <ul class="list-inline card-toolbar-menu d-flex align-items-center mb-0">
                    <li class="list-inline-item">
                    <button type="button" class="btn btn-success btn-label waves-effect waves-light btn-sm" @click="openAddModal">
                        <i class="ri-add-circle-line label-icon align-middle fs-16 me-2"></i>Add Category
                    </button>
                    </li>
                </ul>
            </div>
        </div>
        </div>
        <div class="card-body">
        <Category/>
        </div>
    </div>
    <AddDataModal ref="addDataModal" @addCategory="addCategory" />
    <ViewDataModal ref="ViewDataModal" />
    <EditDataModal ref="EditDataModal" />
    <DeleteDataModal ref="deleteDataModal" />
    </div>
</div>
</template>
<script>
import { defineComponent } from 'vue';

export default defineComponent({
components: {
    AddDataModal,
    EditDataModal,
    ViewDataModal,
    DeleteDataModal,
},
methods: {
    openAddModal() {
    this.$refs.addDataModal.openAddModal();
    },
    openEditModal() {
    this.$refs.EditDataModal.openEditModal();
    },
    openViewModal() {
    this.$refs.ViewDataModal.openViewModal();
    },
    openDeleteModal() {
    this.$refs.deleteDataModal.openModal();
    },
    addItem(itemData) {
      // Handle adding new branch here
    console.log('Adding new item:', itemsData);
    }
}
});
</script>