<template>
    <div class="main-container" style="z-index:1">
        <HeaderComponent/>
        
        <InfoBoxComponent class="info-box-container" style="z-index: 2; position: absolute"/>
        <SpinnerComponent id="spinner" />
        <div id="content" class="content-container" style="z-index:1; position: relative;">
            <!--h1 class="results-title" style="z-index:1;"> Results</h1-->
            <div v-if="trackers.length > 0" style="z-index:1;">
                <ul class="results">
                    <li><p id="tf" class="results-title">Trackers found: </p></li>
                    <li><p class="trackers-found"> {{ trackers.length }}</p></li>
                </ul>
                <ul class="btn-download-js-container">
                    <button id="btn-download-js">
                        <div id="img-download"></div>
                        <p class="hover-text">Download JSON</p>
                    </button>
                </ul>
                <div class="cards-container">
                    <div v-for="tracker in trackers" :key="tracker.id" style="z-index:1;">
                        <TrackerComponent :tracker="tracker" class="card"/>
                    </div>
                </div>
            </div>
            <div v-if="trackers.length == 0" style="z-index:1;">
                <p id="nt"> No trackers found </p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import TrackerComponent from "../components/TrackerComponent.vue";
import HeaderComponent from "../components/HeaderComponent.vue";
import SpinnerComponent from "../components/SpinnerComponent.vue";
import InfoBoxComponent from "../components/InfoBoxComponent.vue";

export default {
    name: "ResultView",
    components: { TrackerComponent, HeaderComponent, SpinnerComponent, InfoBoxComponent },
    props: {
        url: String,
    },

    data() {
        return {
            trackers: Array
        }
    },

    methods : {
        showCrads : function() {
        var cards = document.getElementsByClassName("card");
        var delay = 0;

        for (var i = 0; i < cards.length; i++) {
            cards[i].style.position = "absolute";
            cards[i].style.bottom = "-100px";
            cards[i].style.transition = "all 0.2s ease-in-out";
            /*
            setTimeout(function() {
                cards[i].style.bottom = "0px";
            }, delay);
            delay += 200;
            */
        }
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
                this.showCrads();
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

/**Toggle Theme*/
const body = document.querySelector("body");
const sunIcon = document.querySelector(".toggle .bxs-sun");
const moonIcon = document.querySelector(".toggle .bx-moon");
</script>

<style lang="scss">
#spinner {
    margin-top: 15%;
}
.btn-download-js-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 30px;
    margin-left: 35px;
}

.hover-text {
    visibility: hidden;
    opacity: 0;
}
#btn-download-js {
    display: flex;
    position: absolute;
    align-items: center;
    width:35px;
    height:35px;
    border: none;
    padding-left: 10px;
    border-radius:35px;
    background:var(--background);
    box-shadow:0 0 1rem -.25rem rgba(0, 0, 0, 0.475);
    color:var(--text);
    transform: translate(-50%, -50%);
    cursor: pointer;
    text-align: center;
    transition: 0.2s cubic-bezier(0.25, 0, 0, 1);
    #img-download {
        position: fixed;
        background-image: url(/download.svg);
        height: 13px;
        width: 13px;
        visibility: visible;
        opacity: 1;
        &:hover {
            filter: invert(70%);
        }
    }
    &:hover{
        width: 150px;
        margin-left: 120px;
        color: black;
        transition: 0.2s ease-out;
        stroke-width: 4;
        stroke-dasharray: 100, 500;
        stroke-dashoffset: 0;
    }
    &:hover .hover-text {
        margin-left: 23px;
        visibility: visible;
        opacity: 1;
        transition: 0.1s;
        transition-delay: 0.2s;
    }
}



.main-conatiner {
    position: absolute;
}
.card {
    transform: translateY(10px);
    transition: all 0.3s ease-in-out;
}
.results {
    align-items: center;
    text-align: center;
    margin-bottom: 10px;
    animation: title-load 0.35s ease-out;
}
.results li{
    display: inline-block;
    padding-right: 5px;
}

#nt {
    margin-bottom: 20px;
    text-align: center;
    font-size: 25px;
    font-family: 'Trebuchet MS';
}

@keyframes title-load {
    0% {
        margin-right: 100%;
    }
    100% {
        margin-right: 0%;
    }
}
.results-title {
    margin-bottom: 20px;
    text-align: center;
    font-size: 25px;
    font-family: 'Trebuchet MS';
}

.trackers-found {
    margin-bottom: 20px;
    text-align: center;
    font-size: 25px;
    font-family: 'Trebuchet MS';
    font-weight: bolder;
    background: -webkit-linear-gradient(rgb(1, 103, 255), rgb(0, 203, 176));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.cards-container {
    margin-left:50px;
    margin-right:50px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    grid-gap: 1rem;
    row-gap: 0.25rem;
    align-items: center;
    justify-content: center;
}

.cards-container:hover > .cards-container {
    opacity: 0.8;
    filter: blur(10px);
}

.content-container:hover .card {
    opacity: 0.8;
    filter: blur(5px);
}

.content-container .card:hover {
    opacity: 1;
    filter: blur(0px);
}

.content-container {
    position: absolute;
    margin-top: 5vh
}

.info-box-container {
    height: auto;
    width: 700px;
    margin-top: 2vh;
    margin-left: calc(100vw - 730px);
}

</style>