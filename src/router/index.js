import LogIn from '@/views/LogIn.vue'
import { createRouter, createWebHistory } from 'vue-router'
import { isAuthenticated } from '../authentication';
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Login',
      component: LogIn
    },

// BRANCHES | BRANCHES | BRANCHES

{
  path: '/branches',
  name: 'branches',
  component: () => import('../views/branches/Branch.vue'),
  meta: {
    title: "Branches",
  },
},

{
  path: '/branches_stocks',
  name: 'branches_stocks',
  component: () => import('../views/branches_stocks/Stocks.vue'),
  meta: {
    title: "Branches Stocks",
  },
},

{
  path: '/branches_sales',
  name: 'branches_sales',
  component: () => import('../views/branches_sales/Sales.vue'),
  meta: {
    title: "Branches Sales",
  },
},

{
  path: '/deleted_branches',
  name: 'deleted_branches',
  component: () => import('../views/branches/deletedBranches.vue'),
  meta: {
    title: "Deleted Branches",
  },
},

// HUMAN RESOURCES | HUMAN RESOURCES | HUMAN RESOURCES

{
  path: '/roles',
  name: 'roles',
  component: () => import('../views/hr/Roles.vue'),
  meta: {
    title: "Roles",
  },
},

{
  path: '/staff',
  name: 'staff',
  component: () => import('../views/hr/Staff.vue'),
  meta: {
    title: "Staff",
  },
},

{
  path: '/deleted_hr',
  name: 'deleted_hr',
  component: () => import('../views/hr/deletedHR.vue'),
  meta: {
    title: "Deleted Human Resources",
  },
},


// PRODUCTS | PRODUCTS | PRODUCTS

    {
      path: '/products',
      name: 'products',
      component: () => import('../views/products/Products.vue'),
      meta: {
        title: "Products",
      },
    },
    {
      path: '/items',
      name: 'items',
      component: () => import('../views/products/Items.vue'),
      meta: {
        title: "items",
      },
    } ,

    {
      path: '/category',
      name: 'category',
      component: () => import('../views/products/category.vue'),
      meta: {
        title: "category",
      },
    },

    {
      path: '/package',
      name: 'package',
      component: () => import('../views/products/package.vue'),
      meta: {
        title: "package",
      },
    },

// ADD PRODUCTS | DISABLED PRODUCTS | ADD PURCHASE

    {
      path: '/addproducts',
      name: 'addproducts',
      component: () => import('../views/products/productsAddForm.vue'),
      meta: {
        title: "addproducts",
      },
    },

    {
      path: '/disabled-products',
      name: 'disabled-products',
      component: () => import('../views/products/Disabled_Products.vue'),
      meta: {
        title: "Products",
      },
    },
    
    {
      path: '/addpurchase',
      name: 'addpurchase',
      component: () => import('../views/supply_chain/purchaseForm.vue'),
      meta: {
        title: "addpurchase",
      },
    },

// SUPPLY_CHAIN | SUPPLY_CHAIN | SUPPLY_CHAIN

    {
      path: '/warehouse',
      name: 'warehouse',
      component: () => import('../views/supply_chain/Warehouse.vue'),
      meta: {
        title: "Warehouse",
      },
    },

    {
      path: '/supply_reqs',
      name: 'supply_reqs',
      component: () => import('../views/supply_chain/Supply_Request.vue'),
      meta: {
        title: "Supply Request",
      },
    },

    {
      path: '/supplier',
      name: 'supplier',
      component: () => import('../views/supply_chain/supplier.vue'),
      meta: {                                                                                                                                                                             
        title: "supplier",
      },
    },

    {
      path: '/purchase',
      name: 'purchase',
      component: () => import('../views/supply_chain/purchase.vue'),
      meta: {
        title: "Journal",
      },
    },

    {
      path: '/deleted_sc',
      name: 'deleted_sc',
      component: () => import('../views/supply_chain/deletedSC.vue'),
      meta: {
        title: "Deleted Supply Chain",
      },
    },

    // LOGISTICS | LOGISTICS | LOGISTICS

  {
    path: '/trucks',
    name: 'trucks',
    component: () => import('../views/logistics/Trucks.vue'),
    meta: {
      title: "Trucks",
    },
  },

  {
    path: '/drivers',
    name: 'drivers',
    component: () => import('../views/logistics/Drivers.vue'),
    meta: {
      title: "Drivers",
    },
  },

// CUSTOMER | CUSTOMER | CUSTOMER

{
  path: '/customers',
  name: 'customers',
  component: () => import('../views/customers/Customer.vue'),
  meta: {
    title: "Customer",
  },
},

{
  path: '/transactions',
  name: 'transactions',
  component: () => import('../views/customers/Transactions.vue'),
  meta: {
    title: "Transactions",
  },
}

]
})
export default router
export function requireAuth(to, from, next) {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated()) {
      next({ name: 'Login' });
    } else {
      next();
    }
  } else {
    next();
  }
}
