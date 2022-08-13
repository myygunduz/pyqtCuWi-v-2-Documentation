<template>
    <div class="page">
        <nav-bar 
        :theme="theme"
        @changeTheme="changeTheme"></nav-bar>
        <div class="main grid">
            <doc-nav-bar></doc-nav-bar>
            <div class="main-area" >
                <h1 id="introduction">Introduction</h1>
                <br><hr><br>
                <h2 id="what-is-pyqtcuwi" class="anchor">What is PyQtCuWi?</h2>
                <p>PyQtCuWi is a custom widget library for PyQt6/PySide6. It is a Qt-based library that is designed to be used in your programs</p>
                <br>
                <p>Here is a minimal example:</p>
                <code-highlight :code="'introduction'" :theme="theme"></code-highlight>
                <p>Output:</p>
                <br>
                <div class="box">
                    <div id="example">Button</div>
                </div>

                <br><hr><br>
                <h2 id="installation" class="anchor">Installation</h2>
                <p>Use PIP To Download</p>
                <br>
                <div class="box">
                    <p>pip install PyQtCuWi2</p>
                </div>
                <br>
                <p>or</p>
                <br>
                <div class="box">
                    <p>python3 -m pip install PyQtCuWi2</p>
                </div>

                <br><hr><br>
                <h2 id="usage" class="anchor">Usage</h2>
                <p>1- Import the PyQtCuWi2</p>
                <code-highlight :code="'step1'" :theme="theme"></code-highlight>
                <p>2- Create a widget from PyQtCuWi2</p>
                <code-highlight :code="'step2ForButton'" :theme="theme" :title="'step2'"></code-highlight>
                <p>3- Add the widget to your layout</p>
                <code-highlight :code="'step3'" :theme="theme"></code-highlight>
                <br><hr><br>
                <h2 id="license" class="anchor">License</h2>
                <code-highlight :code="'licence'" :theme="theme"></code-highlight>

            </div>
            <page-nav-bar :page="'introduction'"></page-nav-bar>
        </div>
    </div>
</template>


<script>
import Navbar from '../Navbar.vue'
import DocNavBar from '../DocNavBar.vue'
import PageNavBar from '../PageNavBar.vue'
import CodeHighlight from '../CodeHighlight.vue'
export default {
    name: 'IntroductionPage',
    components: {
        'nav-bar': Navbar,
        'doc-nav-bar': DocNavBar,
        'page-nav-bar': PageNavBar,
        'code-highlight': CodeHighlight
    },
    props: {
        theme: {
            type: String,
            default: 'dark'
        }
    },
    methods: {
        changeTheme() {
            this.$emit('change-theme')
        }
    },
    updated() {
        this.$nextTick(() => {
            if(this.$route.hash) {
                const el = document.querySelector(this.$route.hash);
                el && el.scrollIntoView();
            }
        })
    },
    created() {
        this.$nextTick(() => {
            if(this.$route.hash) {
                const el = document.querySelector(this.$route.hash);
                el && el.scrollIntoView();
            }
        })
        
    }
}
</script>


<style scoped>


.box{
    width: 100%;
    height: 100%;
    background-color:var(--code-bg-color);
    padding:10px;
    border-radius: 5px;
}
.box #example{
    background-color:#fff;
    color:#161616;
    text-align: center;
    line-height: 32px;
    width:100px;
    height:32px;
    cursor: context-menu;
    user-select:none;
}
.box #example:hover{
    background-color:#dcdcdc;
    color:#141414;
}

</style>
