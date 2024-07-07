<template>
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
    <tr v-for= "warehouse in warehouses" :key="warehouse.id">
      <td style="vertical-align: middle;">{{ warehouse.warehouse_name }}</td>
      <td style="vertical-align: middle;">{{ warehouse.location }}</td>
      <td style="vertical-align: middle;">{{ warehouse.caretaker }}</td>
      <td class="text-center"> {{ warehouse.status }}
      </td>

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
              <button type="button" class="dropdown-item editbtn" data-bs-toggle="modal" data-bs-target="#editWarehouseModal" @click="editWarehouse(warehouse)">
                <i class="ri-pencil-line align-bottom me-2 text-muted"></i>Edit
              </button>
            </li>

            <li>
              <button type="button" class="dropdown-item deletebtn" data-bs-toggle="modal" data-bs-target="#deleteWarehousehModal" @click="deleteWarehouse(warehouse)">
                <i class="ri-delete-bin-2-line align-bottom me-2 text-muted"></i>Delete
              </button>
            </li>

            <!-- <li>
              <button type="button" class="dropdown-item recoverbtn" data-bs-toggle="modal" data-bs-target="#recoverWarehouseModal" @click="recoverWarehouse">
                <i class="ri-save-3-fill align-bottom me-2 text-muted"></i>Recover
              </button>
            </li> -->
          </ul>

        </div>
      </td>
    </tr>
  </tbody>
</table>
<editModal :selectedWarehouseId="selectedWarehouseId" ref="editModalRef" />
<deleteModal :selectedWarehouseId="selectedWarehouseId" ref="deleteModalRef" />
</template>

<script>
import axios from 'axios';
import editModal from './warehouse_modals/warehouseEditModal.vue';
import deleteModal from './warehouse_modals/warehouseDeleteModal.vue';
  export default {
    components: {
      editModal,
      deleteModal
    },
    data(){
      return {
        warehouses: [],
        selectedWarehouseId: null,
      }
    },
    mounted() {
      this.fetchWarehouses();
    },
  
    methods: {
      fetchWarehouses() {
        axios.get('http://restful.localhost:8000/api/warehouses/')
          .then(response => {
            this.warehouses = response.data.filter(warehouse => warehouse.status !== 'Deleted')
          })
          .catch(error => {
            console.error('Error fetching data: ', error);
          });
      },
  
      viewWarehouse(warehouse) {
        const warehouseId = warehouse.id;
        console.log(warehouseId);
        // @ts-ignore
          $('#viewWarehouseModal').modal('show');
          $('#warehouse_name-view').val(warehouse.warehouse_name);
          $('#warehouse-location-view').val(warehouse.location);
          $('#warehouse-caretaker-view').val(warehouse.caretaker);
        },
        editWarehouse(warehouse) {
        const warehouseId = warehouse.id;
        console.log(warehouseId);
        this.selectedWarehouseId = warehouseId;
        // @ts-ignore
          $('#editWarehouseModal').modal('show');
          $('#warehouse_name-edit').val(warehouse.warehouse_name);
          $('#warehouse-location-edit').val(warehouse.location);
          $('#warehouse-caretaker-edit').val(warehouse.caretaker);
        },
        deleteWarehouse(warehouse) {
        const warehouseId = warehouse.id;
        console.log(warehouseId);
        this.selectedWarehouseId = warehouseId;
        // @ts-ignore
          $('#deleteWarehousehModal').modal('show');
          $('#warehouse_name-delete').val(warehouse.warehouse_name);
          $('#warehouse-location-delete').val(warehouse.location);
          $('#warehouse-caretaker-delete').val(warehouse.caretaker);
        },
    },
  };
</script>