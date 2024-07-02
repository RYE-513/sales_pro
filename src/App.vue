<script setup>
import { ref } from 'vue';
import { RouterLink, RouterView } from 'vue-router';
import NavBar from './views/includes/Nav.vue';
import Header from './views/includes/Header.vue';

const isSidebarVisible = ref(true);

function toggleSidebar() {
  isSidebarVisible.value = !isSidebarVisible.value;
  console.log(isSidebarVisible.value);
}
</script>

<template>
  <div id="layout-wrapper">
    <Header @toggle-menu="toggleSidebar" />
    <div class="nav-wrapper">
      <NavBar :visible="isSidebarVisible" />
    </div>
    <div class="main-content">
      <div class="page-content">
        <div class="container-fluid">
          <RouterView />
        </div>
      </div>
    </div>
  </div>
</template>

<style>

</style>

<script>
import './assets/libs/bootstrap/js/bootstrap.bundle.min.js';
import './assets/libs/simplebar/simplebar.min.js';
// import './assets/libs/node-waves/waves.min.js';
import './assets/libs/feather-icons/feather.min.js';
import './assets/js/pages/plugins/lord-icon-2.1.0.js';
import './assets/js/plugins.js';
// import './assets/libs/cleave.js/cleave.min.js';
import './assets/js/pages/form-masks.init.js';
// import './assets/js/app.js';
import './assets/js/pages/datatables.init.js';
import './assets/libs/fullcalendar/main.min.js';
import './assets/libs/glightbox/js/glightbox.min.js';
import './assets/js/pages/file-manager.init.js';
import "https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js";
import "https://cdn.datatables.net/1.11.5/js/dataTables.bootstrap5.min.js";
import "https://cdn.datatables.net/responsive/2.2.9/js/dataTables.responsive.min.js";
</script>

<style></style>