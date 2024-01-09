<template>
    <form v-on:submit="navigateToResults" id="search-bar">
        <input type="text" placeholder="search site" name="urlToAnalyse" id="urlToAnalyse"
            v-model="urlToAnalyse" />
        <button type="submit">
            <img class="flat-icon" src="/search.svg" alt="search button" />
        </button>
    </form>
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


<style lang="scss">
* {
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
}

:root {
    --searchBarColor: rgba(255, 255, 255, 0.767);
    --searchBarHoverColor: #ffffff;
    --placeholderColor: #000000;
    --inputColor: #000000;

    --transitionColor: 0.3s;
    --transitionScale: 0.1s;
}

#urlToAnalyse {
    background: none;
    border: none;
    outline: none;

}

#urlToAnalyse:-webkit-autofill,
#urlToAnalyse:-webkit-autofill:hover,
#urlToAnalyse:-webkit-autofill:focus,
#urlToAnalyse:-webkit-autofill:active {
    -webkit-box-shadow: 0 0 0 1000px transparent inset !important;
    -webkit-text-fill-color: inherit !important;
    transition: background-color 5000s ease-in-out 0s;
}



#search-bar {
    max-height: 35px;
    min-height: 35px;
    max-width: 400px;
    min-width: 400px;
    height: 35px;
    width: 400px;
    background: var(--searchBarColor);
    display: flex;
    align-items: center;
    border-radius: 20px;
    backdrop-filter: blur(1px) saturate(180%);
    transition: var(--transitionColor);

    &::placeholder {
        color: var(--placeholderColor);
    }

    input {
        flex: 1;
        margin-left: 20px;
        font-size: var(--fontSize);
        color: var(--inputColor);
        &:focus {
            box-shadow: none !important;
            outline-color: transparent;
            background-color: transparent !important;
        }
    }

    &:hover {
        background-color: var(--searchBarHoverColor);
    }

    button {
        height: 35px;
        width: 35px;
        background: transparent;
        box-shadow: none;
        border-radius: 50%;
        margin-left: auto;

        &:hover img{
            transform: scale(1.2);
            transition: var(--transitionScale);
        }
        
        img {
            height: 20px;
            filter: invert(30%);
        }

        &:active {
            img {
                filter: invert(1);
            }
        }
    }
}

</style>
