<template>
    <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
        <thead class="table-light">
        <tr>
            <th width="30%" class="text-center">Driver Name</th>
            <th width="5%" class="text-center">Status</th>
            <th width="10%" class="text-center">Action</th>
        </tr>
        </thead>

<tbody>
        <tr v-for="driver in drivers" :key="driver.id">
        <td style="vertical-align: middle;">{{ driver.staff }}</td>

            <div>
                <select class="btn btn-sm dropdown" style="max-width: 160px; max-height: 33px; font-size: 11px;" v-model="driver.status" @change="updateDriverStatus(drivers)">
                <option value="For Approval" class="btn btn-soft-info btn-sm dropdown">For Approval</option>
                <option value="Active" class="btn btn-soft-success btn-sm dropdown">Active</option>
                <option value="Disable" class="btn btn-soft-warning btn-sm dropdown">Disable</option>
                </select>
            </div>

            <td class="text-center">
            <div class="dropdown d-inline-block">
                <button class="btn btn-soft-info btn-sm dropdown" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="vertical-align: middle;">Actions</button>
                <ul class="dropdown-menu dropdown-menu-end">
                <li>
                    <button type="button" class="dropdown-item viewbtn" data-bs-toggle="modal" data-bs-target="#viewDriverModal" @click="viewDriver(drivers)">
                    <i class="ri-eye-fill align-bottom me-2 text-muted"></i>View
                    </button>
                </li>

                <li>
                    <button type="button" class="dropdown-item editbtn" data-bs-toggle="modal" data-bs-target="#editDriverModal" @click="editDriver(drivers)">
                    <i class="ri-pencil-line align-bottom me-2 text-muted"></i>Edit
                    </button>
                </li>

                <li>
                    <button type="button" class="dropdown-item deletebtn" data-bs-toggle="modal" data-bs-target="#deleteDriverModal" @click="deleteDriver(drivers)">
                    <i class="ri-delete-bin-2-line align-bottom me-2 text-muted"></i>Delete
                    </button>
                </li>

                <li>
                    <button type="button" class="dropdown-item recoverbtn" data-bs-toggle="modal" data-bs-target="#recoverDriverModal" @click="recoverDriver(drivers)">
                    <i class="ri-save-3-fill align-bottom me-2 text-muted"></i>Recover
                    </button>
                </li>
                </ul>
            </div>
            </td>
        </tr>
        </tbody>
    </table>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      drivers: [],
    };
  },
  created() {
    this.fetchDrivers();
  },
  methods: {
    fetchDrivers() {
      axios
        .get('http://restful.localhost:8000/api/driver/')
        .then((response) => {
          this.drivers = response.data;
        })
        .catch((error) => {
          console.error('Error fetching drivers:', error);
        });
    }},
};
</script>
