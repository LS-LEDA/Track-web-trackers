<template>
    <div id="header">
        <img id="header-logo" src="/main-logo.svg"/>
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


<style lang="scss">
:root {
    --header-background: linear-gradient(to right, rgb(165, 180, 252), rgb(192, 132, 252));
}

#header {
    background: var(--header-background);
    height: 60px;
    width: 100%;
    display: flex;
    align-items: center;

    #header-logo {
        width: 65px;
    }
}

.toggle-container {
    float: left;
    margin-top: auto;
    margin-bottom: auto;
}
</style>
