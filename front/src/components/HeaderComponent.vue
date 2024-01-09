<template>
    <div id="header">
        <LogoComponent/>
        <SearchBarComponent />
        <div class="toggle-container"><ThemeToggleComponent/></div>
        <SideBarComponent/>
    </div>
</template>

<script>
import SearchBarComponent from './SearchBarComponent.vue';
import ThemeToggleComponent from './ThemeToggleComponent.vue'
import SideBarComponent from "./SideBarComponent.vue";
import LogoComponent from './LogoComponent.vue';
export default {
    name: "Header",
    components: { SearchBarComponent, ThemeToggleComponent, SideBarComponent, LogoComponent },
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
    align-items: center;
    margin-left: 10px;
}
</style>
