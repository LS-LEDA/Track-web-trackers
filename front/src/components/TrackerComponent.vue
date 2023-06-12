<template >
    <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
    <div class="card">

        <body>
            <div class="column">
                <div class="multi-button">
                    <button id="btn-home" class="btn-child" v-on:click="location.href = tracker.website">
                        <a v-bind:href="tracker.website" target="_blank">
                            <div class="img-home"></div>
                        </a>
                    </button>
                    <button id="btn-2" class="btn-child" v-on:click="shareTracker">
                        <a v-bind:href="tracker.description" target="_blank">
                            <div class="img-send"></div>
                        </a>
                    </button>
                    <button id="btn-download" class="btn-child" v-on:click="downloadTracker">
                        <div class="img-download"></div>
                    </button>
                </div>
                <div class="card-header">
                    <div><img class="logo" :src="getLogo(tracker.website)" alt="Logo"></div>
                    <h2 class="card-title">{{ tracker.name }}</h2>
                </div>

                <div v-for="category in tracker.categories" :key="category">
                    <ul class="category-container">
                        <div v-if="category != null">
                            <li>
                                <p style="font-weight: bold;">Categories:</p>
                            </li>
                            <li>
                                <p style="font-weight: lighter;">{{ category }}</p>
                            </li>
                        </div>
                        <div v-else>
                            <li>
                                <p style="font-weight: bold;">Categories:</p>
                            </li>
                            <li>
                                <p style="font-weight: lighter;"> no categories found</p>
                            </li>
                        </div>

                    </ul>
                </div>

                <button v-on:click="showMore = !showMore" class="btn-mr btn-rq">Show requests identified</button>
                <div v-if="showMore" :class="{ 'show': showMore }">
                    <p style="font-family: 'Trebuchet MS';">Number of requests: {{ tracker.event_url.length }}</p>
                    <div v-for="tracked_url in tracker.event_url" :key="tracked_url">
                        <li class="short-url">
                            <lu>{{ tracked_url }}</lu>
                        </li>
                    </div>
                    <a v-on:click="downloadTracker" style="display: flex; justify-content: center;">Download to see full
                        info</a>
                </div>
            </div>
        </body>
    </div>
</template>

<script>

export default {
    name: "TrackerComponent",
    props: {
        tracker: {
            categories: Array,
            description: String,
            event_url: Array,
            name: String,
            website: String,
        }
    },
    data() {
        return {
            showMore: false
        }
    },
    methods: {
        getLogo(website) {
            let url = website;
            let domainName = new URL(url).hostname;
            let logoURL = 'https://logo.clearbit.com/' + domainName;
            if (logoURL.includes('google')) {
                logoURL = '/google.png'
            }
            return logoURL;
        },

        shareTracker() {
            let url = window.location.href;
            navigator.clipboard.writeText(url);
            alert("URL on your clipboard to share it!")
            return false;
        },

        downloadTracker() {
            const tracker = this.tracker;
            const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(tracker));
            const downloadAnchorNode = document.createElement('a');
            downloadAnchorNode.setAttribute("href", dataStr);
            downloadAnchorNode.setAttribute("download", "tracker.json");
            document.body.appendChild(downloadAnchorNode); // required for firefox
            downloadAnchorNode.click();
            downloadAnchorNode.remove();
        }
    }
}
</script>

<style lang="scss">
.category-container {
    align-items: center;
    font-family: 'Trebuchet MS';
    margin-top: 5px;
    margin-bottom: 10px;
}

.category-container li {
    display: inline-block;
    padding-right: 5px;
    font-family: 'Trebuchet MS';
    font-weight: lighter;
}

.btn-mr {
    display: inline-block;
    background-color: transparent;
    width: 41.5%;
    padding-right: 5px;
    padding: 0;
    font-size: 15px;
    font-weight: normal;
    color: black;
    border: none;
    box-shadow: none;
    border-radius: 10px;
    transition: 0.3s ease-in-out;
}

.btn-mr:hover {
    background-color: #0065b3;
    color: white;
}

.btn-mr:active {
    background-color: #005599;
}

