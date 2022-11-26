
<template>
    <HeaderComponent />

    <SpinnerComponent id="spinner" />

    <div id="content">
        <h1> Results</h1>

        <div v-if="trackers.length > 0">
            <div v-for="tracker in trackers" :key="tracker.id">
                <TrackerComponent :tracker="tracker" />
            </div>
        </div>
        <div v-if="trackers.length == 0">
            <p> No trackers found </p>
        </div>
    </div>

</template>

<script>
import axios from "axios";
import TrackerComponent from "../components/TrackerComponent.vue";
import HeaderComponent from "../components/HeaderComponent.vue";
import SpinnerComponent from "../components/SpinnerComponent.vue";

export default {
    name: "ResultView",
    components: { TrackerComponent, HeaderComponent, SpinnerComponent },
    props: {
        url: String,
    },

    data() {
        return {
            trackers: Array
        }
    },

    mounted() {
        document.getElementById("content").style.display = "none";
        SpinnerComponent.methods.showSpinner();

        const options = {
            method: "GET",
            url: `${import.meta.env.VITE_TRACKERS_API}${this.$route.params.url}`,
        };

        axios.request(options)
            .then(response => {
                this.trackers = response.data
                SpinnerComponent.methods.hideSpinner();
                document.getElementById("content").style.display = "block";
            })

    },

    // if url changed, call api again
    watch: {
        $route(to, from) {
            document.getElementById("content").style.display = "none";
            SpinnerComponent.methods.showSpinner();
            const options = {
                method: "GET",
                url: `${import.meta.env.VITE_TRACKERS_API}${this.$route.params.url}`,
            };

            axios.request(options)
                .then(response => {
                    this.trackers = response.data
                    SpinnerComponent.methods.hideSpinner();
                    document.getElementById("content").style.display = "block";
                })
        }
    }

}
</script>