<template>
  <div class="background">
    <div class="info-box-container" style="z-index: 2;">
      <InfoBoxComponent style="margin-top: 1vh; margin-right: 0vh;" />
    </div>
    <div class="component">
      <div class="container">
        <div class="title-grid">
          <h1 class="title-1 header-title">Project</h1>
          <h1 class="title-2 header-title ">Web</h1>
          <div class="search-bar-grid ">
            <div class="search-bar-container-out">
              <SearchBarComponent />
            </div>
          </div>
          <h1 class="title-3 header-title">Tracker</h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SearchBarComponent from "../components/SearchBarComponent.vue";
import InfoBoxComponent from "../components/InfoBoxComponent.vue";

export default {
  name: "HomeView",
  components: { SearchBarComponent, InfoBoxComponent },
  data() {
    return {
      containerSyles: {
        marginTop: '0'
      }
    };
  },
  mounted() {
    window.addEventListener("resize", this.checkWindowSize);
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.checkWindowSize);
  },
  methods: {
    checkWindowSize() {
      if (window.innerHeight >= window.innerWidth) {
        this.containerSyles = {
          marginRight: '50vw'
        };
      }
      else {
        this.containerSyles = {
          marginTop: '0vh'
        };
      }
    }
  }
};
</script>

<style lang="scss">
* {
  font-family: 'Trebuchet MS';
}

.component {
  margin: auto;
  margin-top: 10em;
  width: 50%;
}

.background {
  width: 100%;
  position: fixed;
  z-index: -1;
  min-height: 100vh;
  background: conic-gradient(at right center, rgb(107, 122, 146), rgb(16, 27, 53), rgb(0, 0, 0));
  background-position: center;
  background-size: cover;
}

.container {
  z-index: 1;
}

.search-bar-container {
  display: inline-block;
  height: auto;
  justify-content: center;
  align-items: center;
}

.search-bar-container-out {
  margin-left: 15px;
}

.title-container {
  animation: nav-load 0.4s ease-in-out;
}

.header-title {
  color: rgb(255, 255, 255);
  font-size: max(8vw, 5em, 5rem);
  transition: 0.3s;
  font-family: 'Trebuchet MS';
  font-weight: bold;
  text-shadow: 10px;
  line-height: 1.3;
}

.info-box-container {
  position: inherit;
  z-index: 2;
}

.title-1 {
  grid-area: top;
}

.title-2 {
  grid-area: middle-left;
}

.search-bar-grid {
  grid-area: middle-right;
  display: flex;
  align-items: center;
}

.title-3 {
  grid-area: bottom;
}

.title-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr 1fr;
  grid-template-areas:
    "top top top top"
    "middle-left middle-right middle-right middle-right"
    "bottom bottom bottom bottom";
}

@media only screen and (max-width: 790px) {
  .title-grid {
    grid-template-columns: 1fr;
    grid-template-areas:
      "top"
      "middle-left"
      "bottom"
      "middle-right";
    width: fit-content;
    margin: auto;
  }

  .component {
    width: 100%;
  }
}
</style>
