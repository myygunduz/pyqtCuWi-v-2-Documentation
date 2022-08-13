<template>
    <div class="page">
        <nav-bar 
        :theme="theme"
        @changeTheme="changeTheme"></nav-bar>
        <div class="main grid">
            <doc-nav-bar></doc-nav-bar>
            <div class="main-area" >
                
                <h1 id="qinput">QInput</h1>
                <p>QInput is a custom widget for all input widgets.</p>
                <br><hr><br>
                
                <h2 id="params">Parameters</h2>
                <table-view :data="params"></table-view>
                <br><hr><br>
                
                <h2 id="widgets">Widgets</h2>
                <div class="widgets">
                        
                    <widget-preview 
                    v-for="(widget_data,index) in widgets"
                    :key="index"
                    :widget_data="widget_data"
                    ></widget-preview>
                        
                </div>
                <br><hr><br>
                
                <h2 id="methods">Methods</h2>
                <table-view :data="methods"></table-view>
                <br><hr><br>

                <h2 id="signals">Signals</h2>
                <table-view :data="signals"></table-view>
                
            </div>
            <page-nav-bar :page="'QInput'"></page-nav-bar>
        </div>
    </div>
</template>


<script>
import Navbar from '../../Navbar.vue'
import DocNavBar from '../../DocNavBar.vue'
import PageNavBar from '../../PageNavBar.vue'
import TableView from '../../TableView.vue'
import WidgetPreview from '../WidgetPreview.vue'
import axios from 'axios'
    
export default {
    name: 'QInputPage',
    data(){
        return{
            widgets:[],
            params:[],
            methods:[],
            signals:[],
            sliderVal:50,
            anchor: this.$route.hash
        }
    },
    components: {
        'nav-bar': Navbar,
        'doc-nav-bar': DocNavBar,
        'page-nav-bar': PageNavBar,
        'table-view': TableView,
        'widget-preview': WidgetPreview
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
        },
        click(id){
            //check if checkbox is checked
            if(document.getElementById(id).checked ){
                //uncheck checkbox
                if (id=='checkbox1' || id=='checkbox2') {
                    document.getElementById(id).checked = false;
                }
            }else{
                //check checkbox
                document.getElementById(id).checked = true;
            }

        }
    },
    updated() {
        if(this.$route.hash != this.anchor){
            console.log(this.$route.hash == this.anchor)
            this.$nextTick(() => {
                if(this.$route.hash) {
                    const el = document.querySelector(this.$route.hash);
                    el && el.scrollIntoView();
                }
                this.anchor = this.$route.hash;
            })
        }
    },
    created() {
        this.$nextTick(() => {
            if(this.$route.hash) {
                const el = document.querySelector(this.$route.hash);
                el && el.scrollIntoView();
            }
        })
        axios.get('../../jsons/QInput.json')
        .then(response => {
            this.widgets = response.data.widgets
            this.params = response.data.params
            this.methods = response.data.methods
            this.signals = response.data.signals
        })
        .catch(error => {
            console.log(error)
        })
    }
}
</script>


<style>


.widgets{
    display: grid;
    grid-template-columns: 1fr 1fr;
    align-items: center;
    justify-items: center;
    grid-gap: 20px;
    margin-top: 20px;
}

</style>
