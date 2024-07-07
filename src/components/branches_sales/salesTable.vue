<template>

<table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
    <thead class="table-light">
    <tr>
        <th width="20%" class="text-center">Inventory Number</th>
        <th width="20%" class="text-center">Date</th>
        <th width="20%" class="text-center">Total Price</th>
        <th width="10%" class="text-center">Entry By</th>
        <th width="10%" class="text-center">Action</th>
    </tr>
    </thead>

    <tbody>
        <tr v-for="sale in sales" :key="sale.id">
            <td style="vertical-align: middle;">{{ sale.inv_no }}</td>
            <td style="vertical-align: middle;">{{ sale.date }}</td>
            <td style="vertical-align: middle;">{{ sale.total_price }}</td>
            <td style="vertical-align: middle;">{{ sale.entry_by }}</td>
            <td class="text-center">
                <div class="dropdown d-inline-block">
                <button class="btn btn-soft-info btn-sm dropdown" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="vertical-align: middle;">Actions</button>
                <ul class="dropdown-menu dropdown-menu-end">
                    <li>
                    <button type="button" class="dropdown-item viewbtn" data-bs-toggle="modal" data-bs-target="#viewBranchModal" @click="viewBranch(branch)">
                        <i class="ri-eye-fill align-bottom me-2 text-muted"></i>View
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
    sales: []
    };
},

mounted() {
    this.fetchSales();
},

methods: {
    fetchSales() {
    axios.get('http://restful.localhost:8000/api/sales/')
        .then(response => {
            this.sales = response.data;
        })
        .catch(error => {
            console.error('Error fetching sales:', error);
        });
    },
    viewBranch(sale) {
      // Add logic to view branch details here
    }
}};

</script>