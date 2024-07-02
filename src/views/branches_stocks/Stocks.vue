<script setup>
import Sales from '/src/components/branches_stocks/stocksTable.vue'
import PageTitle from '/src/components/branches_stocks/stocksPageTitle.vue'
</script>


<template>
<PageTitle/>

<div class="row">
    <div class="col-lg-12">
    <div class="card">
        <div class="card-header">
        <div class="d-flex align-items-center">
            <div class="flex-grow-1">
                <h6 class="card-title mb-0">Stocks</h6>
            </div>
        </div>
        </div>

        <div class="card-body">
        <Sales/>
        </div>
    </div>
</div>

</div>

</template>