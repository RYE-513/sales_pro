<template>
    <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
      <thead class="table-light"> 
        <tr>
            <th width="20%" class="text-center">Products</th>
            <th width="15%" class="text-center">Category</th>
            <th width="15%" class="text-center">Package</th>
            <th width="10%" class="text-center">Product Price</th>
            <th width="10%" class="text-center">Status</th>
            <th width="10%" class="text-center">Action</th>
        </tr>
      </thead>
      <tbody>
        

  <tr v-for="product in products" :key="product.id">
    <td>{{ product.product_name }}</td>
    <td>{{ product.product_category}}</td>
    <td>{{ product.product_package}}</td>
    <td>{{ product.current_price}}</td>
    <td class="text-center">{{product.status}}</td>

<td class="text-center">
  <div class="dropdown d-inline-block">
    <button class="btn btn-soft-info btn-sm dropdown" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="vertical-align: middle;">Actions</button>
    <ul class="dropdown-menu dropdown-menu-end">
      <li>
        <button type="button" class="dropdown-item viewbtn" data-bs-toggle="modal" data-bs-target="#viewProductsModal" @click="viewProducts(product)">
          <i class="ri-eye-fill align-bottom me-2 text-muted"></i>View
        </button>
      </li>

      <li>
        <button type="button" class="dropdown-item editbtn" data-bs-toggle="modal" data-bs-target="#editProductsModal" @click="editProducts(product)">
          <i class="ri-pencil-line align-bottom me-2 text-muted"></i>Edit
        </button>
      </li>

      <li>
        <button type="button" class="dropdown-item deletebtn" data-bs-toggle="modal" data-bs-target="#deleteProductsModal" @click="deleteProducts(product)">
          <i class="ri-delete-bin-2-line align-bottom me-2 text-muted"></i>Disable
        </button>
      </li>
    </ul>
  </div>
</td>
</tr>
</tbody>
</table>
<deleteModal :selectedProductId="selectedProductId" ref="deleteModalRef" />
</template>

<script>
import axios from 'axios';
import deleteModal from './products_modals/productDeleteModal.vue'
export default {
  components: {
      deleteModal
    },
  data(){
    return {
      products: [],
      selectedProductId: null,
    }
  },
  mounted() {
    this.fetchData();
  },

  methods: {
    fetchData() {
      axios.get('/api/products/')
        .then(response => {
          this.products = response.data.filter(product => product.status !== 'Deleted')
        })
        .catch(error => {
          console.error('Error fetching data: ', error);
        });
    },

    viewProducts(product) {
        $('#viewProductsModal').modal('show');
        $('#product-name-view').val(product.product_name);
        $('#product-category-view').val(product.product_category);
        $('#product-package-view').val(product.product_package);
        $('#product-price-view').val(product.current_price);
      },
      editProducts(product) {
      const productId = product.id;
      console.log(productId);
      this.selectedProductId = productId;
        $('#editProductsModal').modal('show');
        $('#product-name-edit').val(product.product_name);
        $('#product-category-edit').val(product.product_category);
        $('#product-package-edit').val(product.product_package);
        $('#product-price-edit').val(product.current_price);
      },
      deleteProducts(product) {
      const productId = product.id;
      console.log(productId);
      this.selectedProductId = productId;
        $('#deleteProductsModal').modal('show');
      },
  },
};
</script>