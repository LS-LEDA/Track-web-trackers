<template>
    <div id="header">
        <SearchBarComponent />
        <div class="toggle-container"><ThemeToggleComponent/></div>
    </div>
</template>

<script>
import SearchBarComponent from './SearchBarComponent.vue';
import ThemeToggleComponent from './ThemeToggleComponent.vue'
export default {
    name: "Header",
    components: { SearchBarComponent, ThemeToggleComponent },
}
</script>


<style scoped>
#header {
    background-image: conic-gradient(at right center, rgb(183, 199, 226), rgb(24, 42, 87),rgb(17, 35, 78));
    height: 60px;
    width: 100%;
    display: flex;
    align-items: center;
}

.toggle-container {
    float: left;
    margin-top: auto;
    margin-bottom: auto;
}
</style>
