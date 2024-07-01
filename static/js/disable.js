

const resinfo = document.getElementById('resinfo');
const input = document.getElementById('landline');
input.addEventListener("keypress", (e) => {
    console.log(e.currentTarget.value);
});