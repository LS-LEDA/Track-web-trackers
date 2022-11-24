<template>
  <div class="container">
    <div class="title-container">
      <h1 class="header-title">Projecte Web Trackers</h1>
    </div>
    <div class="search-bar-container">
      <form v-on:submit="searchForTrackers" class="search-bar">
        <input type="text" placeholder="search tracker" name="urlToAnalyse" id="urlToAnalyse" v-model="urlToAnalyse" />
        <button type="submit">
          <img src="https://www.pngall.com/wp-content/uploads/8/Vector-Search.png" alt="search button" />
        </button>
      </form>
    </div>
    <div class="spinner hide" id="spinner">
      <img src="/loading.gif" alt="loading" />
    </div>
  </div>

</template>

<script>
import axios from "axios";

export default {
  name: "HomeView",
  components: {},
  data() {
    return {
      urlToAnalyse: null,
    };
  },
  methods: {
    fillTrackersList(trackers) {
      this.trackers = trackers;
    },
    async searchForTrackers(e) {
      e.preventDefault();

      const spinner = document.getElementById("spinner");
      spinner.classList.remove("hide");

      const options = {
        method: "GET",
        url: `${import.meta.env.VITE_TRACKERS_API}${this.urlToAnalyse}`,
      };

      const data = await axios.request(options);
      const trackers = data.data;
      console.log(trackers);

      // hide spinner
      spinner.classList.add("hide");
    },
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

.container {
  width: 100%;
  min-height: 100vh;
  padding: 10%;
  background-image: linear-gradient(rgb(1, 10, 20), rgba(0, 8, 51, 0.2)),
    url(/background.jpg);
  background-position: center;
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 1000px;
  /* Suppose you want minimum width of 1000px */
}

.title-container {
  align-items: center;
  min-width: 100px;
  padding: 20px;
  float: left;
  width: 30%;
}

.header-title {
  color: rgb(236, 230, 255);
  width: 80%;
  font-size: max(7vw, 5em, 5rem);
}

.search-bar-container {
  float: left;
  width: 100%;
  padding-left: 3%;
  padding-right: 25%;
}

@media screen and (max-width: 1000px) {

  .title-container,
  .search-bar-container {
    width: 100%;
    padding: 20px 0px;
  }

  .container {
    display: block;
  }
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

.hide {
  display: none;
}
</style>
