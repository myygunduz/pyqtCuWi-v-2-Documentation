<template>
    <docs-pages-template
    :theme="theme"
    :params="params"
    :methods="methods"
    :signals="signals"
    :widget_data="widget_data"
    :widget_type="'QInputRadio'"
    :exampleFile="'radio'"
    :isMedia="false"
    :step2File="'step2ForRadio'"
    :step3File="'step3'"
    
    ></docs-pages-template>
    
</template>


<script>
import DocsPagesTemplateVue from '../../DocsPagesTemplate.vue'
import axios from 'axios'
export default {
    name: 'QInputRadioPage',
    data(){
        return{
            params:[],
            methods:[],
            signals:[],
            widget_data:{},
            anchor: this.$route.hash
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
            this.widget_data = response.data.widgets[3]
            this.params = response.data.QInputRadio.params
            this.methods = response.data.QInputRadio.methods
            this.signals = response.data.QInputRadio.signals

        })
        .catch(error => {
            console.log(error)
        })
        
    }
}
</script>
