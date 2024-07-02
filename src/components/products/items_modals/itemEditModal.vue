<template>
    <div class="modal fade" id="editItemsModal" tabindex="-1" aria-labelledby="editItemsModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header bg-soft-success" style="padding: 15px;">
                <h5 class="modal-title">Update Items</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-edit" name="id-edit" readonly hidden>
                    <div class="row">
                        <div class=" mb-3">
                            <label for="items-name-edit" class="form-label">Items</label>
                            <input type="text" class="form-control" v-model="item_name" required>
                        </div>
                </div>
                        <button type="submit" class="btn btn-success" @click="editItems()">Update Items</button> 
                </form>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
export default {
    props: ['selectedItemId'],
    data() {
        return {
            itemId: '',
            item_name: ''
        };
    },
    watch: {
        selectedItemId: {
            immediate: true,
            handler(newVal) {
                if(newVal) {
                    this.fetchItem(newVal);
                }
            }
        }
    },
    methods: {
        fetchItem(selectedItemId) {
            axios.get(`api/items/${selectedItemId}/`)
            .then(response => {
                const itemDetails = response.data;
                console.log(response);
                this.item_name = itemDetails.item_name;
            })
            .catch(error => {
                console.error('Error fetching Items', error);
            });
        },

        editItems() {
            axios.put(`/api/items/${this.selectedItemId}/`, {
                item_name: this.item_name,
            })
            .then(response => {
                console.log(`Items with ID ${this.selectedItemId} updated successfully`, response.data);
                this.$emit('ItemUpdated', response.data);
                $('#editItemsModal').modal('hide');

                setTimeout(function() {
                    location.reload();
                }, 500);
            })
            .catch(error => {
                console.error('Error updating Items', error);
            });
        }
    }
};
</script>