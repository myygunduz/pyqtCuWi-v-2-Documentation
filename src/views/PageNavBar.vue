<template>
    <div class="nav">
        <p>On this page</p>
        <div class="links">
            <router-link 
                v-for="(data,index) in navData" :key="index"
                :to="data.url" 
                class="link"
                active-class="active">
                {{data.name}}
            </router-link>
        </div>
        <br><hr><br>
        <p>Having a problem?</p>
        <div class="links">
            <a href="https://github.com/myygunduz/pyqtCuWi-V2/issues" class="link">Please send an issue.</a>
        </div>
        <br><hr><br>
        <p>Social medias</p>
        <div class="socialMedias">
            <a v-for="(socialMedia, index) in socialMedias" 
            :key="index" 
            v-html="socialMedia['icon']" 
            :href="socialMedia['link']"
            :style="{'--color':socialMedia['color']}"
            target="_blank"></a>
        </div>
        <br><hr><br>
        <div class="license">
            <svg aria-hidden="true" viewBox="0 0 24 24" version="1.1" data-view-component="true" class="octicon octicon-law color-fg-default float-left mr-2">
                <path fill-rule="evenodd" d="M12.75 2.75a.75.75 0 00-1.5 0V4.5H9.276a1.75 1.75 0 00-.985.303L6.596 5.957A.25.25 0 016.455 6H2.353a.75.75 0 100 1.5H3.93L.563 15.18a.762.762 0 00.21.88c.08.064.161.125.309.221.186.121.452.278.792.433.68.311 1.662.62 2.876.62a6.919 6.919 0 002.876-.62c.34-.155.606-.312.792-.433.15-.097.23-.158.31-.223a.75.75 0 00.209-.878L5.569 7.5h.886c.351 0 .694-.106.984-.303l1.696-1.154A.25.25 0 019.275 6h1.975v14.5H6.763a.75.75 0 000 1.5h10.474a.75.75 0 000-1.5H12.75V6h1.974c.05 0 .1.015.14.043l1.697 1.154c.29.197.633.303.984.303h.886l-3.368 7.68a.75.75 0 00.23.896c.012.009 0 0 .002 0a3.154 3.154 0 00.31.206c.185.112.45.256.79.4a7.343 7.343 0 002.855.568 7.343 7.343 0 002.856-.569c.338-.143.604-.287.79-.399a3.5 3.5 0 00.31-.206.75.75 0 00.23-.896L20.07 7.5h1.578a.75.75 0 000-1.5h-4.102a.25.25 0 01-.14-.043l-1.697-1.154a1.75 1.75 0 00-.984-.303H12.75V2.75zM2.193 15.198a5.418 5.418 0 002.557.635 5.418 5.418 0 002.557-.635L4.75 9.368l-2.557 5.83zm14.51-.024c.082.04.174.083.275.126.53.223 1.305.45 2.272.45a5.846 5.846 0 002.547-.576L19.25 9.367l-2.547 5.807z"></path>
            </svg>
            <a href="https://github.com/myygunduz/pyqtCuWi-V2/blob/main/LICENSE" target="_blank">MIT License</a>
        </div>
    </div>
</template>


<script>
import axios from 'axios';
export default {
    name: 'PageNavBar',
    data(){
        return {
            navData: [],
            socialMedias: [],
        }
    },
    props: {
        page: {
            type: String
        }
    },
    created() {
        axios.get('/jsons/PageNavBar.json')
        .then(response => {
            if (this.$props.page=='introduction'){
                this.navData = response.data.introduction;
            }else if(this.$props.page=='QInput'){
                this.navData = response.data.QInput;
            }else if(this.$props.page=='QInputButton'){
                this.navData = response.data.QInputButton;
            }else if(this.$props.page=='QInputCheckbox'){
                this.navData = response.data.QInputCheckBox;
            }else if(this.$props.page=='QInputFile'){
                this.navData = response.data.QInputFile;
            }else if(this.$props.page=='QInputRadio'){
                this.navData = response.data.QInputRadio;
            }else if(this.$props.page=='QInputSlider'){
                this.navData = response.data.QInputSlider;
            }else if(this.$props.page=='QMedia'){
                this.navData = response.data.QMedia;
            }else if(this.$props.page=='QMediaImage'){
                this.navData = response.data.QMediaImage;
            }else if(this.$props.page=='QMediaGif'){
                this.navData = response.data.QMediaGif;
            }

        })
        .catch(error => {
            console.log(error);
        });
        axios.get('../../jsons/SocialMedias.json')
        .then(response => {
            this.socialMedias = response.data;
        }).catch(error => {
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
    border-left:1px solid var(--nav-bg-color);
    display:flex;
    flex-direction:column;
    justify-content:space-around;
    align-items:center;

    color:var(--nav-color);

    overflow-x:hidden;
    overflow-y:auto;
    
}
.nav hr{
    width: 80%;
    height: 2px;
    background: var(--doc-hr-color);
    border:0;
}
.nav p{
    font-size:20px;
    width: 80%;
    text-align:left;
}
.nav .links{
    position: relative;
    display:flex;
    flex-direction:column;
    width: 80%;
}
.nav .links::before{
    content:'';
    position:absolute;
    left:5px;
    top:0;
    width:50%;
    height: 100%;
    border-left:1px solid var(--nav-bg-color);
    border-bottom: 1px solid var(--nav-bg-color);
    border-bottom-left-radius: 5px;
}

.nav .link{
    cursor: pointer;
    color:var(--nav-color);
    margin-bottom:10px;
    position: relative;
    transition: all 0.3s;
    text-decoration: none;
    padding-left: 15px;
}
.nav .link:hover{
    color:var(--nav-h-color);
    text-decoration: underline;
}
.nav .link::before{
    content:'';
    position:absolute;
    left:5px;
    top:50%;
    transform:translateY(-50%);
    width:10px;
    height:1px;
    background-color:var(--nav-bg-color);
}

.socialMedias{
    width: 100%;
    margin-right:10px;
    transition:all 0.3s;
    display:grid;
    grid-template-columns:repeat(3,1fr);
    align-items:center;
    justify-items:center;

}
.socialMedias a{
    text-decoration: none;
    color:var(--nav-color);
    transition:all 0.3s;
    font-size:30px;
}
.socialMedias a:hover{
    color:var(--color);
    transform: scale(1.1);
}

.license{
    width:100%;
    display:flex;
    flex-direction:row;
    justify-content:center;
    align-items:center;

}
.license a{
    color:var(--nav-color);
    text-decoration: none;
    margin-left:10px;
    transition:all 0.3s;
}
.license .octicon{
    fill:var(--nav-color);
    width: 25px;
    height: 25px;
    transition:all 0.3s;
}
.license:hover a,
.license:hover .octicon{
    color:var(--nav-h-color);
    fill:var(--nav-h-color);
}

</style>