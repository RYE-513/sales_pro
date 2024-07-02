let currentUser = null;

export function login(username, password) {
  if (username === 'user' && password === 'password') {
    currentUser = { username };
    return true;
  }
  return false;
}

export function logout() {
  currentUser = null;
}

export function isAuthenticated() {
  return currentUser !== null;
}

export function getCurrentUser() {
  return currentUser;
}