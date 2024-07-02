<template>
  <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
    <thead class="table-light"> 
      <tr>
        <th width="40%" class="text-center">Product Packages</th>
        <th width="10%" class="text-center">Status</th>
        <th width="10%" class="text-center">Action</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for=" packages in packagess" :key="packages.id">
        <td>{{ packages.package_name }}</td>
        <td class="text-center"> {{ packages.status }}
        </td>
        <td class="text-center">
          <div class="dropdown d-inline-block">
            <button class="btn btn-soft-info btn-sm dropdown" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="vertical-align: middle;">Actions</button>
            <ul class="dropdown-menu dropdown-menu-end">
              <li>
                <button type="button" class="dropdown-item viewbtn" data-bs-toggle="modal" data-bs-target="#viewPackageModal" @click="viewProducts(packages)">
                  <i class="ri-eye-fill align-bottom me-2 text-muted"></i>View
                </button>
              </li> 

              <li>
                <button type="button" class="dropdown-item editbtn" data-bs-toggle="modal" data-bs-target="#editPackageModal" @click="editPackage(packages)">
                  <i class="ri-pencil-line align-bottom me-2 text-muted"></i>Edit
                </button>
              </li>

              <li>
                <button type="button" class="dropdown-item disablebtn" data-bs-toggle="modal" data-bs-target="#deletePackageModal" @click="disablePackage(packages)">
                  <i class="ri-delete-bin-fill align-bottom me-2 text-muted"></i>Disable
                </button>
              </li>
            </ul>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
  <editModal :selectedPackageId="selectedPackageId" ref="editModalRef" />
</template>

<script>
import axios from 'axios';
import editModal from './package_modals/packageEditModal.vue';
export default {
  components: {
    editModal
  },
  data(){
    return {
      packagess: [],
      selectedPackageId: null,
      selectedPackage: {
        id: '',
        package_name: ''
      }
    };
  },
  mounted() {
    this.fetchData();
  },

  methods: {
    fetchData() {
      axios.get('/api/packages/')
        .then(response => {
          this.packagess = response.data.filter(packages => packages.status !== 'Deleted')
        })
        .catch(error => {
          console.error('Error fetching data: ', error);
        });
    },

    viewProducts(packages) {
      // @ts-ignore
        $('#viewPackageModal').modal('show');
        $('#product-package-view').val(packages.package_name);
      },
      editPackage(packages) {
      const packageId = packages.id;
      console.log(packageId);
      this.selectedPackageId = packageId;
      // @ts-ignore
        $('#editPackageModal').modal('show');
        $('#product-package-edit').val(packages.package_name);
      },
  },
};
</script>