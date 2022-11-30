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
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
}

.search-bar-container {
    float: left;
    width: 100%;
    padding-left: 3%;
    padding-right: 25%;
}


.search-bar {
    width: 100%;
    max-width: max(700px, 5em, 5rem);
    background: rgba(255, 255, 255, 0.6);
    display: flex;
    align-items: center;
    border-radius: 100px;
    padding: 5px 10px;
    backdrop-filter: blur(1px) saturate(180%);
}

.search-bar input {
    background: transparent;
    flex: 1;
    border: 0;
    outline: none;
    padding: 24px 20px;
    font-size: 20px;
    color: #000000;
}

::placeholder {
    color: #3f3e7a86;
}

.search-bar button img {
    width: 25px;
}

.search-bar button {
    border: 0;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    background: #58629b;
    cursor: pointer;
}
</style>
