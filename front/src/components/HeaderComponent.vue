<template>
    <div class="header">
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
.header {
    background-image: linear-gradient(rgb(1, 10, 20), rgba(0, 8, 51, 0.2)),
    url(/background.jpg);
    height: 80px;
    width: 100%;
    display: flex;
    align-items:initial;
}

.search-bar-container {
    margin-top: auto;
    margin-bottom: auto;
    margin-left: 10px;
    margin-right: 10px;
}

.search-bar {
    margin-top: auto;
    margin-bottom: auto;
}
.toggle-container {
    margin: 10px 10px 10px;
    margin-right: 20px;
    margin-top: auto;
    margin-bottom: auto;
}
</style>
