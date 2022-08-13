<template>
    <docs-pages-template
    :theme="theme"
    :params="params"
    :methods="methods"
    :signals="signals"
    :widget_data="widget_data"
    :widget_type="'QInputButton'"
    :exampleFile="'introduction'"
    :isMedia="false"
    :step2File="'step2ForButton'"
    :step3File="'step3'"
    
    ></docs-pages-template>
    
</template>


<script>
import DocsPagesTemplateVue from '../../DocsPagesTemplate.vue'
import axios from 'axios'
export default {
    name: 'QInputButtonPage',
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
            default: 'light'
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
        axios.get('../../jsons/QInput.json')
        .then(response => {
            this.widget_data = response.data.widgets[0]
            this.params = response.data.QInputButton.params
            this.methods = response.data.QInputButton.methods
            this.signals = response.data.QInputButton.signals

        })
        .catch(error => {
            console.log(error)
        })
        
    }
}
</script>
