<script>
import axios from 'axios';
import recoverWarehouseModal from './warehouse_modals/warehouseRecoverModal.vue'
import recoverSupplyReqsModal from './supply-reqs_modals/supplyreqsRecoverModal.vue'
export default {
    components: {
      recoverWarehouseModal,
      recoverSupplyReqsModal,
    },
    data() {
      return {
        warehouses: [],
        supply_reqs: [],
        selectedWarehouseId: null,
        selectedSupplyReqId: null,
      };
    },
    mounted() {
      this.fetchData();
      this.fetchSupplyReq()
    },
    methods: {
    fetchData() {merge
      axios.get('http://merge.localhost:8000/api/warehouses/')
        .then(response => {
          this.warehouses = response.data.filter(warehouse => warehouse.status === 'Deleted');
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
    fetchSupplyReq() {
      axios.get('http://merge.localhost:8000/api/supplyreqs/')
        .then(response => {
          this.supply_reqs =response.data.filter(supply_req => supply_req.status === 'Deleted');
        })
    },
    viewWarehouse(warehouse) {
      $('#viewWarehouseModal').modal('show');
      $('#warehouse_name-view').val(warehouse.warehouse_name);
      $('#warehouse-location-view').val(warehouse.location);
      $('#warehouse-caretaker-view').val(warehouse.caretaker);
    },
    recoverWarehouse(warehouse) {
      const warehouseId = warehouse.id;
      console.log(warehouseId);
      this.selectedWarehouseId = warehouseId;
      $('#recoverWarehouseModal').modal('show');
      $('#warehouse_name-recover').val(warehouse.warehouse_name);
      $('#warehouse-location-recover').val(warehouse.location);
      $('#warehouse-caretaker-recover').val(warehouse.caretaker);
      },
    viewSupplyReqs(supply_reqs) {
      $('#viewSupplyRequestModal').modal('show');
      $('#req_num-view').val(supply_reqs.req_num);
      $('#staffsupply-view').val(supply_reqs.staff);
      $('#branchsupply-view').val(supply_reqs.branch);
      $('#daterequestsupply-view').val(supply_reqs.date_requested);
      $('#driver-view').val(supply_reqs.driver_staff);
      $('#driver_truck-view').val(supply_reqs.driver_truck);
      $('#datedeliveredsupply-view').val(supply_reqs.date_delivered);
      },
    recoverSupplyReqs(supply_reqs) {
      const supplyreqsId = supply_reqs.id;
      console.log(supplyreqsId);
      this.selectedSupplyReqId = supplyreqsId;
      $('#recoverSupplyRequestModal').modal('show');
      $('#req_num-recover').val(supply_reqs.req_num);
      $('#staffsupply-recover').val(supply_reqs.staff);
      $('#branchsupply-recover').val(supply_reqs.branch);
      $('#daterequestsupply-recover').val(supply_reqs.date_requested);
      $('#driver-recover').val(supply_reqs.driver_staff);
      $('#driver_truck-recover').val(supply_reqs.driver_truck);
      $('#datedeliveredsupply-recover').val(supply_reqs.date_delivered);
      },
  },
  };
  </script>
<template>
    <!-- DELETED WAREHOUSE TABLE -->
    <div class="flex-grow-1">
      <h6 class="card-title mb-0">Deleted Warehousing</h6>
      <br>
    </div>
    <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
      <thead class="table-light">
        <tr>
          <th width="20%" class="text-center">Warehouse Name</th>
          <th width="20%" class="text-center">Location</th>
          <th width="20%" class="text-center">Caretaker</th>
          <th width="10%" class="text-center">Status</th>
          <th width="10%" class="text-center">Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="warehouse in warehouses" :key="warehouse.id">
          <td>{{warehouse.warehouse_name}}</td>
          <td>{{warehouse.location}}</td>
          <td>{{warehouse.caretaker}}</td>
          <td>{{warehouse.status}}</td>
          <td class="text-center">
        <div class="dropdown d-inline-block">
          <button class="btn btn-soft-info btn-sm dropdown" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="vertical-align: middle;">Actions</button>
          <ul class="dropdown-menu dropdown-menu-end">
            <li>
              <button type="button" class="dropdown-item viewbtn" data-bs-toggle="modal" data-bs-target="#viewWarehouseModal" @click="viewWarehouse(warehouse)">
                <i class="ri-eye-fill align-bottom me-2 text-muted"></i>View
              </button>
            </li>
            <li>
              <button type="button" class="dropdown-item recoverbtn" data-bs-toggle="modal" data-bs-target="#recoverWarehouseModal" @click="recoverWarehouse(warehouse)">
                <i class="ri-save-3-fill align-bottom me-2 text-muted"></i>Recover
              </button>
            </li>
          </ul>
        </div>
        </td>
        </tr>
      </tbody>
    </table>
    <!-- DELETED SUPPLY REQUEST TABLE -->
    <div class="flex-grow-1">
      <h6 class="card-title mb-0">Deleted Supply Request</h6>
      <br>
    </div>
    <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
    <thead class="table-light">
      <tr>
        <th width="5%" class="text-center" style="font-size: 10px; vertical-align: middle;">Request Number</th>
        <th width="20%" class="text-center" style="vertical-align: middle;">Staff Name</th>
        <th width="20%" class="text-center" style="vertical-align: middle;">Branch Name</th>
        <th width="5%" class="text-center" style="font-size: 10px; vertical-align: middle;">Date Requested</th>
        <th width="15%" class="text-center" style="vertical-align: middle;">Driver</th>
        <th width="15%" class="text-center" style="vertical-align: middle;">Truck</th>
        <th width="5%" class="text-center" style="font-size: 10px; vertical-align: middle;">Date Delivered</th>
        <th width="10%" class="text-center" style="vertical-align: middle;">Status</th>
        <th width="15%" class="text-center" style="vertical-align: middle;">Action</th>
      </tr>
      </thead>
      <tbody>
        <tr v-for="supply_reqs in supply_reqs" :key="supply_reqs.id">
          <td style="vertical-align: middle;">{{supply_reqs.req_num}}</td>
          <td style="vertical-align: middle;">{{supply_reqs.staff}}</td>
          <td style="vertical-align: middle;">{{supply_reqs.branch}}</td>
          <td style="vertical-align: middle;">{{supply_reqs.date_requested}}</td>
          <td style="vertical-align: middle;">{{supply_reqs.driver_staff}}</td>
          <td style="vertical-align: middle;">{{supply_reqs.driver_truck}}</td>
          <td style="vertical-align: middle;">{{supply_reqs.date_delivered}}</td>
          <td class="text-center">{{supply_reqs.status}}
          </td>
        <td class="text-center">
        <div class="dropdown d-inline-block">
          <button class="btn btn-soft-info btn-sm dropdown" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="vertical-align: middle;">Actions</button>
          <ul class="dropdown-menu dropdown-menu-end">
            <li>
              <button type="button" class="dropdown-item viewbtn" data-bs-toggle="modal" data-bs-target="#viewSupplyRequestModal" @click="viewSupplyReqs(supply_reqs)">
                <i class="ri-eye-fill align-bottom me-2 text-muted"></i>View
              </button>
            </li>
            <li>
              <button type="button" class="dropdown-item recoverbtn" data-bs-toggle="modal" data-bs-target="#recoverSupplyRequestModal" @click="recoverSupplyReqs(supply_reqs)">
                <i class="ri-save-3-fill align-bottom me-2 text-muted"></i>Recover
              </button>
            </li>
          </ul>
        </div>
        </td>
        </tr>
      </tbody>
    </table>
    <recoverWarehouseModal :selectedWarehouseId="selectedWarehouseId" ref="recoverWarehoseModalRef" />
    <recoverSupplyReqsModal :selectedSupplyReqId="selectedSupplyReqId" ref="recoverSupplyReqsModal" />
</template>