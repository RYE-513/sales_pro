<template>
  <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
    <thead class="table-light">
      <tr>
        <th width="20%" class="text-center">Branch Name</th>
        <th width="20%" class="text-center">Location</th>
        <th width="20%" class="text-center">Manager</th>
        <th width="10%" class="text-center">Status</th>
        <th width="10%" class="text-center">Stocks</th>
        <th width="10%" class="text-center">Sales</th>
        <th width="10%" class="text-center">Action</th>
      </tr>
    </thead>

    <tbody>
      <tr v-for="branch in branches" :key="branch.id">
        <td style="vertical-align: middle;">{{ branch.branch_name }}</td>
        <td style="vertical-align: middle;">{{ branch.location }}</td>
        <td style="vertical-align: middle;">{{ branch.manager }}</td> 
        <td class="text-center">{{ branch.status }}
        </td>
        <td class="text-center">
          <div class="dropdown d-inline-block">
            <RouterLink to="/branches_stocks" class="btn btn-warning btn-sm dropdown">Stocks</RouterLink>
          </div>     
        </td>

        <td class="text-center">
          <div class="dropdown d-inline-block">
            <RouterLink to="/branches_sales" class="btn btn-primary btn-sm dropdown">Sales</RouterLink>
          </div>     
        </td>  

        <td class="text-center">
          <div class="dropdown d-inline-block">
            <button class="btn btn-soft-info btn-sm dropdown" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="vertical-align: middle;">Actions</button>
            <ul class="dropdown-menu dropdown-menu-end">
              <li>
                <button type="button" class="dropdown-item viewbtn" data-bs-toggle="modal" data-bs-target="#BranchModal" @click="viewBranchModal(branch)">
                  <i class="ri-eye-fill align-bottom me-2 text-muted"></i>View
                </button>
              </li>

              <li>
                <button type="button" class="dropdown-item editbtn" data-bs-toggle="modal" data-bs-target="#editBranchModal" @click="editBranch(branch)">
                  <i class="ri-pencil-line align-bottom me-2 text-muted"></i>Edit
                </button>
              </li>

              <li>
                <button type="button" class="dropdown-item deletebtn" data-bs-toggle="modal" data-bs-target="#deleteBranchModal" @click="deleteBranch(branch)">
                  <i class="ri-delete-bin-2-line align-bottom me-2 text-muted"></i>Delete
                </button>
              </li>
            </ul>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
  <deleteModal :selectedBranchId="selectedBranchId" ref="deleteModalRef" /> 
  <editModal :selectedBranchId="selectedBranchId" ref="editModalRef" />
</template>

<script>
import axios from 'axios';
import deleteModal from './branch_modals/branchDeleteModal.vue';
import editModal from './branch_modals/branchEditModal.vue';

export default {
  components: {
    deleteModal,
    editModal,
  },

  data() {
    return {
      branches: [],
      selectedBranchId: null,
      selectedBranch: {
        id: '',
        branch_name: '',
        location: '',
        manager: '',
      }
    };
  },

  mounted() {
    this.fetchBranches();
  },

  methods: {
    fetchBranches() {
      axios.get('http://restful.localhost:8000/api/branches/')
          .then(response => {
            this.branches = response.data.filter(branch => branch.status !== 'Deleted')
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
    handleAddBranch(branch) {
      axios.post('/api/branches/', branch)
        .then(response => {
          this.$emit('addBranchesSuccess', response.data);
        })
        .catch(error => {
          console.error('Error adding branches:', error);
        });
    },
    
    viewBranchModal(branch) {
      const branchId = branch.id;
      console.log(branchId);
        $('#BranchModal').modal('show');
        $('#branch_name-view').val(branch.branch_name);
        $('#location-view').val(branch.location);
        $('#manager-view').val(branch.manager);
      },
    editBranch(branch) {
      const branchId = branch.id;
      console.log(branchId);
      this.selectedBranchId = branch.id;
        $('#editBranchModal').modal('show');
        $('#branch_name-edit').val(branch.branch_name);
        $('#location-edit').val(branch.location);
        $('#manager-edit').val(branch.manager); 
    },
    deleteBranch(branch) {
      const branchId = branch.id;
      console.log(branchId);
      this.selectedBranchId = branchId;
        $('#deleteBranchModal').modal('show');
        $('#branch_name-delete').val(branch.branch_name);
        $('#location-delete').val(branch.location);
        $('#manager-delete').val(branch.manager);
    }
  },
};
</script>