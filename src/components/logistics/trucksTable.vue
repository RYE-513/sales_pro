<template>
    <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
        <thead class="table-light">
        <tr>
            <th width="20%" class="text-center">Truck Name</th>
            <th width="20%" class="text-center">Truck Net Weight</th>
            <th width="20%" class="text-center">Plate Number</th>
            <th width="10%" class="text-center">Status</th>
            <th width="10%" class="text-center">Action</th>
        </tr>
        </thead>

        <tbody>
        <tr v-for="trucks in trucks" :key="trucks.id">
            <td style="vertical-align: middle;">{{ trucks.truck_name }}</td>
            <td style="vertical-align: middle;">{{ trucks.truck_net_weight }}</td>
            <td style="vertical-align: middle;">{{ trucks.plate_no }}</td> 

            <div>
                <select class="btn btn-sm dropdown" style="max-width: 160px; max-height: 33px; font-size: 11px" v-model="trucks.status" @change="updateTruckStatus(trucks)">
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
                    <button type="button" class="dropdown-item viewbtn" data-bs-toggle="modal" data-bs-target="#viewTruckModal" @click="viewTruck(trucks)">
                    <i class="ri-eye-fill align-bottom me-2 text-muted"></i>View
                    </button>
                </li>

                <li>
                    <button type="button" class="dropdown-item editbtn" data-bs-toggle="modal" data-bs-target="#editTruckModal" @click="editTruck(trucks)">
                    <i class="ri-pencil-line align-bottom me-2 text-muted"></i>Edit
                    </button>
                </li>

                <li>
                    <button type="button" class="dropdown-item deletebtn" data-bs-toggle="modal" data-bs-target="#deleteTruckModal" @click="deleteTruck(trucks)">
                    <i class="ri-delete-bin-2-line align-bottom me-2 text-muted"></i>Delete
                    </button>
                </li>

                <li>
                    <button type="button" class="dropdown-item recoverbtn" data-bs-toggle="modal" data-bs-target="#recoverTruckModal" @click="recoverTruck(trucks)">
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

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const trucks = ref([]);

    const fetchTrucks = async () => {
    try {
        const response = await axios.get('/api/trucks/');
        trucks.value = response.data;
        console.log('Fetched trucks:', trucks.value);
    } catch (error) {
        console.error('Error fetching trucks:', error);
    }
    };
    
onMounted(fetchTrucks);
</script>