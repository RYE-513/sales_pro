<template>
  <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
    <thead class="table-light"> 
      <tr>
          <th width="20%" class="text-center">Items</th>
          <th width="10%" class="text-center">Status</th>
          <th width="10%" class="text-center">Action</th>
      </tr>
    </thead>
    <tbody>
      
      <tr v-for="items in items" :key="items.id">
        <td>{{ items.item_name }}</td>
        <td class="text-center"> {{ items.status }}
    </td>
    
<td class="text-center">
  <div class="dropdown d-inline-block">
    <button class="btn btn-soft-info btn-sm dropdown" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="vertical-align: middle;">Actions</button>
    <ul class="dropdown-menu dropdown-menu-end">
      <li>
        <button type="button" class="dropdown-item viewbtn" data-bs-toggle="modal" data-bs-target="#viewItemsModal" @click="viewItems(items)">
          <i class="ri-eye-fill align-bottom me-2 text-muted"></i>View
        </button>
      </li>
      <li>
        <button type="button" class="dropdown-item editbtn" data-bs-toggle="modal" data-bs-target="#editItemsModal" @click="editItems(items)">
          <i class="ri-pencil-line align-bottom me-2 text-muted"></i>Edit
        </button>
      </li>
      <li>
        <button type="button" class="dropdown-item deletebtn" data-bs-toggle="modal" data-bs-target="#deleteItemsModal" @click="deleteItems(items)">
          <i class="ri-delete-bin-2-line align-bottom me-2 text-muted"></i>Disable
        </button>
      </li>
    </ul>
  </div>
</td>
</tr>
</tbody>
</table>
<editModal :selectedItemId="selectedItemId" ref="editModalRef" />
</template>
  
<script>
import axios from 'axios';
import editModal from './items_modals/itemEditModal.vue';
export default {
  components: {
    editModal
  },
  data(){
    return {
      items: [],
      selectedItemId: null,
      selectedItem: {
        id: '',
        item_name: ''
      }
    };
  },
  mounted() {
    this.fetchData();
  },

  methods: {
    fetchData() {
      axios.get('/api/items/')
        .then(response => {
          this.items = response.data.filter(items => items.status !== 'Deleted')
        })
        .catch(error => {
          console.error('Error fetching data: ', error);
        });
    },

    viewItems(items) {
      $('#viewItemsModal').modal('show');
      $('#items-name-view').val(items.item_name);
    },
    editItems(items) {
      const itemId = items.id;
      console.log(itemId);
      this.selectedItemId = itemId;
      $('#editItemsModal').modal('show');
      $('#items-name-edit').val(items.item_name);
    },
  }
}
</script>