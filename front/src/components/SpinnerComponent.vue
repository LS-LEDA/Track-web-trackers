<template>
    <div id="spinner" class="spinner">
        <img src="/animat-search-color.gif" alt="spinner img" class="loading-gif">
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
    margin-left: auto;
    margin-right: auto;
}

.loading-gif {
    display: block;
    margin-left: auto;
    margin-right: auto;
    margin-top: auto;
    margin-bottom: auto;
    width: 250px;
}
</style>
