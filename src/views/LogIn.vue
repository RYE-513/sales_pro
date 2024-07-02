<template>
  <div>
    <input v-model="username" type="text" placeholder="Username">
    <input v-model="password" type="password" placeholder="Password">
    <button @click="handleLogin">Login</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await axios.post('http://merge.localhost:8000/api/login/', {
          username: this.username,
          password: this.password
        });
        // Handle successful login
        console.log('Login successful');
        // You might save the authentication token here
      } catch (error) {
        // Handle login failure
        console.error('Login failed:', error.response.data);
      }
    }
  }
};
</script>
