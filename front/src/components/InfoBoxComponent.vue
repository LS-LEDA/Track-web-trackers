<template>
    <div id="ic" class="info-card" tabindex="0">
      <span class="info-card-wrap">
        <span class="info-card__infoicon">
          <img id="info-icon" src="https://img.icons8.com/ios-glyphs/512/information.png" style="width:20px">
        </span>
      </span>
        
        <h1 class="info-card__title"><p>Projecte Web Trackers</p></h1>
        <p class="info-card__description">This is the Web Tracker Project. Type any URL in the search bar to know if the site has any tracker.</p>
    </div>
</template>

<style lang="scss">

* {
  z-index: 2;
  box-sizing:border-box;
}

.info-card{
  z-index: 2;
  position: absolute;
  
  clip-path: circle(15px at 97% 17%);
  transition: all ease-in-out .3s;
  background-color:#ffffff;
  
  &__infoicon{
    position:absolute;
    margin-left: calc(100vw - 1251px);
    margin-top: 25px;
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
    box-shadow: 0px 3px 9px rgba(0,0,0,0.30),
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

</style>
