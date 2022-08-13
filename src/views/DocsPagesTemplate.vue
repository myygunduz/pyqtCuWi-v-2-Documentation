<template>
    <div class="page">
        <nav-bar 
        :theme="theme"
        @changeTheme="this.$emit('change-theme')"></nav-bar>
        <div class="main grid">
            <doc-nav-bar></doc-nav-bar>
            <div class="main-area" >
                <h1 :id="widget_type.toLowerCase()">{{widget_type}}</h1>
                <br><hr><br>
                
                <h2 id="usage">Usage</h2>
                <p>1- Import the PyQtCuWi2</p>
                <code-highlight :code="'step1'" :theme="theme"   :title="'step1'"></code-highlight>
                <p>2- Create a widget from PyQtCuWi2</p>
                <code-highlight :code="step2File" :theme="theme" :title="'step2'"></code-highlight>
                <p>3- Add the widget to your layout</p>
                <code-highlight :code="step3File" :theme="theme" :title="'step3'"></code-highlight>
                <br><hr><br>

                <h2 id="example">Example</h2>
                <code-highlight :code="exampleFile" :theme="theme" :title="widget_type"></code-highlight>
                <p>Output:</p>
                <br>
                <widget-preview 
                    :widget_data="widget_data"
                    :title="'output'"
                    :isMedia="isMedia"
                    ></widget-preview>
                <br><hr><br>

                <h2 id="params">Parameters</h2>
                <table-view :data="params"></table-view>
                <br><hr><br>

                <h2 id="methods">Methods</h2>
                <table-view :data="methods"></table-view>
                <br><hr><br>

                <h2 id="signals">Signals</h2>
                <table-view :data="signals"></table-view>
            </div>
            <page-nav-bar :page="widget_type"></page-nav-bar>
        </div>
    </div>
</template>


<script>
import Navbar        from './Navbar.vue'
import DocNavBar     from './DocNavBar.vue'
import PageNavBar    from './PageNavBar.vue'
import TableView     from './TableView.vue'
import CodeHighlight from './CodeHighlight.vue'
import WidgetPreview from './docs/WidgetPreview.vue'
export default {
    components: {
        'nav-bar': Navbar,
        'doc-nav-bar': DocNavBar,
        'page-nav-bar': PageNavBar,
        'table-view': TableView,
        'code-highlight': CodeHighlight,
        'widget-preview': WidgetPreview
    },
    props: {
        theme: {type: String,default: 'dark'},
        params:{type: Array,},
        methods:{type: Array,},
        signals:{type: Array,},
        widget_data:{type: Array,},
        widget_type:{type: String,},
        exampleFile:{type: String,},
        isMedia:{type: Boolean,default: false},
        step2File:{type: String,},
        step3File:{type: String,},
    }
}
</script>
