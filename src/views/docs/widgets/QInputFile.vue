<template>
    <docs-pages-template
    :theme="theme"
    :params="params"
    :methods="methods"
    :signals="signals"
    :widget_data="widget_data"
    :widget_type="'QInputFile'"
    :exampleFile="'file'"
    :isMedia="false"
    :step2File="'step2ForFile'"
    :step3File="'step3'"
    
    ></docs-pages-template>

</template>


<script>
import DocsPagesTemplateVue from '../../DocsPagesTemplate.vue'
import axios from 'axios'
export default {
    name: 'QInputFilePage',
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
        },
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
            this.widget_data = response.data.widgets[2]
            this.params = response.data.QInputFile.params
            this.methods = response.data.QInputFile.methods
            this.signals = response.data.QInputFile.signals

        })
        .catch(error => {
            console.log(error)
        })
        
    }
}
</script>