@keyframes cards-load {
    0% {
        margin-top: 100%;
        opacity: 0;
    }

    100% {
        margin-top: 0;
        opacity: 1;
    }
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

.card-header {
    display: inline-block;
}

.logo {
    height: 60px;
    width: 60px;
    float: left;
    mix-blend-mode: multiply;
}

.card-title {
    margin-top: 25px;
    margin-bottom: 25px;
    padding-left: 90px;
    font-family: 'Trebuchet MS';
    font-weight: bold;
    font-size: 20px;
}

.img-home {
    background-image: url(/home.svg);
    height: 13px;
    width: 13px;
    margin-bottom: 1.5px;
    margin-right: 1px;

    &:hover {
        filter: invert(100%);
    }
}

.img-send {
    background-image: url(/send.svg);
    height: 13px;
    width: 13px;
    margin-bottom: 1px;
    margin-left: 2px;

    &:hover {
        filter: invert(100%);
    }
}

.img-download {
    background-image: url(/download.svg);
    height: 13px;
    width: 13px;
    margin-bottom: 1px;
    margin-right: 1px;

    &:hover {
        filter: invert(100%);
    }
}

.card:not(:hover) .btn-child {
    opacity: 0;
}

.card {
    --background: #FFFFFF;
    --text: rgb(38, 38, 38);
    position: relative;
    flex: 1;
    min-width: 300px;
    margin: 10px;
    display: block;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.365);
    padding: 20px;
    margin: auto;
    margin-bottom: 15px;
    width: 500px;
    min-height: 170px;
    z-index: 2;
    animation: cards-load 0.4s ease-out;

    &:hover {
        box-shadow: 0px 0px 40px -17px rgba(0, 0, 0, 0.62);
        transition: 0.15s;
    }

    .multi-button {
        z-index: 0;
        position: absolute;
        top: 1.25rem;
        left: 1.25rem;
        border-radius: 100%;
        width: 0rem;
        height: 0rem;
        transform: translate(-50%, -50%);
        transition: .25s cubic-bezier(0.25, 0, 0, 1);

        button {
            display: grid;
            place-items: center;
            position: absolute;
            width: 2rem;
            height: 2rem;
            border: none;
            border-radius: 100%;
            background: var(--background);
            box-shadow: 0 0 1rem -.25rem rgba(0, 0, 0, 0.365);
            color: var(--text);
            transform: translate(-50%, -50%);
            cursor: pointer;
            transition: .25s cubic-bezier(0.25, 0, 0, 1);
            z-index: 1;

            &:hover {
                background: var(--text);
                color: var(--background);
                box-shadow: 0 0 1rem -.25rem white;
            }

            &:first-child:nth-last-child(1) {
                //If there is 1 child
                left: 25%;
                top: 25%;
            }

            &:first-child:nth-last-child(2),
            &:first-child:nth-last-child(2)~* {

                //If there are 2 children
                &:nth-child(1) {
                    left: 37.5%;
                    top: 18.75%;
                }

                &:nth-child(2) {
                    left: 18.75%;
                    top: 37.5%;
                }
            }

            &:first-child:nth-last-child(3),
            &:first-child:nth-last-child(3)~* {

                //If there are 3 children
                &:nth-child(1) {
                    left: 50%;
                    top: 15.625%;
                }

                &:nth-child(2) {
                    left: 25%;
                    top: 25%;
                }

                &:nth-child(3) {
                    left: 15.625%;
                    top: 50%;
                }
            }

            &:first-child:nth-last-child(4),
            //If there are 4 children, if first child is also 4th item from bottom get self, and
            &:first-child:nth-last-child(4)~* {

                //If there are 4 children, if first child is also 4th item from bottom get siblings
                &:nth-child(1) {
                    left: 62.5%;
                    top: 18.75%;
                }

                &:nth-child(2) {
                    left: 37.5%;
                    top: 18.75%;
                }

                &:nth-child(3) {
                    left: 18.75%;
                    top: 37.5%;
                }

                &:nth-child(4) {
                    left: 18.75%;
                    top: 62.5%;
                }
            }
        }
    }

    .container {
        position: absolute;
        width: 100%;
        height: 100%;
        border-radius: 1rem;
        background: var(--background);
        color: var(--text);
    }

    &:hover .multi-button,
    .multi-button:focus-within {
        //Hover or a button inside is focused
        width: 10rem;
        height: 10rem;
    }
}

@media (max-width: 800px) {
    .menu-item {
        flex: 1 0 calc(50% - 20px);
        transition: 0.2s;
    }

    .card {
        width: auto
    }
}

/* Responsive layout for screens smaller than 600px */
@media (max-width: 600px) {
    .menu-item {
        flex: 1 0 100%;
        transition: 0.2s;
    }
}

.btn-rq {
    margin: auto;
    color: white;
    background: #7ba8d4;
    padding: 10px;
}

.btn-rq:hover {
    background: #0065b3;
}
</style>
