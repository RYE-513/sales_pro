<script>
</script>
<template>
    <div class="card-body">
        <form method="post" action="{% url 'supply_chain:add_purchase_form' %}" id="ProductsOrderForm">
            <div class="row">
                <label class="col-md-3 col-form-label">Product Name</label>
                <label class="col-md-3 col-form-label">Category</label>
                <label class="col-md-3 col-form-label">Package</label>
                <label class="col-md-3 col-form-label">Product Price</label>
            </div>
            <div class="row">
                <div class="col-md-3">
                    <input type="text" class="form-control" name="product_name" id="product_name">
                    <div class="form-control-feedback" style="font-size: 9pt; padding-top: 5px; color: red;"></div>
                </div>
                <div class="col-md-3">
                    <select class="form-control dpselect" name="category_id">
                        <option>Select Category</option>
                    </select>
                </div>
                <div class="col-md-3">
                    <select class="form-control dpselect" name="package_id">
                        <option>Select Package</option>
                    </select>
                </div>
                <div class="col-md-3">
                    <input type="text" class="form-control" name="product_price" id="product_price">
                </div>
            </div>
        </form>
    </div>
    

                <div class="main-content-label mg-b-5"></div>
                <div class="form-body">
                    <div class="table-responsive">
                        <table style="width: 100%" class="table table-bordered" id="items-tbl">
                            <thead>
                                <th style="padding-top: 5px; padding-bottom: 5px; font-size: 9pt" class="text-center"width="15%">Item Name</th>
                                <th style="padding-top: 5px; padding-bottom: 5px; font-size: 9pt" class="text-center" width="10%">Qty</th>
                                <th style="padding-top: 5px; padding-bottom: 5px; font-size: 9pt" class="text-center" width="10%">Total</th>
                                <th style="padding-top: 5px; padding-bottom: 5px; font-size: 9pt" width="9%" class="text-center">Action</th>
                            </thead>
                            <tbody id="table-Items">
                                <tr>
                                    <td>
                                        <select class="form-control form-control item_selection">
                                            <option value="item1">Item 1</option>
                                            <option value="item2">Item 2</option>
                                            <option value="item3">Item 3</option>
                                            <!-- Add more options as needed -->
                                        </select>
                                    </td>
                                    
                                    <td>
                                        <input type="text" class="form-control form-control dr_amount" name="dr_amount[]">
                                    </td>

                                    <td>
                                        <input type="text" class="form-control form-control dr_amount" name = "">
                                    </td>
                                    
                                    <td class="text-center">
                                        <button type="button" class="btn btn-success btn-add-ledger"><i class="fa far fa-plus-square text-white"></i></button>
                                        <button type="button" class="btn btn-danger btn-remove-ledger "><i class="fa far fa-minus-square text-white"></i></button>
                                    </td>
                                </tr>
                            </tbody>
                                <tfoot style="font-family: arial, sans-serif">
                                    <tr class="table-primary" style="background: #00c292; color: black;">
                                        <td colspan="1" class="text-right" style="font-weight: bold; font-size: 10pt; padding-top: 5px; padding-bottom: 5px;">Total</td>
                                        <td class="text-right" style="font-weight: bold; font-size: 10pt; padding-top: 5px; padding-bottom: 5px;" id="total_dr_amt">0.00</td>
                                        <td class="text-right" style="font-weight: bold; font-size: 10pt; padding-top: 5px; padding-bottom: 5px;" id="total_cr_amt">0.00</td>
                                        <td class="text-right"></td>
                                    </tr>
                                </tfoot>
                            </table>
                        </div>
                    </div>
                


            <div class="card-body">
                <div class="row">
                    <div class="col-md-3">
                        <a href="" class="btn btn-danger float-left">
                            <i class="ri-alert-line"></i> Back
                        </a>
                    </div>
                    <div class="col-md-6"></div>
                    <div class="col-md-3">
                        <button type="button" id="unbalance_warning" class="btn btn-primary float-right unpass_btn">
                            <i class="ri-send-plane-fill"</i> Submit</button>    
                    </div>
                </div>
            </div>
</template>