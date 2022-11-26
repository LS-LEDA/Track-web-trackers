<template>
    <div id="spinner" class="spinner">
        <img src="/loading.gif" alt="spinner img">
    </div>
</template>

<script>
export default {
    name: "SpinnerComponent",
    methods: {
        showSpinner() {
            document.getElementById("spinner").style.display = "block";
        },
        hideSpinner() {
            document.getElementById("spinner").style.display = "none";
        }
    }
}
</script>


<style scoped>
.spinner {
    position: absolute;
    top: 50%;
    left: 50%;
    margin-top: -50px;
    margin-left: -50px;
    width: 100px;
    height: 100px;
}
</style>
