<script setup>
    import PurchaseDataModal from '/src/components/supply_chain/purchaseAddForm.vue'
</script>
<template>
    <div class="row">
        <div class="col-12">
            <div class="page-title-box d-sm-flex align-items-center justify-content-between">
                <h4 class="mb-sm-0">Purchase Order Information</h4>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-lg-12">
            <div class="card">
                <div class="card-body">
                    <PurchaseDataModal/>
                </div>
            </div>
        </div>
    </div>
</template>