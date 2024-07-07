<template>
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
        <tr v-for= "supply_reqs in supply_reqs" :key="supply_reqs.id">
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
                  <button type="button" class="dropdown-item viewbtn" data-bs-toggle="modal" data-bs-target="#viewSupplyRequestModal" @click="viewSupplyRequest(supply_reqs)">
                    <i class="ri-eye-fill align-bottom me-2 text-muted"></i>View
                  </button>
                </li>
                <li>
                  <button type="button" class="dropdown-item editbtn" data-bs-toggle="modal" data-bs-target="#editSupplyRequestModal" @click="editSupplyRequest(supply_reqs)">
                    <i class="ri-pencil-line align-bottom me-2 text-muted"></i>Edit
                  </button>
                </li>
                <li>
                  <button type="button" class="dropdown-item deletebtn" data-bs-toggle="modal" data-bs-target="#deleteSupplyRequestModal" @click="deleteSupplyRequest(supply_reqs)">
                    <i class="ri-delete-bin-2-line align-bottom me-2 text-muted"></i>Delete
                  </button>
                </li>
              </ul>
            </div>
          </td>
        </tr>
      </tbody>
</table>
<deleteModal :selectedSupplyReqsId="selectedSupplyReqsId" ref="deleteModalRef" />
</template>

<script>
import axios from 'axios';
import deleteModal from './supply-reqs_modals/supplyreqsDeleteModal.vue'
export default {
  components: {
    deleteModal
  },
  data() {
    return {
      supply_reqs: [],
      selectedSupplyReqsId: null,
    };
  },
  mounted() {
    this.fetchSupplyReqs();
  },
  methods: {
    fetchSupplyReqs() {
      axios.get('http://restful.localhost:8000/api/supplyreqs/')
        .then(response => {
          // this.supply_reqs = response.data;
          this.supply_reqs = response.data.filter(supply_reqs => supply_reqs.status !== 'Deleted');
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
      },
      viewSupplyRequest(supply_reqs) {
        $('#viewSupplyRequestModal').modal('show');
        $('#req_num-view').val(supply_reqs.req_num);
        $('#staffsupply-view').val(supply_reqs.staff);
        $('#branchsupply-view').val(supply_reqs.branch);
        $('#daterequestsupply-view').val(supply_reqs.date_requested);
        $('#driver-view').val(supply_reqs.driver_staff);
        $('#driver_truck-view').val(supply_reqs.driver_truck);
        $('#datedeliveredsupply-view').val(supply_reqs.date_delivered);
      },
      editSupplyRequest(supply_reqs) {
        const supplyreqId = supply_reqs.id;
        this.selectedSupplyReqsId = supplyreqId;
        $('#editSupplyRequestModal').modal('show');
        $('#req_num-edit').val(supply_reqs.req_num);
        $('#staffsupply-edit').val(supply_reqs.staff);
        $('#branchsupply-edit').val(supply_reqs.branch);
        $('#daterequestsupply-edit').val(supply_reqs.date_requested);
        $('#driver-edit').val(supply_reqs.driver_staff);
        $('#driver_truck-edit').val(supply_reqs.driver_truck);
        $('#datedeliveredsupply-edit').val(supply_reqs.date_delivered);
      },
      deleteSupplyRequest(supply_reqs) {
        const supplyreqId = supply_reqs.id;
        this.selectedSupplyReqsId = supplyreqId;
        $('#deleteSupplyRequestModal').modal('show');
        $('#req_num-delete').val(supply_reqs.req_num);
        $('#staffsupply-delete').val(supply_reqs.staff);
        $('#branchsupply-delete').val(supply_reqs.branch);
        $('#daterequestsupply-delete').val(supply_reqs.date_requested);
        $('#driver-delete').val(supply_reqs.driver_staff);
        $('#driver_truck-delete').val(supply_reqs.driver_truck);
        $('#datedeliveredsupply-delete').val(supply_reqs.date_delivered);
      },
    },
  };
</script>