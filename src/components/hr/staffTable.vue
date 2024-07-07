<template>
  <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
      <thead class="table-light">
        <tr>
        <th width="10%" class="text-center">First Name</th>
        <th width="10%" class="text-center">Last Name</th>
        <th width="10%" class="text-center">Contact Number</th>
        <th width="5%" class="text-center">Email</th>
        <th width="5%" class="text-center">Roles</th>
        <th width="5%" class="text-center">Status</th>
        <th width="5%" class="text-center">Action</th>
      </tr>
    </thead>

    <tbody>
        <tr v-for= "staff in staffs" :key="staff.id">
          <td style="vertical-align: middle;">{{ staff.first_name }}</td>
          <td style="vertical-align: middle;">{{ staff.last_name }}</td>
          <td style="vertical-align: middle;">{{ staff.mobile_no }}</td>
          <td style="vertical-align: middle;">{{ staff.email }}</td>
          <td style="vertical-align: middle;">{{ staff.role }}</td>
          <td class="text-center">{{ staff.status }}
        </td>
        <td class="text-center">
          <div class="dropdown d-inline-block">
            <button class="btn btn-soft-info btn-sm dropdown" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="vertical-align: middle;">Actions</button>
            <ul class="dropdown-menu dropdown-menu-end">
              <li>
                <button type="button" class="dropdown-item viewbtn" data-bs-toggle="modal" data-bs-target="#viewStaffModal"  @click="viewStaff(staff)">
                  <i class="ri-eye-fill align-bottom me-2 text-muted"></i>View
                </button>
              </li>
              <li>
                <button type="button" class="dropdown-item editbtn" data-bs-toggle="modal" data-bs-target="#editStaffModal"  @click="editStaff(staff)">
                  <i class="ri-pencil-line align-bottom me-2 text-muted"></i>Edit
                </button>
              </li>
              <li>
                <button type="button" class="dropdown-item deletebtn" data-bs-toggle="modal" data-bs-target="#deleteStaffModal" @click="deleteStaff(staff)">
                  <i class="ri-delete-bin-2-line align-bottom me-2 text-muted"></i>Delete
                </button>
              </li>
            </ul>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
  <editModal :selectedStaffId="selectedStaffId" ref="editModalRef" />
  <deleteModal :selectedStaffId="selectedStaffId" ref="deleteModalRef" />
</template>

<script>

import axios from 'axios';
import editModal from './staff_modals/staffEditModal.vue';
import deleteModal from './staff_modals/staffDeleteModal.vue';

export default {
  components: {
    editModal,
    deleteModal,
  },
  data() {
    return {
      staffs: [],
      selectedStaffId: null,
    };
  },

  mounted() {
    this.fetchStaffs();
  },

  methods: {
    fetchStaffs() {
      axios.get('http://restful.localhost:8000/api/staff/')
        .then(response => {
          this.staffs = response.data;
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },

    handleAddStaff(staff) {
      axios.post('http://restful.localhost:8000/api/staff/', staff)
        .then(response => {
          this.staffs.push(response.data);
          this.$emit('addStaffSuccess', response.data);
        })
        .catch(error => {
          console.error('Error adding staff:', error);
        });
    },

    viewStaff(staff) {
      $('#viewStaffModal').modal('show');
      $('#first_name-view').val(staff.first_name);
      $('#last_name-view').val(staff.last_name);
      $('#mobile_no-view').val(staff.mobile_no);
      $('#email-view').val(staff.email);
      $('#roles-view').val(staff.role);
    },
    editStaff(staff) {
      const staffId = staff.id;
      console.log(staffId);
      this.selectedStaffId = staffId;
      $('#editStaffModal').modal('show');
      $('#first_name-edit').val(staff.first_name);
      $('#last_name-edit').val(staff.last_name);
      $('#mobile_no-edit').val(staff.mobile_no);
      $('#email-edit').val(staff.email);
      $('#roles-edit').val(staff.role);
    },
    deleteStaff(staff) {
      const staffId = staff.id;
      console.log(staffId);
      this.selectedStaffId = staffId;
      $('#deleteStaffModal').modal('show');
      $('#first_name-delete').val(staff.first_name);
      $('#last_name-delete').val(staff.last_name);
      $('#mobile_no-delete').val(staff.mobile_no);
      $('#email-delete').val(staff.email);
      $('#roles-delete').val(staff.role);
    }
  },
};

</script>

