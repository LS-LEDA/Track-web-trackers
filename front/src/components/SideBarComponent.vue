<template>
    <aside>
        Sidebar
    </aside>
</template>

<script>
</script>

<style>
aside {
    display: flex;
    flex-direction: column;
    width: calc(2rem + 35px);
    overflow: hidden;
    min-height: 10vh;
    padding: 1rem;
    transition: 0.3s ease-out;

    @media (max-width: 760px) {
        position: fixed;
    }
}
</style>