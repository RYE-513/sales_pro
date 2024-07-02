<template>
    <table id="alternative-pagination" class="table nowrap dt-responsive align-middle table-hover table-bordered" style="width:100%">
        <thead>
        <tr>
            <th width="20%" class="text-center">Products</th>
            <th width="15%" class="text-center">Category</th>
            <th width="15%" class="text-center">Package</th>
            <th width="10%" class="text-center">Product Price</th>
            <th width="10%" class="text-center">Status</th>
            <th width="10%" class="text-center">Action</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td class="products-name"></td>
            <td class="products-category"></td>
            <td class="products-package"></td>
            <td class="products-price"></td>
            <td class="text-center">
            <span class="badge badge-outline-danger">Deleted</span>
            </td>
            <td class="text-center">
            <button type="button" class="btn btn-success btn-sm activate-btn">Activate</button>
            </td>
        </tr>
        </tbody>
    </table>
</template>