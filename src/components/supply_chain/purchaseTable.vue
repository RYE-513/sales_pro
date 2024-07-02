<template>
    <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
    <thead class="table-light"> 
        <tr>
            <th width="10%" class="text-center">Suppliers Name</th>
            <th width="10%" class="text-center">PO Number</th> 
            <th width="10%" class="text-center">Delivery Address</th>
            <th width="10%" class="text-center">Delivery Date</th>
            <th width="5%"  class="text-center">Action</th>
        </tr>
    </thead>
    <tbody>
      <tr v-for="purchase in purchase" :key="purchase.id">
        <td>{{ purchase.supplier }}</td>
        <td>{{ purchase.po_number }}</td>
        <td>{{ purchase.delivery_address }}</td>
        <td>{{ purchase.delivery_date }}</td> 

    <td class="text-center">
      <div class="dropdown d-inline-block">
        <button class="btn btn-soft-info btn-sm dropdown" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="vertical-align: middle;">Actions</button>
        <ul class="dropdown-menu dropdown-menu-end">
          <li>
            <button type="button" class="dropdown-item viewbtn" data-bs-toggle="modal" data-bs-target="#viewPurchaseModal" @click="viewPackage(purchase)">
              <i class="ri-eye-fill align-bottom me-2 text-muted"></i>View
            </button>
          </li> 

          <li>
            <button type="button" class="dropdown-item editbtn" data-bs-toggle="modal" data-bs-target="#editPurchaseModal" @click="editPurchase(purchase)">
              <i class="ri-pencil-line align-bottom me-2 text-muted"></i>Edit
            </button>
          </li>
        </ul>
      </div>
    </td>
  </tr>
</tbody>
</table>
<editModal :selectedPurchaseId="selectedPurchaseId" ref="editModalRef" />
</template>

<script>
import axios from 'axios';
import editModal from './purchase_modals/purchaseEditModal.vue';
  export default {
    components: {
      editModal
    },
    data(){
      return {
        purchase: [],
        selectedPurchaseId: null,
        selectedPurchase: {
          id: '',
          supplier: '',
          po_number: '',
          delivery_address: '',
          delivery_date: ''
        }
      }
    },
    mounted(){
      this.fetchData();
    },

    methods: {
      fetchData() {
        axios.get('/api/purchase/')
          .then(response => {
            this.purchase = response.data;
            // this.purchase = response.data.filter(purchase => purchase.status !== 'Deleted')
          })
          .catch(error => {
            console.error('Error fetching data: ', error);
          });
      },

      viewPackage(purchase) {
        $('#viewPurchaseModal').modal('show');
        $('#purchase-view').val(purchase.supplier);
        $('#po-view').val(purchase.po_number);
        $('#deliveryaddress-view').val(purchase.delivery_address);
        $('#deliverydate-view').val(purchase.delivery_date);
      },
      editPurchase(purchase) {
        const purchaseId = purchase.id;
        this.selectedPurchaseId = purchaseId;
        $('#editPurchaseModal').modal('show');
      },
    }
  }
</script>

<!-- <script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const purchase = ref([]);

// Function to fetch position data
const fetchPurchase = async () => {
  try {
    const response = await axios.get('/api/purchase/');
    purchase.value = response.data;
    console.log('Fetched purchase:', purchase.value);
  } catch (error) {
    console.error('Error fetching purchase:', error);
  }
};

onMounted(fetchPurchase);

</script>
     -->