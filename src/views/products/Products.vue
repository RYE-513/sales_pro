<script setup>
    import Products from '/src/components/products/productTable.vue'
    import PageTitle from '/src/components/products/productPageTitle.vue'
    import ViewDataModal from '/src/components/products/products_modals/productViewModal.vue'
    import EditDataModal from '/src/components/products/products_modals/productEditModal.vue'
    import DeleteDataModal from '/src/components/products/products_modals/productDeleteModal.vue'
    // import RecoverDataModal from '/src/components/products/products_modals/productRecoverModal.vue'
</script>

<template>

    <PageTitle/>
    <div class="row">
        <div class="col-lg-12">
            <div class="card">
                <div class="card-header">
                    <div class="d-flex align-items-center">
                        <div class="flex-grow-1">
                            <h6 class="card-title mb-0">Products List</h6>
                        </div>
                        <div class="flex-shrink-0">
                            <ul class="list-inline card-toolbar-menu d-flex align-items-center mb-0">
                                <li class="list-inline-item">
                                    <a href="/addproducts" class="btn btn-success btn-label waves-effect waves-light btn-sm" style="font-size: 11px; width: 140px; height: 24px">
                                        <i class="ri-add-circle-line label-icon align-middle fs-16 me-2"></i>Add Products
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="card-body">
                    <Products/>
                </div>
            </div>
                <ViewDataModal ref="viewDataModal" /> <!-- @addProduct="addProduct"-->
                <EditDataModal ref="editDataModal" />
                <DeleteDataModal ref="deleteDataModal" />
            </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
components: {
    // ViewDataModal,
    // EditDataModal,
    // DeleteDataModal,
    // RecoverDataModal,
},

methods: {

    openViewModal() {
    this.$refs.ViewDataModal.openModal();
    },

    openViewModal() {
    this.$refs.ViewDataModal.openModal();
    },
    
    openEditModal() {
    this.$refs.EditDataModal.openModal();
    },
    
    openDeleteModal() {
    this.$refs.DeleteDataModal.openModal();
    },
},
});
</script>
