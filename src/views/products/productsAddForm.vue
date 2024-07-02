<script setup>
    import ProductsDataModal from '/src/components/products/productsAddForm.vue'
</script>
<template>
    <div class="row">
        <div class="col-12">
            <div class="page-title-box d-sm-flex align-items-center justify-content-between">
                <h4 class="mb-sm-0">Products Order Information</h4>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-lg-12">
            <div class="card">
                <div class="card-body">
                    <ProductsDataModal/>
                </div>
            </div>
        </div>
    </div>
</template>