<template>
    <div class="toggle">
            <button id="btn-light" class="btn-light" v-on:click="setLight">
                <div class="emoji">🔆</div>
            </button>
            <button id="btn-dark" class="btn-dark" v-on:click="setDark">
                <div class="emoji">🌙</div>
            </button>
    </div>
</template>

<style>

.toggle {
    margin-right: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

button {
    display: block;
    box-shadow: inset 0px 5px 15px rgba(0, 0, 0, 0.4), inset 0px -5px 15px rgba(255, 255, 255, 0.4);
    cursor: pointer;
}

.btn-dark {
    position: relative;
    text-align: center;
    font-size: 13px;
    display: inline-block;
    width: 30px;
    height: 30px;
    border-radius: 20px;
    background: transparent;
    color: white;
}

.btn-light {
    position: relative;
    text-align: center;
    font-size: 13px;
    width: 30px;
    height: 30px;
    border-radius: 20px;
    background: transparent;   
}

.btn-light:hover, .btn-dark:hover {
    background-color: aliceblue;
    height: 40px;
    color: black;
    transition: 0.3s ease-in-out;
}

.emoji {
    filter: invert(100%), brightness(200%);
    color: white;
}


</style>

<script>
import TrackerComponent from './TrackerComponent.vue';

export default {
    name: "ThemeToggleComponent",
    methods: {
        setDark(){
            document.body.style.background = 'rgb(38, 38, 38)';
            document.body.style.transition = '0.15s';
            //document.getElementById("tf").style.color = 'white';
            const pgText = document.getElementsByTagName("p");
            for (let i=0;i<pgText.length; i++) {
                pgText[i].style.color = 'white';
            }
            //document.getElementById("nt").style.color = 'white';
            const cards = document.getElementsByClassName("card");
            for (let i=0; i<cards.length; i++) {
                cards[i].style.background = 'rgb(38, 38, 38)';
                cards[i].style.color = 'white';
            }
            document.getElementById("ic").style.background = 'rgb(38, 38, 38)';
            document.getElementById("ic").style.transition = '0.15s';
            document.getElementById("info-icon").style.filter = "invert(100%)";
            document.getElementById("img-download").style.filter = "invert(100%)";
            console.log("Botó apretat");
        },
        setLight() {
            document.body.style.background = 'white';
            document.getElementById("tf").style.color= 'black';
            const cards = document.getElementsByClassName("card");
            for (let i=0; i<cards.length; i++) {
                cards[i].style.background = 'white';
                cards[i].style.color = 'black';
                cards[i].style.transition = '0.15s';
            }
            const pgText = document.getElementsByTagName("p");
            for (let i=0;i<pgText.length; i++) {
                pgText[i].style.color = 'black';
            }
            document.getElementById("ic").style.background = 'white';
            document.getElementById("ic").style.transition = '0.15s';
            document.getElementById("info-icon").style.filter = "invert(0%)";
            document.getElementById("img-download").style.filter = "invert(0%)";
            document.getElementById("nt").style.color= 'black';

        }
    }
}
</script>