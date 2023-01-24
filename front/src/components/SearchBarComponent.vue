<template>
    <div class="search-bar-container">
        <form v-on:submit="navigateToResults" class="search-bar">
            <input type="text" placeholder="search tracker" name="urlToAnalyse" id="urlToAnalyse"
                v-model="urlToAnalyse" />
            <button type="submit">
                <img src="https://www.pngall.com/wp-content/uploads/8/Vector-Search.png" alt="search button" />
            </button>
        </form>
    </div>
</template>

<script>
export default {
    name: "SearchBarComponent",
    props: {
        url: String,
    },
    data() {
        return {
            urlToAnalyse: null,
        };
    },
    methods: {
        navigateToResults(e) {
            e.preventDefault();
            this.$router.push({ name: "results", params: { url: this.urlToAnalyse.replace(/\./g, '%2E') } });
        },
    },
}
</script>


<style scoped>
* {
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
}

.search-bar-container {
    float: center;
}


.search-bar {
    max-height: 55px;
    max-width: max(600px, 5em, 5rem);
    background: rgba(255, 255, 255, 0.6);
    display: flex;
    align-items: center;
    border-radius: 100px;
    backdrop-filter: blur(1px) saturate(180%);
    transition: 0.3s;
}

.search-bar:hover {
    background-color: white;
}

.search-bar input {
    -webkit-background-composite: clear;
    background-color: transparent;
    flex: 1;
    border: 0;
    outline: none;
    padding: 0px 20px;
    font-size: 17px;
    color: black;
}

::placeholder {
    color: #3f3e7a86;
}

.search-bar button img {
    width: 20px;
    filter: invert(100%);
}

.search-bar button {
    border: 0;
    border-radius: 50%;
    width: 50px;
    height: 50px;
    background: linear-gradient(to left top, rgb(59, 130, 246), rgb(147, 51, 234));
    cursor: pointer;
}

.search-bar button:hover {
    background: linear-gradient(to left top, rgb(134, 239, 172), rgb(59, 130, 246), rgb(147, 51, 234));
    transition: all 0.15s ease-out;
}
.search-bar button:active{
    background: linear-gradient(to left top, rgb(134, 239, 172), rgb(59, 130, 246));
    transition: all 0.15s ease-out;
}
</style>
