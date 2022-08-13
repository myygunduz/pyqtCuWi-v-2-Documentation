<template>
    <docs-pages-template
    :theme="theme"
    :params="params"
    :methods="methods"
    :signals="signals"
    :widget_data="widget_data"
    :widget_type="'QMediaImage'"
    :exampleFile="'image'"
    :isMedia="true"
    :step2File="'step2ForImage'"
    :step3File="'step3ForMedia'"
    
    ></docs-pages-template>

</template>


<script>
import DocsPagesTemplateVue from '../../DocsPagesTemplate.vue'
import axios from 'axios'
export default {
    name: 'QMediaImage',
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
            this.widget_data = response.data.medias[0]
            this.params = response.data.QMediaImage.params
            this.methods = response.data.QMediaImage.methods
            this.signals = response.data.QMediaImage.signals

        })
        .catch(error => {
            console.log(error)
        })
        
    }
}
</script>
