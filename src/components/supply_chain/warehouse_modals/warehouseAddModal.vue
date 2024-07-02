<template>
  <div class="modal fade" tabindex="-1" role="dialog" ref="modal">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header bg-soft-success" style="padding: 20px;">
          <h5 class="modal-title">Add Warehouse</h5>
          <button type="button" class="btn-close" @click="closeModal"></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submitForm">
            <div class="mb-3">
              <label for="warehouseName" class="form-label">Warehouse Name</label>
              <input type="text" class="form-control mb-1" id="warehouse_name" placeholder="Warehouse Name" v-model="formData.warehouse_name" required>
            </div>
            
            <div class="mb-3">
              <label for="location" class="form-label">Location</label>
              <input type="text" class="form-control" id="location" placeholder="Location" v-model="formData.location" required>
            </div>
            
            <div class="mb-3">
              <label for="staff" class="form-label">Select Caretaker</label>
              <select id="staff" class="select2 form-control" v-model="selectedStaff" required>
                <option value="">Select Caretaker</option>
                <option v-for="staff in staffs" :key="staff.id" :value="staff.id">{{ staff.first_name }} {{ staff.last_name }}</option>
              </select>
            </div>
            <button type="submit" class="btn btn-success">Add Warehouse</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      formData: {
        warehouse_name: '',
        location: '',
        staff: '',
      },
      staffs: [],
      selectedStaff: '',
    };
  },
  methods: {
    openAddModal() {
      $(this.$refs.modal).modal('show');
    },
    closeModal() {
      $(this.$refs.modal).modal('hide');
    },
    async fetchDropdownData() {
      try {
        const responseStaff = await axios.get('http://merge.localhost:8000/api/staff/');
        this.staffs = responseStaff.data.filter(staff => staff.role === 'Manager' && staff.status === 'Active');
      } catch(error) {
        console.error('Error fetching dropdown data:', error);
      }
    },
    async submitForm() {
      try {
        this.formData.staff = this.selectedStaff;
        const response = await axios.post('http://merge.localhost:8000/api/warehouses/', this.formData);
        this.$emit('Warehouses Added Successfully', response.data);
        this.closeModal();

        setTimeout(() => {
          location.reload();
        }, 500);
      } catch (error) {
        console.error('Error adding Branch:', error);
      }
    },
  },

  mounted() {
    this.fetchDropdownData();
  },
};

</script>