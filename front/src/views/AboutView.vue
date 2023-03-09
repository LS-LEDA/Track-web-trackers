<template>
    <HeaderComponent id="header" showSearch="false" />
    <div class="background">
        <div class="container">
            <h1 class="header-title heading-1"> About </h1>
            <br>
            <p>The project is an user rights of control initiative to expose web trackers and raise awareness regarding
                automatic data collection.</p>

            <p>This is an open source project developed in La Salle URL - Human-Environment Research group, Technology
                Enhanced Learning research line leadered by Daniel Amo Filva. </p>

            <h2 class="heading2" id="team">Team</h2>
            <p>The project leader for this project is Daniel Amo-Filva, who oversees the development of the project and
                manages contributions from other developers.</p>
            <ul>
                <li>Dr. Daniel Amo Filvà: <a class="link-about"
                        href="mailto:daniel.amo@salle.url.edu">daniel.amo@salle.url.edu</a> - <a class="link-about"
                        href="https://github.com/danielamof/">Github</a></li>
                <li>Pau Passolas Nadal: <a class="link-about"
                        href="mailto:pau.passolas@students.salle.url.edu">pau.passolas@students.salle.url.edu</a> - <a
                        class="link-about" href="https://github.com/ppassolas/">Github</a></li>
                <li>Dídac Ibars Teixidó: <a class="link-about"
                        href="mailto:didac.ibars@students.salle.url.edu">didac.ibars@students.salle.url.edu</a> - <a
                        class="link-about" href="https://github.com/TheDidi">Github</a></li>
            </ul>

            <h2 class="heading2">Cookie Policy</h2>

            <p>Track Web Trackers does not use cookies on its website.</p>

            <h2 class="heading2">Legal Advertisement</h2>

            <p>This website is provided as is, without warranty of any kind, express or implied, including but not limited
                to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event
                shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an
                action of contract, tort or otherwise, arising from, out of or in connection with the website or the use or
                other dealings in the website.</p>

            <h2 class="heading2">Privacy Policy</h2>

            <p>Track Web Trackers does not collect or store any personal information about its users.
                <br>For any questions or concerns about Track Web Trackers, please contact us at
            </p>

            <p>Thank you for using Track Web Trackers!</p>
            <a class="link-about" href="https://github.com/LS-LEDA/Track-web-trackers">Github</a>
        </div>
    </div>
</template>
  
<script>
import HeaderComponent from "../components/HeaderComponent.vue";

export default {
    name: "AboutView",
    components: { HeaderComponent },

    data() {
        return {

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
    font-family: 'Trebuchet MS', sans-serif;
}

.heading1 {
    color: white;
    font-size: 72px !important;
    font-weight: bold;
    letter-spacing: -1px;
    line-height: 1;
    text-align: center;
}



.heading2 {
    color: white;
    font-size: 36px !important;
    font-weight: 300 !important;
    line-height: 28px !important;
    margin: 25px !important;
}

.link-about {
    color: white;
}

.background {
    width: 100%;
    position: fixed;
    z-index: -1;
    min-height: 100vh;
    background: conic-gradient(at right center, rgb(107, 122, 146), rgb(16, 27, 53), rgb(0, 0, 0));
    background-position: center;
    background-size: cover;
    scroll-behavior: smooth;
}

.container {
    z-index: 1;
    color: white;
    font-family: 'Trebuchet MS';
    margin: auto;
    width: 70%;
    padding: 10px;
}


.header-title {
    color: rgb(255, 255, 255);
    transition: 0.3s;
    font-family: 'Trebuchet MS';
    font-weight: bold;
    text-shadow: 10px;
}
</style>
  