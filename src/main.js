// Import necessary stylesheets
import './assets/libs/jsvectormap/css/jsvectormap.min.css';
import './assets/css/bootstrap.min.css';
import './assets/css/icons.min.css';
import './assets/css/app.min.css';
import './assets/css/custom.min.css';
import './assets/libs/fullcalendar/main.min.css';
import './assets/libs/glightbox/css/glightbox.min.css';
import './assets/css/dataTables.bootstrap5.min.css'; 
import './assets/css/responsive.bootstrap.min.css'; 
import './assets/css/buttons.dataTables.min.css';

// Import Vue and Maska
import { createApp } from 'vue';
import App from './App.vue';
import router, { requireAuth } from './router';
// import Maska from 'maska';

// Import VueDatePicker component
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';

// Apply global navigation guard
router.beforeEach(requireAuth);

// Create Vue app instance
const app = createApp(App);

// Use router
app.use(router);

// Use Maska
// app.use(Maska);

// Mount the app to the element with id 'app'
app.mount('#app');

// Register VueDatePicker component globally
app.component('VueDatePicker', VueDatePicker);
