<template>
    <div id="header-logo-container">
        <button id="header-logo-btn">
            <a style="display: flex;" href="http://localhost:5173/" data-replace="hello">
                <img id="header-logo-img" src="/main-logo.svg"/>
                <p id="hover-text">Download JSON</p>
            </a>
        </button>
    </div>
</template>

<script>
export default {
    name: "HeaderLogo"
}
</script>

<style lang="scss">

#header-logo-btn {
    background: none;
    box-shadow: none;
}

#header-logo-img {
    width: 65px;
    transition: transform 0.2s;
}

#hover-text {
    visibility: hidden;
    opacity: 0;
}

#header-logo-container {
    position: relative;
    display: inline-block;
    width: 65px;
    overflow: hidden;
    transition: 0.3s;

    &:hover {
            width: 75px;
    }

    &:hover #header-logo-img {
        transform: scale(1.2);
    }

    &:hover #header-text {
        //margin-left: 23px;
        visibility: visible;
        opacity: 1;
        transition: 0.1s;
        transition-delay: 0.2s;
    }
    
}


</style>
