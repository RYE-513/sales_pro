<template>
    <div class="modal fade" tabindex="-1" role="dialog" ref="modal">
      <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
          <div class="modal-header bg-soft-success" style="padding: 20px;">
            <h5 class="modal-title">Add Supply Request</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
          <div class="modal-body">
            <form @submit.prevent="submitForm">
              <div class="row mb-3">
                <div class="col-md-6">
                        <label for="req_num" class="form-label" required>Request Number</label>
                        <input type="number" class="form-control" id="req_num" name="req_num" placeholder="Request Number" v-model="formData.req_num" required>
                </div>
                <div class="col-md-6">
                  <label for="staff" class="form-label">Staff</label>
                  <select class="form-control" v-model="formData.staff" required>
                    <option value="">Select Staff</option>
                    <option v-for="staff in staffList" :key="staff.id" :value="staff.id">{{ staff.first_name }} {{ staff.last_name }}</option>
                  </select>
                </div>
            </div>
            <div class="row mb-3">
              <div class="col-md-6">
                <label for="manager" class="form-label">Branch</label>
                <select class="form-control" v-model="formData.branch" required>
                  <option value="">Select Branch</option>
                  <option v-for="branch in branchList" :key="branch.id" :value="branch.id">{{ branch.branch_name }} </option>
                </select>
              </div>
              <div class="col-md-6">
                <label for="description" class="form-label">Date Requested</label>
                <datepicker v-model="formData.date_requested" format="yyyy-MM-dd" input-class="form-control" placeholder="Select Date" required></datepicker>
                <!-- Use formData.date_requested as v-model for the datepicker -->
                <input type="date" class="form-control" v-model="formData.date_requested" name="date_requested" />
                <!-- Use formData.date_requested as v-model for the regular input -->
              </div>
            </div>
            <div class="row mb-3">
              <div class="col-md-6">
                  <label for="staff" class="form-label">Driver</label>
                  <select class="form-control" v-model="formData.driver" required>
                    <option value="">Select Driver</option>
                    <option v-for="driver_staff in driver_staffList" :key="driver_staff.id" :value="driver_staff.id">{{ driver_staff.first_name }} {{ driver_staff.last_name }}</option>
                  </select>
                </div>
                <div class="col-md-6">
                  <label for="description" class="form-label">Truck</label>
                  <input type="text" class="form-control" id="driver_truck" name="driver_truck" placeholder="Truck" required/>
              </div>
            </div>
            <div class="col-md-12">
              <label for="description" class="form-label">Date Delivered</label>
              <datepicker v-model="formData.date_delivered" format="yyyy-MM-dd" input-class="form-control" placeholder="Select Date" required></datepicker>
              <!-- Use formData.date_requested as v-model for the datepicker -->
              <input type="date" class="form-control" v-model="formData.date_delivered" name="date_requested" />
              <!-- Use formData.date_requested as v-model for the regular input -->
            </div>
            <br>
              <button type="submit" class="btn btn-success">Add Supply Request</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>

<script>
import axios from 'axios';
  
  export default {
    data() {
      return {
        formData: {
          // req_num: '',
          // staff: ''
          // branch: '',
          // date_requested: '',
          // driver_staff: '',
          // driver_truck: '',
          // date_delivered: '',

        },
        // staffList: [] // Initialize an empty array to hold the staff list
        // branchList: []
        // driver_staffList: []


      };
    },
    methods: {
      openAddModal() {
        $(this.$refs.modal).modal('show');
      },
      closeModal() {
        $(this.$refs.modal).modal('hide');
      },
      fetchStaff() {
        const subdomain = window.location.hostname.split('.')[0];
        const baseURL = `http://${subdomain}.localhost:8000`;
        axios.get(`${baseURL}/api/staff/`) // Replace 'staff' with your actual staff API endpoint
          .then(response => {
            this.staffList = response.data; // Assign the fetched staff list to the staffList array
          })
          .catch(error => {
            console.error('Error fetching staff:', error);
          });
      },
      submitForm() {
        const subdomain = window.location.hostname.split('.')[0];
        const baseURL = `http://${subdomain}.localhost:8000`;
        axios.post(`${baseURL}/api/branches/`, this.formData)
          .then(response => {
            this.$emit('addBranch', this.formData);
            this.closeModal();
          })
          .catch(error => {
            console.error('Error adding branch:', error);
          });
      }
    },
    mounted() {
      // Fetch staff when the component is mounted
      this.fetchStaff();
    }
  };

  // DATE PICKER

  import { ref } from 'vue';
  import Datepicker from '@vuepic/vue-datepicker';
  import '@vuepic/vue-datepicker/dist/main.css';

  const date = ref();
</script>
<!-- 
<script>
import axios from 'axios';

export default {
  data() {
    return {
      formData: {
        req_num: '',
        staff: '',
        branch: '',
        date_requested: '',
        driver_staff: '',
        driver_truck: '',
        date_delivered: '',
      },
      staffs: [],
      branches: [],
      driver_staffs: [],
      selectedStaff: '',
      selectedBranch: '',
      selectedDriver: '',
    };
  },
  methods: {
    openAddModal() {
      $(this.$refs.modal).modal('show');
    },
    closeModal() {
      $(this.$refs.modal).modal('hide');
    },
    async fetchStaff() {
      try {
        const responseStaff = await axios.get('/api/staff/');
        this.staffs = responseStaff.data.filter(staff => staff.role !== 'Driver' && staff.status === 'Active');
        const responseDriver = await axios.get('/api/staff/');
        this.driver_staffs = responseDriver.data.filter(driver_staff => driver_staff.role === 'Driver && driver_staff.status === 'Acitve');
      } catch(error) {
        console.error('Error fetching dropdown Staff data:', error);
      }
    },
    async fetchBranch() {
      try {
      const responseBranch = await axios.get('/api/branches/');
      this.branches = responseBranch.data.filter(branch => branch.status !== 'Deleted');
      } catch(error) {
        console.error('Error fetching dropdown Branches data:', error);
      }
    },
    async submitForm() {
      try {
        this.formData.staff = this.selectedStaff;
        this.formData.branch = this.selectedBranch;
        this.formData.driver_staff = this.selectedDriver;
        const response = await axios.post('/api/supplyreqs/', this.formData);
        this.$emit('Supply Request Added Successfully', response.data);
        this.closeModal();

        setTimeout(() => {
          location.reload();
        }, 500);
      } catch(error) {
        console.error('Error adding Supply Request:', error);
      }
    },
  },
  mounted() {
    this.fetchStaff();
    this.fetchBranch();
  }
}
</script> -->