<script>
import { ref } from 'vue';
import { RouterLink, RouterView } from 'vue-router';
import isSidebarVisible from '../../App.vue'

export default {
  name: 'Nav',
  props: {
    visible: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<template>
<div v-if="visible" class="sidebar" >
<div class="app-menu navbar-menu">
    <!-- LOGO -->
    <div class="navbar-brand-box">
        <!-- Dark Logo-->
        <a href="index.html" class="logo logo-dark">
            <span class="logo-sm">
                <img src="" alt="" height="22">
            </span>
            <span class="logo-lg">
                <img src="" alt="" height="17">
            </span>
        </a>
        <!-- Light Logo-->
        <a href="index.html" class="logo logo-light">
            <span class="logo-sm">
                <img src="" alt="" height="22">
            </span>
            <span class="logo-lg">
                <img src="" alt="" height="17">
            </span>
        </a>
        <button type="button" class="btn btn-sm p-0 fs-20 header-item float-end btn-vertical-sm-hover" id="vertical-hover">
            <i class="ri-record-circle-line"></i>
        </button>
    </div>

    <div class="dropdown sidebar-user m-1 rounded">
        <button type="button" class="btn material-shadow-none" id="page-header-user-dropdown" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="d-flex align-items-center gap-2">
                <img class="rounded header-profile-user" src="/favicon.ico" alt="Header Avatar">
                <span class="text-start">
                    <span class="d-block fw-medium sidebar-user-name-text">SALES PRO</span>
                </span>
            </span>
        </button>
    </div>

    <div id="scrollbar">
        <div class="container-fluid">
            <div id="two-column-menu">
            </div>
            <ul class="navbar-nav" id="navbar-nav">
                <!-- <li class="menu-title"><span data-key="t-menu">Menu</span></li> -->

                <!-- <li class="nav-item"> 
                    <a class="nav-link menu-link" href="#sidebarDashboards" data-bs-toggle="collapse" role="button" aria-expanded="false" aria-controls="sidebarDashboards"> 
                        <i class="ri-dashboard-2-line"></i> <span data-key="t-dashboards">Dashboard</span> 
                    </a>
                </li> -->

                <li class="nav-item">
                    <a class="nav-link menu-link" href="#sidebarBranches" data-bs-toggle="collapse" role="button" aria-expanded="false" aria-controls="sidebarDashboards">
                        <i class="ri-honour-line"></i> <span data-key="t-dashboards">Branches</span>
                    </a>
                    
                    <div class="collapse menu-dropdown" id="sidebarBranches">
                        <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                                <RouterLink to="/branches" class="nav-link" data-key="t-analytics">Branch</RouterLink>
                                <!-- <RouterLink to="/deleted_branches" class="nav-link" data-key="t-analytics">Deleted</RouterLink> -->
                            </li>

                        </ul>
                    </div>
                </li>

                <li class="nav-item">
                    <a class="nav-link menu-link" href="#sidebarHR" data-bs-toggle="collapse" role="button" aria-expanded="false" aria-controls="sidebarLayouts">
                        <i class="ri-account-circle-line"></i> <span data-key="t-apps">Human Resources</span>
                    </a>

                    <div class="collapse menu-dropdown" id="sidebarHR">
                        <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                                <RouterLink to="/roles" class="nav-link" data-key="t-analytics">Roles</RouterLink>
                                <RouterLink to="/staff" class="nav-link" data-key="t-analytics">Staff</RouterLink>
                                <!-- <RouterLink to="/deleted_hr" class="nav-link" data-key="t-analytics">Deleted</RouterLink> -->
                            </li>
                        </ul>
                    </div>
                </li>

                <!-- <li class="nav-item">
                    <a class="nav-link menu-link" href="#sidebarProducts" data-bs-toggle="collapse" role="button" aria-expanded="false" aria-controls="sidebarDashboards">
                        <i class="ri-dashboard-2-line"></i> <span data-key="t-dashboards">Products</span>
                    </a>
                    <div class="collapse menu-dropdown" id="sidebarProducts">
                        <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                                <RouterLink to="/products" class="nav-link" data-key="t-analytics"> Products </RouterLink>
                                <RouterLink to="/items" class="nav-link" data-key="t-analytics"> Items </RouterLink>
                                <RouterLink to="/category" class="nav-link" data-key="t-analytics"> Categories </RouterLink>
                                <RouterLink to="/package" class="nav-link" data-key="t-analytics"> Packages </RouterLink>
                            </li>
                        </ul>
                    </div>
                </li> -->

                <li class="nav-item">
                    <a class="nav-link menu-link" href="#sidebarSupplyChain" data-bs-toggle="collapse" role="button" aria-expanded="false" aria-controls="sidebarLayouts">
                        <i class="ri-stack-line"></i> <span data-key="t-apps">Supply Chain</span>
                    </a>
                    <div class="collapse menu-dropdown" id="sidebarSupplyChain">
                        <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                                <RouterLink to="/warehouse" class="nav-link" data-key="t-analytics">Warehousing</RouterLink>
                                <RouterLink to="/supply_reqs" class="nav-link" data-key="t-analytics">Supply Request</RouterLink>
                                <!-- <RouterLink to="/supplier" class="nav-link" data-key="t-analytics">Supplier</RouterLink>
                                <RouterLink to="/purchase" class="nav-link" data-key="t-analytics">Purchase</RouterLink> -->
                                <!-- <RouterLink to="/stock_receivables" class="nav-link" data-key="t-analytics">Stock Receivables</RouterLink> -->
                                <!-- <RouterLink to="/deleted_sc" class="nav-link" data-key="t-analytics">Deleted</RouterLink> -->
                            </li>
                        </ul>
                    </div>
                </li>

                <li class="nav-item">
                    <a class="nav-link menu-link" href="#sidebarLogistics" data-bs-toggle="collapse" role="button" aria-expanded="false" aria-controls="sidebarLayouts">
                        <i class="ri-truck-line"></i> <span data-key="t-apps">Logistics</span>
                    </a>

                    <div class="collapse menu-dropdown" id="sidebarLogistics">
                        <ul class="nav nav-sm flex-column">
                            <li class="nav-item">
                                <RouterLink to="/trucks" class="nav-link" data-key="t-analytics">Trucks</RouterLink>
                                <RouterLink to="/drivers" class="nav-link" data-key="t-analytics">Drivers</RouterLink>
                            </li>
                        </ul>
                    </div>
                </li>

                <li class="nav-item">
                    <RouterLink to="/customers" class="nav-link menu-link" data-key="t-apps">
                        <i class="ri-user-3-line"></i><span data-key="t-analytics">Customer</span>
                    </RouterLink>
                </li>

            </ul> 
        </div>
    </div>
</div>
    <div class="sidebar-background"></div>
</div>
<div class="vertical-overlay"></div>
</template>
