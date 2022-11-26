<template>
  <div class="container">
    <div class="title-container">
      <h1 class="header-title">Projecte Web Trackers</h1>
    </div>
    <SearchBarComponent />
  </div>

</template>

<script>
import SearchBarComponent from "../components/SearchBarComponent.vue";

export default {
  name: "HomeView",
  components: { SearchBarComponent },
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



::placeholder {
  color: #3f3e7a86;
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
