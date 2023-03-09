<template>
    <div class="header">
        <div class="icon-container">
            <router-link to="/">
                <img src="/icon.png" alt="logo" />
            </router-link>
        </div>
        <SearchBarComponent v-if="showSearch == true" />
        <div class=" toggle-container">
            <ThemeToggleComponent />
        </div>
    </div>
</template>

<script>
import SearchBarComponent from './SearchBarComponent.vue';
import ThemeToggleComponent from './ThemeToggleComponent.vue'
export default {
    name: "Header",
    components: { SearchBarComponent, ThemeToggleComponent },
    props: {
        showSearch: {
            type: Boolean,
            default: true
        }
    },
}
</script>

<style scoped>
.icon-container {
    margin-top: auto;
    margin-bottom: auto;
    margin-left: 10px;
    margin-right: 10px;
    height: 60px;
    width: 60px;
    display: inline-block;
    overflow: hidden;
}

.icon-container img {
    width: 100%
}

.header {
    background-image: conic-gradient(at right center, rgb(183, 199, 226), rgb(24, 42, 87), rgb(17, 35, 78));
    height: 80px;
    width: 100%;
    display: flex;
    align-items: initial;
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
    float: left;
    margin-top: auto;
    margin-bottom: auto;
}
</style>
