<template>
    <div class="accordion" @click="toggleAccordion">
        <img :src="image" alt="Accordion image" class="accordion-img" />
        <h2 class="accordion-title txt">{{ title }}</h2>
        <span class="accordion-state-icon" :class="{ 'rotate': isOpen }">&#9660;</span>
    </div>
    <div v-show="isOpen" class="accordion-content">
        <slot></slot>
    </div>
</template>

<script>

export default {
    props: {
        image: String,
        title: String
    },
    data() {
        return {
            isOpen: false
        };
    },
    methods: {
        toggleAccordion(){
            this.isOpen = !this.isOpen;
        }
    },
};

</script>

<style lang="scss"> /**scoped vol dir que les regles en auqets style sol s'apliquen aquí */
* {
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}
.accordion {
    display: flex;
    width: 100%;
    align-items: center;
    padding: 10px;
    border-radius: 10px;
    transition: 0.1s;

    &:hover {
        background-color: grey;
    }

    .accordion-img {
        width: 20px;
    }

    .accordion-title {
        margin-left: 10px;
    }
}
</style>