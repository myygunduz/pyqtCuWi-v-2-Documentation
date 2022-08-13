<template>
    <div class="page">
        <nav-bar
        :theme="theme"
        @changeTheme="changeTheme"></nav-bar>
        <div class="main">
            <div class="text">
                <h1>Custom Widget for <br>your Programs</h1>
                <p>PyQtCuWi is a custom widget library for PyQt6/PySide6.</p>
                <p>It is a Qt-based library that is designed to be used in your programs.</p>
                <div class="buttons">
                    <router-link to="/introduction">
                        <button>Get Started</button>
                    </router-link>
                    <router-link to="/introduction#installation">
                        <button>Installation</button>
                    </router-link>
                </div>
            </div>
            <div class="img">
                <img src="/assets/pyqtcuwi.png" alt="logo">
            </div>
        </div>
    </div>
</template>


<script>
import Navbar from './Navbar.vue'
export default {
    name: 'HomePage',
    components: {
        'nav-bar': Navbar,
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
}
</script>


<style scoped>
@import '../styles/theme.css';
.text{
    margin-right:20px;
}

.text h1{
    color:var(--color);
}
.text p{
    color:var(--color);
    font-size:18px;
}

.text button{
    background-color: transparent;
    border:2px solid var(--btn-border-color);
    color: var(--btn-color);
    border-radius: 5px;
    padding: 10px;
    font-size: 18px;
    cursor: pointer;
    margin-top:10px;
    margin-right: 10px;
    transition: all 0.3s ease-in-out;
}
.text button:hover{
    background-color: var(--btn-h-bg-color);
    color: var(--btn-h-color);
}

</style>