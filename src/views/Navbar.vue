<template>
    <div class="bar">
        <div>
            <router-link to="/" class="logo" >
                <img src="/assets/pyqtcuwi.png" alt="logo">
                <span class="bold">PyQtCuWi</span>
                <span>{{mode}}</span>
            </router-link>
        </div>
        <div class="nav">
            <router-link to="/" class="link">
                <span>Home</span>
            </router-link>
            <router-link to="/introduction#introduction" class="link">
                <span>Get Started</span>
            </router-link>
            <router-link to="/introduction#installation" class="link">
                <span>Installation</span>
            </router-link>
            <router-link to="/examples" class="link">
                <span>Examples</span>
                <ul>
                    <li style="--id:1">QInput</li>
                    <li style="--id:2">QMedia</li>
                </ul>
            </router-link>
        </div>
        <div class="nav nav-right">
            <div class="dol" @click="changeTheme" :class="{'dark':theme=='dark','light':theme=='light'}"> <!--dark or light-->
                <div class="toggle"></div>
                <i class="fa-solid fa-sun"></i>
                <i class="fa-solid fa-moon"></i>
            </div>
            <a href="https://github.com/myygunduz/pyqtCuWi-V2" target="_blank" class="link source">
                <i class="fa-brands fa-github"></i>
            </a>
        </div>
    </div>
</template>


<script>
export default {
    name: 'NavBar',
    props: {
        mode: {
            type: String,
            default: 'Documentation'
        },
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
.bar{
    width: 100%;
    height: 60px;
    border-bottom: 1px solid var(--nav-bg-color);
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    position: relative;
}
.bar .logo {
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-decoration: none;
    float:left;
    position: absolute;
    left: 10px;
    top: 50%;
    transform: translateY(-50%);
}
.bar .logo img{
    width: 50px;
}
.bar .logo span.bold{
    font-size: 1.5em;
    font-weight: bold;
    color: var(--nav-color);
    margin-left: 10px;
    padding-left: 0;
}
.bar .logo span{
    font-size: 1em;
    color: var(--nav-color);
    padding-left: 5px;
    transition: all 0.3s ease-in-out;
}
.bar .logo:hover span{
    color: var(--nav-h-color);
}


.bar .nav{
    display: flex;
    justify-content: flex-end;
    align-items: center;
}
.bar .nav-right{
    position: absolute;
    right: 10px;
    top: 0;
}
.bar .link{
    text-decoration: none;
    color: var(--nav-color);
    font-size: 1em;
    margin: 10px;
    padding:10px;
    transition: all 0.3s ease-in-out;

    position: relative;
}
.bar .link.source{
    font-size:1.5rem;
    margin:0;
}
.bar .link.source:hover{
    color: var(--nav-h-color);
}

.bar .link:hover span{
    color: var(--nav-h-color);
    transition: all 0.3s ease-in-out;
}
.bar .link ul{
    position: absolute;
    top: 117%;
    left: 0;
    list-style: none;
    padding-left: 5px;
    margin-left:5px;
    padding-top:5px;
    height:0;
    overflow: hidden;
    transition: all 0.3s ease-in-out;
    background-color: var(--nav-bg-color);
    opacity: 0;

    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
}
.bar .link:hover ul{
    opacity: 1;
    height: 100px;
}

.bar .link ul li{
    padding:10px;
}
.bar .link ul li:hover{
    color: var(--nav-h-color);
}

.bar .nav-right .dol{
    width:60px;
    height: 30px;
    background-color: var(--dol-bg-color);

    display: flex;
    justify-content: space-around;
    align-items: center;

    border-radius: 25px;

    position:relative;

    cursor: pointer;
}
.bar .nav-right .dol .toggle{
    width:23px;
    height:23px;
    background-color: var(--dol-toggle-bg-color);
    border-radius: 50%;
    position: absolute;
    top: 50%;
    left: 5px;
    transform: translateY(-50%);
    transition: all 0.3s ease-in-out;
}
.bar .nav-right .dol.light .toggle{
    left:32px;
}
.bar .nav-right .dol i{
    color:var(--dol-color);
}
</style>