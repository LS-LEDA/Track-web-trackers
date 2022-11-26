<template>
    <div class="card">
        <div class="column">
            <h2>{{ tracker.name }}</h2>
            <p>Website: {{ tracker.website }}</p>
            <p>Description: {{ tracker.description }}</p>
            <p>Categories: </p>
            <div v-for="category in tracker.categories" :key="category">
                <li>{{ category }}</li>
            </div>
            <p class="short-url">Event catch: {{ tracker.event_url }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: "TrackerComponent",
    props: {
        tracker: {
            categories: Array,
            description: String,
            event_url: String,
            name: String,
            website: String,
        }

    }
}
</script>

<style scoped>
.card {
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin: auto;
    margin-bottom: 15px;
    width: 500px;

}

.column {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
}

.short-url {
    overflow: hidden;
    text-overflow: ellipsis;
}
</style>