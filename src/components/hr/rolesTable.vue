<template>
  <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
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
          <td class="text-center">{{ role.status }}</td>
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
                  <button type="button" class="dropdown-item editbtn" data-bs-toggle="modal" data-bs-target="#editRolesModal" @click="editRoles(role)">
                    <i class="ri-pencil-line align-bottom me-2 text-muted"></i>Edit
                  </button>
                </li>
                <li>
                  <button type="button" class="dropdown-item deletebtn" data-bs-toggle="modal" data-bs-target="#deleteRolesModal" @click="deleteRoles(role)">
                    <i class="ri-delete-bin-2-line align-bottom me-2 text-muted"></i>Delete
                  </button>
                </li>
              </ul>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
    <deleteModal :selectedRoleId="selectedRoleId" ref="deleteModalRef" />
    <editModal :selectedRoleId="selectedRoleId" ref="editModalRef" />
  </template>
  
  <script>
  import axios from 'axios';
  import deleteModal from './role_modals/rolesDeleteModal.vue';
  import editModal from './role_modals/rolesEditModal.vue';
  export default {
    components: {
      deleteModal,
      editModal,
    },
    data() {
      return {
        roles: [],
        selectedRoleId: null,
        selectedRole: {
          id: '',
          role_name: '',
          description: '',
        }
      };
    },
  
    mounted() {
      this.fetchData();
    },
  
    methods: {
      fetchData() {
        axios.get('/api/roles/')
            .then(response => {
              this.roles = response.data.filter(role => role.status !== 'Deleted')
          })
          .catch(error => {
            console.error('Error fetching data:', error);
          });
      },
  
      handleAddRole(role) {
        axios.post('/api/roles/', role)
          .then(response => {
            this.$emit('addRoleSuccess', response.data);
          })
          .catch(error => {
            console.error('Error adding role:', error);
          });
      },
  
      viewRole(role) {
        $('#viewRolesModal').modal('show');
        $('#role_name-view').val(role.role);
        $('#description-view').val(role.description);
        $('#status-view').val(role.status);
      },
      editRoles(role) {
        const roleId = role.id;
        console.log(roleId);
        this.selectedRoleId = roleId;
        $('#editRolesModal').modal('show');
      },
      deleteRoles(role) {
        const roleId = role.id;
        console.log(roleId);
        this.selectedRoleId = roleId;
        $('#deleteRolesModal').modal('show');
        $('#role-name-delete').val(role.role);
        $('#description-delete').val(role.description);
      }
    },
  };
  </script>
  