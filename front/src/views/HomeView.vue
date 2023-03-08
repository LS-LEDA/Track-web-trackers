<template>
  <div class="background" >
    <div class="info-box-container" style ="z-index: 2;">
        <InfoBoxComponent style="margin-top: 1vh; margin-right: 0vh;"/>
    </div>
    <div class="container">
      <div class="title-container">
        <h1 class="header-title" :style="containerSyles">Project Web Tracker</h1>
      </div>
      <SearchBarComponent class="search-bar"/>
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

.background {
  width: 100%;
  position: fixed;
  z-index: -1;
  min-height: 100vh;
  background:conic-gradient(at right center, rgb(107, 122, 146), rgb(16, 27, 53), rgb(0, 0, 0));
  background-position: center;
  background-size: cover;
}

.container {
  position: relative;
  display: grid;
  z-index: 1;
}

.search-bar-container {
  display:inline-block;
  height: auto;
  margin-left: auto ;
  margin-right: auto;
  margin-top: calc(50vh - 25px);
  margin-bottom: auto;
  justify-content: center;
  align-items: center;
}

.title-container {
  margin-left: calc(50vw - 500px);
  margin-top: calc(50vh - 12.5vw);
  position: absolute;
  animation: nav-load 0.4s ease-in-out;
}

.header-title {
  position: absolute;
  color: rgb(255, 255, 255);
  font-size: max(8vw, 5em, 5rem);
  transition: 0.3s;
  font-family: 'Trebuchet MS';
  font-weight: bold;
  text-shadow: 10px;
}

.info-box-container {
  position: inherit;
  z-index: 2;
}

/*
.container {
  height: auto;
  width: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 1000px 5.5em;
  z-index: 1;
}

.info-box-container {
  margin-top: 30px;
  height: min-content;
  float: right;
  position: absolute;
}

@keyframes nav-load {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(0);
  }
}

@keyframes search-bar-container-load {
  0% {
    opacity: 0;
    transform: translateX(-100%);
    width: 50px;
  }

  100% {
    opacity: 1;
    transform: translateX(0);
    width: 100%;
  }
}

.title-container {
  align-items: center;
  margin-top: auto;
  margin-bottom: auto;
  position:relative;
  min-width: 100px;
  float: right;
  width: 30%;
  animation: nav-load 0.4s ease-in-out;
  z-index: 1;
}

.search-bar-container {
  opacity: 0;
  width: 50%;
  position: relative;
  margin: 0 auto;
  align-self:inherit;
  animation: search-bar-container-load 300ms ease-in 100ms;
  animation-fill-mode: forwards;
}

.header-title {
  color: rgba(236, 230, 255, 0.902);
  width: 80%;
  font-size: max(8vw, 5em, 5rem);
  transition: 0.3s;
  margin-left: 30%;
  font-family: 'Trebuchet MS';
  font-weight: bold;
  z-index: 1;
}

.header-title:hover {
  color: white;
}

/*
@media screen and (max-width: 1000px) {
  .background {
    position: fixed;
  }
  .container {
    height: 150vw;
  }

  .title-container {
    float: top;
    max-width: max(700px, 10em, 5rem);
    width: 100%;
  }

  .header-title {
    margin-left: 10%;
  }

  .search-bar-container {
    float: left;
    padding-top: 10px;
    padding-bottom: 10px;
  }

  .search-bar {
    margin-right: 20%;
    margin-top: 5%;
  }

  .container {
    display: block;
    min-width: 5.5em;
  }

  .search-bar button {
    width: 50px;
    transition: 0.3s;
  }

  .info-box-container {
    height: min-content;
    margin-left: 5%;
    margin-right: 3%;
  }

  .info-box-container * {
    z-index: 2;
    box-sizing:border-box;
  }

  .info-box-container .info-card {
      z-index: 2;
      position: relative;
  
      clip-path: circle(15px at 93% 17%);
      transition: all ease-in-out .3s;
      background-color:#ffffff;
      
      &__infoicon{
        position:absolute;
        margin-left: 417.5px;
        margin-top: 9.5px;
        color:#000000;
        transition:ease-out .3s;
      }

      &__title{
        position: relative;
        padding-top: 2%;
        margin: 5% 15% 3% 3%;
        font-size:4vh; 
        font-family: 'Trebuchet MS';
        
      }
      &__description{
        margin: 0% 0% 5% 3%;
        padding-bottom: 2%;
        
        font-size: 1.1em;
        font-family:'Poppins';
        line-height: 1.6em;
      }
      &__reference{
        display:inline-block;
        
        border-bottom: 1px solid transparent;
        color:#0099ff;
        text-decoration:none;
        transition: ease-in .3s;
        &:hover{
          border-bottom-color: #0099ff;
        }
      }
      
      &:hover, &:focus{
        clip-path: circle(100%);
        border-radius:20px;
        box-shadow: 0px 3px 9px rgba(0,0,0,0.12),
                    0px 3px 18px rgba(0,0,0,0.08);
        background:#ffffff;
        
        outline:none;
        .info-card__infoicon{
          opacity: 0;
        }
      }
      &:focus{
        box-shadow: 0px 3px 9px rgba(0,0,0,0.12), 
                    0px 3px 18px rgba(0,0,0,0.08), 
                    0px 0px 0px 4px rgba(0,0,0,0.2);
      }
    }
  }


::placeholder {
  color: #3f3e7a86;
}
*/
/*
.search-bar button {
  border: 0;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  background: #58629b;
  cursor: pointer;
  transition: 0.3;
}
*/
</style>
