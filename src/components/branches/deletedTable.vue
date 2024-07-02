<template>
  <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
    <thead class="table-light">
      <tr>
        <th width="20%" class="text-center">Branch Name</th>
        <th width="20%" class="text-center">Location</th>
        <th width="20%" class="text-center">Manager</th>
        <th width="10%" class="text-center">Status</th>
        <th width="10%" class="text-center">Action</th>
      </tr>
    </thead>

    <tbody>
    <tr v-for="branch in branches" :key="branch.id">
      <td style="vertical-align: middle;">{{ branch.branch_name }}</td>
      <td style="vertical-align: middle;">{{ branch.location }}</td>
      <td style="vertical-align: middle;">{{ branch.manager}}</td>
      <td class="text-center">{{ branch.status }}
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
            <!--
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
            -->
            <li>
              <button type="button" class="dropdown-item recoverbtn" data-bs-toggle="modal" data-bs-target="#recoverBranchModal" @click="recoverBranch(branch)">
                <i class="ri-save-3-fill align-bottom me-2 text-muted"></i>Recover
              </button>
            </li>
          </ul>
        </div>
      </td>
    </tr>
  </tbody>
  </table>
  <recoverModal :selectedBranchId="selectedBranchId" ref="recoverModalRef" /> 
</template>

<script>
import axios from 'axios';
import recoverModal from './branch_modals/branchRecoverModal.vue';

export default {
  components: {
    recoverModal,
  },
  data() {
    return {
      branches: [],
      selectedBranchId: null,
    };
  },

mounted() {
  this.fetchData();
},

methods: {
fetchData() {
  axios.get('http://merge.localhost:8000/api/branches/')
    .then(response => {
      this.branches = response.data.filter(branch => branch.status === 'Deleted'); 
    })
    .catch(error => {
      console.error('Error fetching data:', error);
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
      recoverBranch(branch) {
        const branchId = branch.id;
        console.log(branchId);
        this.selectedBranchId = branchId;
        $('#recoverBranchModal').modal('show');
        $('#branch_name-recover').val(branch.branch_name);
        $('#location-recover').val(branch.location);
        $('#manager-recover').val(branch.manager);
      },
    },
};
</script>
