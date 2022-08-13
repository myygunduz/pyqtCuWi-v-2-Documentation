<template>
    <div class="nav">
        <div v-for="(data,index) in navData" :key="index" class="nav-part">
            <p class="part_head">{{data.part_title}}</p>
            <div 
                v-for="(data_item,index) in data.links" 
                :key="index"
                class="part_body"
                :class="{'withSubList':data_item.subList}">

                <router-link 
                    :to="data_item.url" 
                    class="data_name"
                    active-class="active">

                    {{data_item.name}}
                </router-link>

                <router-link  
                    v-for="(data_item,index) in data_item.subList" 
                    :key="index" 
                    :to="data_item.url"
                    class="subItem"
                    active-class="active">

                    {{data_item.name}}

                </router-link>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios';
export default {
    name: 'DocNavBar',
    data(){
        return {
            navData: [],
        }
    },
    created() {
        axios.get('/jsons/DocNavBar.json')
        .then(response => {
            this.navData = response.data;
        })
        .catch(error => {
            console.log(error);
        });
    },
}
</script>

<style scoped>
@import '../styles/theme.css';
.nav{
    width: 100%;
    height: 100%;
    border-right:1px solid var(--nav-bg-color);
    display:flex;
    flex-direction:column;
    justify-content:flex-start;
    align-items:flex-start;

    padding:20px;
    overflow-y: scroll;
    overflow-x: hidden;
}
.nav-part{
    margin-bottom:20px;
    width:100%;
    position: relative;
}

.part_head{
    font-size:20px;
}
.part_body{
    position:relative;
    display:flex;
    flex-direction:column;
    justify-content:flex-start;
    align-items:flex-start;
}
.data_name{
    font-size:16px;
    text-decoration: none;
    padding-left: 15px;
}
.subItem{
    font-size:14px;
    text-decoration: none;
    padding-left: 30px;
}

.part_head,
.data_name,
.subItem{
    cursor: pointer;
    color:var(--nav-color);
    margin-bottom:10px;
    position: relative;
    transition: all 0.3s;
}
.data_name::before,
.subItem::before{
    content:'';
    position:absolute;
    left:5px;
    top:50%;
    transform:translateY(-50%);
    width:10px;
    height:1px;
    background-color:var(--nav-bg-color);
}
.subItem::before{
    left:20px;
}
.data_name:hover,
.subItem:hover,
.active{
    color:var(--nav-h-color);
    text-decoration: underline;
}

.nav-part::before,
.part_body.withSubList::before{
    content:'';
    position:absolute;
    left:5px;
    top:30px;
    width:50%;
    height: calc(100% - (35px));
    border-left:1px solid var(--nav-bg-color);
    border-bottom: 1px solid var(--nav-bg-color);
    border-bottom-left-radius: 5px;
}
.part_body.withSubList::before{
    left:20px;
}


</style>