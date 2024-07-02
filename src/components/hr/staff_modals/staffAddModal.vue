<template>
  <div class="modal fade" tabindex="-1" role="dialog" ref="modal">
    <div class="modal-dialog modal-dialog-centered modal-lg">
      <div class="modal-content">
        <div class="modal-header bg-soft-success" style="padding: 20px;">
          <h5 class="modal-title">Add New Staff</h5>
          <button type="button" class="btn-close" @click="closeModal"></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submitForm">
            <div class="mb-3 row">
              <div class="col-md-6">
                <label for="firstName" class="form-label">First Name</label>
                <input type="text" class="form-control mb-1" id="first_name" name="first_name" placeholder="First Name" v-model="formData.first_name" required>
              </div>
              <div class="col-md-6">
                <label for="lastName" class="form-label">Last Name</label>
                <input type="text" class="form-control mb-1" id="last_name" name="last_name" placeholder="Last Name" v-model="formData.last_name" required>
              </div>
            </div>
            <div class="mb-3 row">
              <div class="col-md-6">
                <label for="mobile_no" class="form-label">Contact Number</label>
                <input type="text" class="form-control" id="mobile_no" name="mobile_no" placeholder="Contact Number" v-model="formData.mobile_no" @input="maskContactNumber" required>
              </div>
              <div class="col-md-6">
                <label for="email" class="form-label">Email Address</label>
                <input type="email" class="form-control" id="email" name="email" placeholder="Email Address" v-model="formData.email" required>
              </div>
            </div>
            <div class="mb-3">
              <label for="roles">Roles</label>
              <select id="roles" class="select2 form-control" v-model="selectedRole" required>
                <option value="">Select Role</option>
                <option v-for="role in roles" :key="role.id" :value="role.id">{{ role.role }}</option>
              </select>
            </div>
            
            <button type="submit" class="btn btn-success">Add Staff</button>
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
        first_name: '',
        last_name: '',
        mobile_no: '',
        email: '',
        role: '', 
      },
      roles: [],
      selectedRole: '',
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
        const responseRoles = await axios.get('http://merge.localhost:8000/api/roles/');
        this.roles = responseRoles.data.filter(role => role.status === 'Active');
      //  this.roles = responseRoles.data;
      } catch (error) {
        console.error('Error fetching dropdown data:', error);
      }
    },
    maskContactNumber(input) {
      var format = "XXX-XXXX-XXX";
      var value = input.value;
      var newValue = value.replace(/\D/g, '');
      var maskedValue = "";
      var j = 0;
      for (var i = 0; i < format.length; i++) {
        if (format[i] === "X") {
          if (newValue[j] !== undefined) {
            maskedValue += newValue[j];
            j++;
          } else {
            break;
          }
        } else {
          maskedValue += format[i];
        }
      }
      input.value = maskedValue;
    },

    async submitForm() {
      // Assign the selected role ID to formData
      this.formData.role = this.selectedRole;
      const response = await axios.post('http://merge.localhost:8000/api/staff/', this.formData)
        .then(response => { 
          this.$emit('addStaffSuccess', response.data); // Emit event when role is added successfully
          this.closeModal();
          
          setTimeout(() => {
          location.reload();
        }, 500);
        })
        .catch(error => {
          console.error('Error adding staff:', error); // Log the error for debugging
        });
    },
  },
  mounted() {
    this.fetchDropdownData();
    var contactNumberInput = document.getElementById("mobile_no");
    if (contactNumberInput) {
      contactNumberInput.addEventListener("input", () => {
        this.maskContactNumber(contactNumberInput);
      });
    }
  },
};
</script>