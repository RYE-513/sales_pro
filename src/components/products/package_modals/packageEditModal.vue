<template>
    <div class="modal fade" id="editPackageModal" tabindex="-1" aria-labelledby="editPackageModalLabel" aria-modal="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header bg-soft-success" style="padding: 15px;">
                <h5 class="modal-title">Edit Package</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <input type="" id="id-edit" name="id-edit" readonly hidden>
                    <div class="">
                        <div class="mb-3">
                            <label for="product-package-edit" class="form-label">Package Name</label>
                            <input type="text" class="form-control" v-model="package_name" name="product-package-edit" required>
                        </div>
                    </div>
                    <div class="col-lg-12">
                        <div class="hstack gap-2 justify-content-end">
                            <button type="button" id="btn_update_info" class="btn btn-success btn-block" @click="editPackage()">Save</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
export default {
    props: ['selectedPackageId'],

    data() {
        return {
            id: '',
            package_name: ''
        };
    },
    watch: {
        selectedPackageId: {
            immediate: true,
            handler(newVal) {
                if(newVal) {
                    this.fetchPackage(newVal);
                }
            }
        }
    },
    methods: {
        fetchPackage(selectedPackageId) {
            axios.get(`api/packages/${selectedPackageId}/`)
            .then(response => {
                const packageDetails = response.data;
                this.package_name = packageDetails.package_name;
            })
            .catch(error => {
                console.error('Error fetching Packages', error);
            });
        },

        editPackage() {
            axios.put(`/api/packages/${this.selectedPackageId}/` , {
                package_name: this.package_name
            })
            .then(response => {
                console.log(`Package with ID ${this.selectedPackageId} updated succesfully`, response.data);
                this.$emit('PackageUpdated', response.data);
                $('#editPackageModal').modal('hide');

                setTimeout(function() {
                    location.reload();
                }, 500);
            })
            .catch(error => {
                console.error('Error updating package:', error);
            });
        }
    }
};
</script>