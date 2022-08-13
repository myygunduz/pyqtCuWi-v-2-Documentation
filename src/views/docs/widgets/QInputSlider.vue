<template>
    <docs-pages-template
    :theme="theme"
    :params="params"
    :methods="methods"
    :signals="signals"
    :widget_data="widget_data"
    :widget_type="'QInputSlider'"
    :exampleFile="'slider'"
    :isMedia="false"
    :step2File="'step2ForSlider'"
    :step3File="'step3'"
    
    ></docs-pages-template>
</template>


<script>
import DocsPagesTemplateVue from '../../DocsPagesTemplate.vue'
import axios from 'axios'
export default {
    name: 'QInputSliderPage',
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
            this.widget_data = response.data.widgets[4]
            this.params = response.data.QInputSlider.params
            this.methods = response.data.QInputSlider.methods
            this.signals = response.data.QInputSlider.signals

        })
        .catch(error => {
            console.log(error)
        })
        
    }
}
</script>
