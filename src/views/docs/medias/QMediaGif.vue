<template>
    <docs-pages-template
    :theme="theme"
    :params="params"
    :methods="methods"
    :signals="signals"
    :widget_data="widget_data"
    :widget_type="'QMediaGif'"
    :exampleFile="'gif'"
    :isMedia="true"
    :step2File="'step2ForGif'"
    :step3File="'step3ForMedia'"
    
    ></docs-pages-template>
    
</template>


<script>
import DocsPagesTemplateVue from '../../DocsPagesTemplate.vue'
import axios from 'axios'
export default {
    name: 'QMediaGif',
    data(){
        return{
            params:[],
            methods:[],
            signals:[],
            widget_data:{}
        }
    },
    components: {
        'docs-pages-template': DocsPagesTemplateVue
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
        axios.get('../../jsons/QMedia.json')
        .then(response => {
            this.widget_data = response.data.medias[1]
            this.params = response.data.QMediaGif.params
            this.methods = response.data.QMediaGif.methods
            this.signals = response.data.QMediaGif.signals

        })
        .catch(error => {
            console.log(error)
        })
        
    }
}
</script>
