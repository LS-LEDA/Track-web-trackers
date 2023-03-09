<template>
  <div id="ic" class="info-card" tabindex="0">
    <span class="info-card-wrap">
      <span class="info-card__infoicon">
        <img id="info-icon" src="https://img.icons8.com/ios-glyphs/512/information.png" style="width:20px">
      </span>
    </span>

    <h1 class="info-card__title">
      <div class="title-button">
        <p>Project Web Tracker</p>
        <button class="btn-about" v-on:click="about">About</button>

      </div>
    </h1>
    <p class="info-card__description">This is the Web Tracker Project. Type any URL in the search bar to know if the site
      has any tracker.</p>
  </div>
</template>

<script>
export default {
  name: "InfoBoxComponent",
  methods: {
    about() {
      this.$router.push('/about');
    }
  }
}
</script>

<style lang="scss">
* {
  z-index: 2;
  box-sizing: border-box;
}

.title-button {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
}

.btn-about {
  background-color: #4CAF50;
  border-radius: 5px;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  color: white;
  font-weight: bold;
}

.btn-about:hover {
  background-color: #3e8e41;
}

.info-card {
  z-index: 2;
  position: absolute;

  clip-path: circle(13px at calc(100% - 13px) 13px);
  transition: all ease-in-out .3s;
  background-color: #ffffff;

  &__infoicon {
    position: absolute;
    margin-left: calc(100% - 23px);
    margin-top: calc(1vh - 7px);
    color: #000000;
    transition: ease-out .3s;
  }

  &__title {
    position: relative;
    padding-top: 2%;
    margin: 5% 15% 3% 3%;
    font-size: 4vh;
    font-family: 'Trebuchet MS';
  }

  &__description {
    margin: 0% 0% 5% 3%;
    padding-bottom: 2%;
    font-size: 1.1em;
    font-family: 'Poppins';
    line-height: 1.6em;
  }

  &__reference {
    display: inline-block;
    border-bottom: 1px solid transparent;
    color: #0099ff;
    text-decoration: none;
    transition: ease-in .3s;

    &:hover {
      border-bottom-color: #0099ff;
    }
  }

  &:hover,
  &:focus {
    clip-path: circle(100%);
    border-radius: 20px;
    box-shadow: 0px 3px 9px rgba(0, 0, 0, 0.30),
      0px 3px 18px rgba(0, 0, 0, 0.08);
    background: #ffffff;
    outline: none;

    .info-card__infoicon {
      opacity: 0;
    }
  }

  &:focus {
    box-shadow: 0px 3px 9px rgba(0, 0, 0, 0.12),
      0px 3px 18px rgba(0, 0, 0, 0.08),
      0px 0px 0px 4px rgba(0, 0, 0, 0.2);
  }
}
</style>
