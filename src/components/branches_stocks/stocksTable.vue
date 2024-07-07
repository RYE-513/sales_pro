<template>

    <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
        <thead class="table-light">
        <tr>
            <th width="20%" class="text-center">Warehouse</th>
            <th width="10%" class="text-center">Quantity</th>
        </tr>    
        </thead>

        <tbody>
            <tr v-for="stock in stocks" :key="stock.id">
                <td style="vertical-align: middle;">{{ stock.warehouse }}</td>
                <td style="vertical-align: middle;">{{ stock.quantity }}</td>
            </tr>
        </tbody>
    </table>
    
</template>


<script>
import axios from 'axios';

export default {

  data() {
    return {
      stocks: []  // Array to store fetched stocks data
    };
  },

  mounted() {
    // Fetch data when the component is mounted
    this.fetchStocks();
  },

  methods: {
    fetchStocks() {
      axios.get('http://restful.localhost:8000/api/stocks/')
        .then(response => {
          this.stocks = response.data;  // Update the 'stocks' array with API response data
        })
        .catch(error => {
          console.error('Error fetching stocks:', error);
        });
    }
  }
};
</script>
