<template>
    <div class="page">
        <nav-bar 
        :theme="theme"
        @changeTheme="this.$emit('change-theme')"></nav-bar>
        <div class="main grid">
            <doc-nav-bar></doc-nav-bar>
            <div class="main-area" >
                <h1 id="stylestring">If You Use String</h1>
                <br><hr><br>

            </div>
            <page-nav-bar :page="'stylestring'"></page-nav-bar>
        </div>
    </div>
</template>


<script>
import Navbar        from '../../Navbar.vue'
import DocNavBar     from '../../DocNavBar.vue'
import PageNavBar    from '../../PageNavBar.vue'
// import TableView     from '../../TableView.vue'
// import CodeHighlight from '../../CodeHighlight.vue'
// import WidgetPreview from '../../docs/WidgetPreview.vue'
export default {
    name: 'StylesDict',
    components: {
        'nav-bar': Navbar,
        'doc-nav-bar': DocNavBar,
        'page-nav-bar': PageNavBar,
        // 'table-view': TableView,
        // 'code-highlight': CodeHighlight,
        // 'widget-preview': WidgetPreview
    },
    props: {
        theme: {type: String,default: 'dark'}
    }
}
</script>
