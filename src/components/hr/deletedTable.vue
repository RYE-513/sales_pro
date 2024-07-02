<template>
  <!-- DELETED ROLES TABLE -->
    <div class="flex-grow-1">
      <h6 class="card-title mb-0">Deleted Role List</h6>
      <br>
    </div>
    <table class="table table-bordered key-buttons text-nowrap table-striped table-bordered" width="100%">
      <thead class="table-light">
          <tr>
              <th width="10%" class="text-center">Role Name</th>
              <th width="10%" class="text-center">Description</th>
              <th width="10%" class="text-center">Status</th>
              <th width="10%" class="text-center">Action</th>
          </tr>
      </thead>
      <tbody>
        <tr v-for="role in roles" :key="role.id">
          <td style="vertical-align: middle;">{{ role.role }}</td>
          <td style="vertical-align: middle;">{{ role.description }}</td>
          <td class="text-center">{{ role.status }}
          </td>
  
          <td class="text-center">
            <div class="dropdown d-inline-block">
              <button class="btn btn-soft-info btn-sm dropdown" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="vertical-align: middle;">Actions</button>
              <ul class="dropdown-menu dropdown-menu-end">
                <li>
                  <button type="button" class="dropdown-item viewbtn" data-bs-toggle="modal" data-bs-target="#viewRolesModal" @click="viewRole(role)">
                    <i class="ri-eye-fill align-bottom me-2 text-muted"></i>View
                  </button>
                </li>
                <li>
                  <button type="button" class="dropdown-item recoverbtn" data-bs-toggle="modal" data-bs-target="#recoverRolesModal" @click="recoverRole(role)">
                    <i class="ri-save-3-fill align-bottom me-2 text-muted"></i>Recover
                  </button>
                </li>
              </ul>
            </div>
          </td>
        </tr>
      </tbody>
  </table>
  <!-- DELETED STAFF TABLE -->
      <div class="flex-grow-1">
        <h6 class="card-title mb-0">Deleted Staff List</h6>
        <br>
      </div>
      <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
            <thead class="table-light">
            <tr>
              <th width="10%" class="text-center">First Name</th>
              <th width="10%" class="text-center">Last Name</th>
              <th width="10%" class="text-center">Contact Number</th>
              <th width="10%" class="text-center">Email</th>
              <th width="5%" class="text-center">Role</th>
              <th width="5%" class="text-center">Status</th>
              <th width="5%" class="text-center">Action</th>
            </tr>
          </thead>
          <tbody>
        <tr v-for="staff in staffs" :key="staff.id">
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
                  <button type="button" class="dropdown-item viewbtn" data-bs-toggle="modal" data-bs-target="#viewStaffModal" @click="viewStaff(staff)">
                    <i class="ri-eye-fill align-bottom me-2 text-muted"></i>View
                  </button>
                </li>
                <li>
                  <button type="button" class="dropdown-item recoverbtn" data-bs-toggle="modal" data-bs-target="#recoverStaffModal" @click="recoverStaff(staff)">
                    <i class="ri-save-3-fill align-bottom me-2 text-muted"></i>Recover
                  </button>
                </li>
              </ul>
            </div>
          </td>
        </tr>
        </tbody>
        </table>
    <recoverRoleModal :selectedRoleId="selectedRoleId" ref="recoverRoleModalRef" /> 
    <recoverStaffModal :selectedStaffId="selectedStaffId" ref="recoverStaffModalRef" /> 
</template>

<script>
import axios from 'axios';
import recoverRoleModal from './role_modals/rolesRecoverModal.vue'
import recoverStaffModal from './staff_modals/staffRecoverModal.vue'
export default {
  components: {
    recoverRoleModal,
    recoverStaffModal,
  },
    data() {
      return {
        roles: [],
        staffs: [],
        selectedRoleId: null,
        selectedStaffId: null,
      };
    },
    mounted() {
      this.fetchData();
      this.fetchStaff()
    },
  
    methods: {
    fetchData() {
      axios.get('http://merge.localhost:8000/api/roles/')
        .then(response => {
          this.roles = response.data.filter(role => role.status === 'Deleted');
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
    fetchStaff() {
      axios.get('http://merge.localhost:8000/api/staff/')
        .then(response => {
          this.staffs =response.data.filter(staff => staff.status === 'Deleted');
        })
    },

    viewRole(role) {
        const roleId = role.id;
        console.log(roleId);
        $('#viewRolesModal').modal('show');
        $('#role_name-view').val(role.role);
        $('#description-view').val(role.description);
        $('#status-view').val(role.status);
      },
      recoverRole(role) {
        const roleId = role.id;
        console.log(roleId);
        this.selectedRoleId = roleId;
        $('#recoverRolesModal').modal('show');
        $('#role_name-recover').val(role.role);
        $('#description-recover').val(role.description);
      },
      viewStaff(staff) {
        const staffId = staff.id;
        console.log(staffId);
        this.selectedStaffId = staffId;
        $('#viewStaffModal').modal('show');
        $('#first_name-view').val(staff.first_name);
        $('#last_name-view').val(staff.last_name);
        $('#mobile_no-view').val(staff.mobile_no);
        $('#email-view').val(staff.email);
        $('#roles-view').val(staff.role);
      },
      recoverStaff(staff) {
        const staffId = staff.id;
        console.log(staffId);
        this.selectedStaffId = staffId;
        $('#recoverStaffModal').modal('show');
        $('#first_name-recover').val(staff.first_name);
        $('#last_name-recover').val(staff.last_name);
        $('#mobile_no-recover').val(staff.mobile_no);
        $('#email-recover').val(staff.email);
        $('#roles-recover').val(staff.role);
      }
  },
};
</script>