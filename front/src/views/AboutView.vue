<template>
    <HeaderComponent id="header" showSearch="false" />
    <div class="background">
        <div class="container">
            <h1 class="header-title-2 heading-1"> About </h1>
            <br>
            <p>The project is an user rights of control initiative as part of the Erasmus+ project Security and Privacy in
                Academic Data management at Schools (SPADATAS). Website <a href="spadatas.eu"
                    target="_blank">spadatas.eu</a>. Grant ref.
                2022-1-ES01-KA220-SCH-000086363

                The main objective of the Track-web-trackers project is to expose web trackers and raise awareness regarding
                automatic data collection.

                The Internet has become, against the user community's desire, a capitalist surveillance digital space with
                no privacy and merci. Websites use cookies, third-party APIs, and other techy mechanisms to collect
                different kinds of data from Internet users for economic purposes. These data collectors transform data into
                users' behaviors and habits, which are fully observed and aggregated through code snippets hidden among
                websites' code. These third-party actors are considered 'trackers' and allow user profiling to display
                targeted advertising and sell behavioral profiles to multiple companies for purposes that violate community
                rights. Transparency is required regarding the use of trackers so that users gain awareness about who is
                taking data from them on a website and thus make better-informed decisions to avoid surveillance mechanisms.
                Hence, Internet users need tools to protect themselves from trackers. The project aims to help build a more
                transparent Internet by exposing web trackers behind websites in conjunction with the participation of the
                community.</p>

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

            <h2 class="heading2">SPADATAS</h2>
            <p>
                The SPADATAS project (Ref.: 2022-1-ES01-KA220-SCH-000086363) is co-financed by the Erasmus+ program of the
                European Union. The content of this publicacion is the sole responsibility of the consortium and neither the
                European Commission, nor the Spanish Service for the Internationalization of Education (SEPIE) are
                responsible for the use that may be made of the information disclosed here.
            </p>
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
    position: absolute;
    z-index: -1;
    min-height: 100vh;
    background: conic-gradient(at right center, rgb(107, 122, 146), rgb(16, 27, 53), rgb(0, 0, 0));
    background-position: center;
    background-size: cover;
    scroll-behavior: smooth;
    padding-bottom: 50px;
}

.header-title-2 {
    color: rgb(255, 255, 255);
    transition: 0.3s;
    font-family: 'Trebuchet MS';
    font-weight: bold;
    text-shadow: 10px;
    font-size: max(6vw, 3em, 3rem);
}

.container {
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
    color: white;
    line-height: 2;
}

h1 {
    font-size: 32px;
    font-weight: bold;
    margin-bottom: 20px;
}

h2 {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 15px;
}

h3 {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
}

p {
    font-size: 16px;
    margin-bottom: 15px;
}

ul {
    list-style: disc;
    padding-left: 20px;
    margin-bottom: 15px;
}

li {
    font-size: 16px;
    line-height: 1.5;
    margin-bottom: 5px;
}

a {
    color: #6fa1ff;
    text-decoration: underline;
}

a:hover {
    color: #fff;
    background-color: #6fa1ff;
}
</style>
