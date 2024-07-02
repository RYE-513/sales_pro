<template>

    <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
        <thead class="table-light">
        <tr>
            <th width="20%" class="text-center">Product</th>
            <th width="20%" class="text-center">Warehouse</th>
            <th width="20%" class="text-center">Category</th>
            <th width="10%" class="text-center">In Out</th>
            <th width="10%" class="text-center">Quantity</th>
        </tr>    
        </thead>

        <tbody>
            <tr v-for="stock in stocks" :key="stock.id">
                <td style="vertical-align: middle;">{{ stock.stock_product }}</td>
                <td style="vertical-align: middle;">{{ stock.stock_warehouse }}</td>
                <td style="vertical-align: middle;">{{ stock.stock_category }}</td>
                <td style="vertical-align: middle;">{{ stock.in_out }}</td>
                <td style="vertical-align: middle;">{{ stock.quantity }}</td>
            </tr>
        </tbody>
    </table>
    
</template>


<script>
    import axios from 'axios';
    
    export default {
        props: ['stocks'],
    
    data() {
        return {    
            stocks: [],
        };
        },
    
        mounted() {
        this.fetchData();
        },
    
        methods: {
        fetchData() {
            axios.get('http://merge.localhost:8000/api/stocks/')
                .then(response => {
                this.stocks = response.data;
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
        },
        }
    };
</script>