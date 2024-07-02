<template>
    <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
    <thead class="table-light"> 
        <tr>
            <th width="40%" class="text-center">Product Categories</th>
            <th width="10%" class="text-center">Status</th>
            <th width="10%" class="text-center">Action</th>
        </tr>
    </thead>
    <tbody>
        
      <tr v-for="category in categories " :key="categories.id">
        <td>{{category.category_name }}</td>  
        <td class="text-center"> {{ category.status }}                                                                                             
        </td>
  <td class="text-center">
    <div class="dropdown d-inline-block">
      <button class="btn btn-soft-info btn-sm dropdown" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="vertical-align: middle;">Actions</button>
      <ul class="dropdown-menu dropdown-menu-end">
        <li>
          <button type="button" class="dropdown-item viewbtn" data-bs-toggle="modal" data-bs-target="#viewCategoryModal" @click="viewCategory(category)">
            <i class="ri-eye-fill align-bottom me-2 text-muted"></i>View
          </button>
        </li>
  
        <li>
          <button type="button" class="dropdown-item editbtn" data-bs-toggle="modal" data-bs-target="#editCategoryModal" @click="editCategory(category)">
            <i class="ri-pencil-line align-bottom me-2 text-muted"></i>Edit
          </button>
        </li>
  
        <li>
          <button type="button" class="dropdown-item deletebtn" data-bs-toggle="modal" data-bs-target="#deleteCategoryModal" @click="deleteCategory(category)">
            <i class="ri-delete-bin-2-line align-bottom me-2 text-muted"></i>Disable
          </button>
        </li>
      </ul>
    </div>
  </td>
  </tr>
  </tbody>
  </table>
  <editModal :selectedCategoryId="selectedCategoryId" ref="editModalRef" />
</template>
  
<script>
import axios from 'axios';
import editModal from './category_modals/categoryEditModal.vue';
  export default {
    components: {
      editModal
    },
    data(){
      return {
        categories: [],
        selectedCategoryId: null,
        selectedCategory: {
          id: '',
          category_name: '',
          description: ''
        }
      };
    },
    mounted() {
      this.fetchData();
    },
  
    methods: {
      fetchData() {
        axios.get('/api/categories/')
          .then(response => {
            this.categories = response.data.filter(category => category.status !== 'Deleted')
          })
          .catch(error => {
            console.error('Error fetching data: ', error);
          });
      },
  
      viewCategory(category) {
        const categoryId = category.id;
        console.log(categoryId);
        // @ts-ignore
          $('#viewCategoryModal').modal('show');
          $('#product-category-view').val(category.category_name);
        },
        editCategory(category) {
        const categoryId = category.id;
        console.log(categoryId);
        this.selectedCategoryId = categoryId;
        // @ts-ignore
          $('#editCategoryModal').modal('show');
          $('#product-category-edit').val(category.category_name);
        },
    },
  };
</script>