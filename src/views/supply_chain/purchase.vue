<script setup>
import Purchase from '/src/components/supply_chain/purchaseTable.vue'
import PageTitle from '/src/components/supply_chain/purchasePageTitle.vue'
import ViewDataModal from '/src/components/supply_chain/purchase_modals/purchaseViewModal.vue'
import EditDataModal from '/src/components/supply_chain/purchase_modals/purchaseEditModal.vue'
</script>
<template>
    <PageTitle/>
    <div class="row">
        <div class="col-lg-12">
            <div class="card">
                <div class="card-header">
                    <div class="d-flex align-items-center">
                        <div class="flex-grow-1">
                            <h6 class="card-title mb-0">Purchase</h6>
                        </div>
                        <div class="flex-shrink-0">
                            <ul class="list-inline card-toolbar-menu d-flex align-items-center mb-0">
                                <li class="list-inline-item">
                                    <a href="/addpurchase" class="btn btn-success btn-label waves-effect waves-light btn-sm" style="font-size: 11px; width: 140px; height: 24px">
                                        <i class="ri-add-circle-line label-icon align-middle fs-16 me-2"></i>Add Purchase
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="card-body">
                    <Purchase/>
                </div>
            </div>
            <ViewDataModal ref="viewDataModal" />
            <EditDataModal ref="editDataModal" />
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    components: {
        ViewDataModal,
        EditDataModal
    },
    methods: {
        openViewModal() {
            this.$refs.viewDataModal.openViewModal();
        },
        openEditModal() {
            this.$refs.editDataModal.openEditModal();
        }
    }
})
</script>