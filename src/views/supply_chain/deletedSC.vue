<script setup>
  import deletedSC from '/src/components/supply_chain/deletedTable.vue'
  import PageTitle from '/src/components/supply_chain/deletedPageTitle.vue'
  import ViewWarehouse from '/src/components/supply_chain/warehouse_modals/warehouseViewModal.vue'
  import RecoverWarehouse from '/src/components/supply_chain/warehouse_modals/warehouseViewModal.vue'
  import ViewSupplyReq from '/src/components/supply_chain/supply-reqs_modals/supplyreqsViewModal.vue'
  import RecoverSupplyReq from '/src/components/supply_chain/supply-reqs_modals/supplyreqsRecoverModal.vue'
</script>

<template>
  <PageTitle/>
  <div class="row">
    <div class="col-lg-12">
      <div class="card">
        <div class="card-body">
          <deletedSC/>
        </div>
      </div>
      <ViewWarehouse ref="viewWareHose" />
      <RecoverWarehouse ref="RecoverWarehouse" />
      <ViewSupplyReq ref="ViewSupplyReq" />
      <RecoverSupplyReq ref="RecoverSupplyReq" />
    </div>
  </div>
</template>