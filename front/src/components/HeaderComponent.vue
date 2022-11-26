<template>
    <div class="header">
        <SearchBarComponent />
    </div>
</template>

<script>
import SearchBarComponent from './SearchBarComponent.vue';
export default {
    name: "Header",
    components: { SearchBarComponent },
}
</script>


<style scoped>
.header {
    background-color: rgb(0, 9, 19);
    height: 100px;
    width: 100%;
    padding-top: 10px;
}
</style>
