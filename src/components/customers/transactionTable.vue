<template>
    <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
        <thead class="table-light">
        <tr>
            <th width="10%" class="text-center">OR Number</th>
            <th width="20%" class="text-center">Branch</th>
            <th width="15%" class="text-center">Staff</th>
            <th width="15%" class="text-center">Payment Amount</th>
            <th width="15%" class="text-center">Change Amount</th>
            <th width="15%" class="text-center">Total</th>
            <th width="30%" class="text-center">Date</th>
        </tr>
        </thead>

        <tbody>
            <tr v-for="transaction in transaction" :key="transaction.id">
                <td style="vertical-align: middle;">{{ transaction.or_number }}</td>
                <td style="vertical-align: middle;">{{ transaction.branch }}</td>
                <td style="vertical-align: middle;">{{ transaction.staff }}</td>
                <td style="vertical-align: middle;">{{ transaction.payment_amount }}</td>
                <td style="vertical-align: middle;">{{ transaction.change_amount }}</td>
                <td style="vertical-align: middle;">{{ transaction.grand_total }}</td>
                <td style="vertical-align: middle;">{{ transaction.date }}</td>
            </tr>

        </tbody>
    </table>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const transaction = ref([]);

    const fetchTransaction = async () => {
    try {
        const response = await axios.get('/api/transaction/');
        transaction.value = response.data;
        console.log('Fetched transaction:', transaction.value);
    } catch (error) {
        console.error('Error fetching transaction:', error);
    }
    };
    
onMounted(fetchTransaction);
</script>
