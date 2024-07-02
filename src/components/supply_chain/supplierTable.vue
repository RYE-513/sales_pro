<template>
  <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
    <thead class="table-light"> 
      <tr>
        <th width="20%" class="text-center">Suppliers Name</th>
        <th width="15%" class="text-center">Location</th>
        <th width="15%" class="text-center">Contact Number</th>
        <th width="15%" class="text-center">Contact Person</th> 
        <th width="10%" class="text-center">Status</th>
        <th width="5%" class="text-center">Action</th> 
      </tr>
    </thead>
    <tbody>
      
      <tr v-for="supplier in supplier" :key="supplier.id">
        <td>{{ supplier.supplier_name }}</td>
        <td>{{ supplier.location}}</td>
        <td><span>+63{{supplier.contact_number}}</span></td>
        <td>{{ supplier.contact_person}}</td>
        <td class="text-center"> {{ supplier.status }}
        </td>
    <td class="text-center">
      <div class="dropdown d-inline-block">
        <button class="btn btn-soft-info btn-sm dropdown" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="vertical-align: middle;">Actions</button>
        <ul class="dropdown-menu dropdown-menu-end">
          <li>
            <button type="button" class="dropdown-item viewbtn" data-bs-toggle="modal" data-bs-target="#viewSupplierModal" @click="viewSupplier(supplier)">
              <i class="ri-eye-fill align-bottom me-2 text-muted"></i>View
            </button>
          </li> 

          <li>
            <button type="button" class="dropdown-item editbtn" data-bs-toggle="modal" data-bs-target="#editSupplierModal" @click="editSupplier(supplier)">
              <i class="ri-pencil-line align-bottom me-2 text-muted"></i>Edit
            </button>
          </li>

          <li>
            <button type="button" class="dropdown-item disablebtn" data-bs-toggle="modal" data-bs-target="#disablePropertyModal" @click="disableSupplier(supplier)">
              <i class="ri-delete-bin-fill align-bottom me-2 text-muted"></i>Disable
            </button>
          </li>
        </ul>
      </div>
    </td>
  </tr>
</tbody>
</table>
<editModal :selectedSupplierId="selectedSupplierId" ref="editModalRef" />
</template>

<script>
import axios from 'axios'
import editModal from './supplier_modals/supplierEditModal.vue';
export default {
  components: {
    editModal
  },
  data() {
    return {
      supplier: [],
      selectedSupplierId: null,
      selectedSupplier: {
        id: '',
        supplier_name: '',
        location: '',
        contact_number: '',
        contact_person: '',
      }
    };
  },

  mounted() {
    this.fetchData();
  },

  methods: {
    fetchData() {
      axios.get('/api/supplier/')
        .then(response => {
          this.supplier = response.data.filter(supplier => supplier.status !== 'Deleted')
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },

    viewSupplier(supplier) {
      $('#viewSupplierModal').modal('show');
      $('#supplier-name-view').val(supplier.supplier_name);
      $('#supplier-location-view').val(supplier.location);
      $('#supplier-contact_number-view').val(supplier.contact_number);
      $('#supplier-contact_person-view').val(supplier.contact_person);
    },
    editSupplier(supplier) {
      const supplierId = supplier.id;
      console.log(supplierId);
      this.selectedSupplierId = supplierId;
      $('#editStaffModal').modal('show');
      $('#supplier-name-edit').val(supplier.supplier_name);
      $('#supplier-location-edit').val(supplier.location);
      $('#supplier-contact_number-edit').val(supplier.contact_number);
      $('#supplier-contact_person-edit').val(supplier.contact_person);
    },
    deleteStaff(supplier) {
      const supplierId = supplier.id;
      console.log(supplierId);
      this.selectedSupplierId = staffId;
      $('#deleteStaffModal').modal('show');
      $('#supplier-name-view').val(supplier.supplier_name);
      $('#supplier-location-view').val(supplier.location);
      $('#supplier-contact_number-view').val(supplier.contact_number);
      $('#supplier-contact_person-view').val(supplier.contact_person);
    }
  },
};
</script>

<!-- <script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const supplier = ref([]);

// Function to fetch position data
const fetchSupplier = async () => {
  try {
    const response = await axios.get('/api/supplier/');
    supplier.value = response.data;
    console.log('Fetched supplier:', supplier.value);
  } catch (error) {
    console.error('Error fetching supplier:', error);
  }
};

onMounted(fetchSupplier);

</script> -->