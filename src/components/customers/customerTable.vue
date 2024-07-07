<template>
    <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
        <thead class="table-light">
        <tr>
            <th width="20%" class="text-center">Customer Name</th>
            <th width="20%" class="text-center">Transaction History</th>
        </tr>
        </thead>

        <tbody>
        <tr v-for="customer in customer" :key="customer.id">
            <td style="vertical-align: middle;">{{ customer.customer_name }}</td>
            <td class="text-center">
                <div class="dropdown d-inline-block">
                    <RouterLink to="/transactions" class="btn btn-soft-info btn-sm dropdown" data-key="t-analytics">Transaction History</RouterLink>
                </div>     
            </td>
        </tr>
        </tbody>
    </table>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const customer = ref([]);

    const fetchCustomer = async () => {
    try {
        const response = await axios.get('http://restful.localhost:8000/api/customer/');
        customer.value = response.data;
        console.log('Fetched customer:', customer.value);
    } catch (error) {
        console.error('Error fetching customer:', error);
    }
    };
    
onMounted(fetchCustomer);
</script>
