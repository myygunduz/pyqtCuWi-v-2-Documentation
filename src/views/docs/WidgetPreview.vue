<template>
    <div class="widget">
        <div class="widget-example" :id="widget_data.id" @drop.prevent="dropLink" @dragenter="checkDrop" @dragover="checkDrop">
            <template v-if="widget_data.id=='button'">
                Button
            </template>

            <template v-if="widget_data.id=='checkbox'">
                <div :id="widget_data.id" @click="click('checkbox1')">
                    <input type="checkbox" id="checkbox1" checked="checked">
                    <label for="checkbox1">Checkbox 1</label>
                    <div class="checkbox-box"></div>
                </div>
                <div :id="widget_data.id" @click="click('checkbox2')">
                    <input type="checkbox" id="checkbox2">
                    <label for="checkbox2">Checkbox 2</label>
                    <div class="checkbox-box"></div>
                </div>
            </template>

            <template v-if="widget_data.id=='file'">
                    <p>Drop File Here</p>
                    <div class="file-details" v-if="file_details">
                        <p>File Name:</p> <p>{{file_details.name}}</p>
                        <p>File Size:</p> <p>{{file_size}}</p>
                        <p>File Type:</p> <p>{{file_extension}}</p>
                        <p>File Path:</p> <p>Preview haven't permission see file path</p>
                        
                    </div>
            </template>

            <template v-if="widget_data.id=='radio'">
                <div :id="widget_data.id" @click="click('radiobutton1')">
                    <input type="radio" id="radiobutton1" name="radiobutton" checked="checked">
                    <label for="radiobutton1">RadioButton 1</label>
                    <div class="radio-box"></div>
                </div>
                <div :id="widget_data.id" @click="click('radiobutton2')">
                    <input type="radio" id="radiobutton2" name="radiobutton">
                    <label for="radiobutton2">RadioButton 2</label>
                    <div class="radio-box"></div>
                </div>
            </template>

            <template v-if="widget_data.id=='slider'">
                <div>
                    <input type="range" min="1" max="100" class="slider" id="myRange" v-model="sliderVal" :style="{'--value':sliderVal+'%'}">
                    <p>Value: <span id="demo">{{sliderVal}}</span></p>
                </div>
            </template>

            <template v-if="widget_data.id=='image'">
                <img :src="widget_data.src" :alt="widget_data.alt" :id="widget_data.id" height="150">
            </template>

            <template v-if="widget_data.id=='gif'">
                <img :src="widget_data.src" :alt="widget_data.alt" :id="widget_data.id" height="100">
            </template>

        </div>

        <router-link
            :to='"/widgets/qinput/"+widget_data.id'
            class="widget-title"
            v-if="!isMedia">
            {{title==''?widget_data.name:title}}
        </router-link>
        <router-link
            :to='"/medias/qmedia/"+widget_data.id'
            class="widget-title"
            v-else>
            {{title==''?widget_data.name:title}}
        </router-link>
    </div>
</template>


<script>

export default {
    name: 'WidgetPreview',
    data(){
        return{
            sliderVal:50,
            anchor: this.$route.hash,
            file_details: '',
            file_size: '',
            file_extension: '',
        }
    },
    props: {
        widget_data: {
            type: Object
        },
        title: {
            type: String,
            default: ''
        },
        isMedia:{
            type: Boolean,
            default: false
        }
    },
    methods: {
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
        checkDrop(e){
            e.preventDefault();
            e.stopPropagation();
        },
        dropLink(e){
            e.preventDefault();
            e.stopPropagation();
            //get file details as image
            this.file_details = e.dataTransfer.files[0];
            console.log(this.file_details.size);
            var size = this.file_details.size;
            this.file_size = this.formatBytes(size);
            this.file_extension = this.file_details.name.split('.').pop();
        },
        formatBytes(bytes, decimals = 2) {
            if (bytes === 0) return '0 Bytes';

            const k = 1024;
            const dm = decimals < 0 ? 0 : decimals;
            const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];

            const i = Math.floor(Math.log(bytes) / Math.log(k));

            return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
        }

    }
}
</script>


<style>


.widget{
    width: 100%;
    height: 100%;
    min-height:150px;
    display: grid;
    grid-template-columns: 1fr;
    align-items: center;
    justify-items: center;
    grid-template-rows: 80% 20%;
    background-color:var(--code-bg-color);
    padding-top:10px;
    border-radius:12px;
    transition: all 0.3s ease-in-out;
}

.widget-title{
    width:100%;
    height:100%;
    font-size:20px;
    color: var(--doc-color);
    background: var(--code-bg-color);
    border-bottom-left-radius: 12px;
    border-bottom-right-radius: 12px;
    transition: all 0.3s ease-in-out;
    text-decoration: none;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.widget-title:hover{
    color: var(--doc-hr-color);
}


#button{
    background-color:#fff;
    color:#161616;
    text-align: center;
    line-height: 32px;
    width:100px;
    height:32px;
    cursor: context-menu;
    user-select:none;
    margin-bottom:10px
}
#button:hover{
    background-color:#dcdcdc;
    color:#141414;
}

#checkbox,
#radio{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: context-menu;

    position: relative;
}

#checkbox input,
#radio input{
    width:0;
    height:0;
    opacity:0;
}
#checkbox label,
#radio label{
    display:inline-block;
    width:100%;
    height:100%;
    user-select:none;
    font-size:20px;
    color:var(--code-color);
    transition: all 0.3s ease-in-out;
}
#checkbox label:hover,
#radio label:hover{
    color:var(--code-h-color);
}

#checkbox .checkbox-box,
#radio .radio-box{
    width:20px;
    height:20px;
    background-color:var(--code-color);
    transition: all 0.3s ease-in-out;

    position: absolute;
    top:50%;
    right:110%;
    transform:translateY(-50%);
}
#radio .radio-box{
    border-radius:50%;
}

#checkbox input:hover ~ .checkbox-box,
#radio input:hover ~ .radio-box{
    background-color: var(--code-h-color);
}
#checkbox input:checked ~ .checkbox-box,
#radio input:checked ~ .radio-box{
    background-color: #2196F3;
}
#checkbox input:checked:hover ~ .checkbox-box,
#radio input:checked:hover ~ .radio-box{
    background-color: #2196F380;
}

#checkbox input:checked ~ .checkbox-box::after,
#radio input:checked ~ .radio-box::after{
    content:'';
    width:10px;
    height:10px;
    position: absolute;
}
#checkbox input:checked ~ .checkbox-box::after{
    top:0;
    left:0;
    width:5px;
    border: 1px solid #fff;
    border-width: 0 3px 3px 0;
    transform: rotate(40deg) translate(6px, -2px);
}

#radio input:checked ~ .radio-box::after{
    background-color: #fff;
    border-radius: 50%;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%);
}

#file{
    min-width: 80%;
    min-height: 80%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding:10px;
    background-color: var(--code-bg-color);
    overflow: hidden;

    border-radius:20px;
    border: 3px dashed var(--code-color);
}

.file-details{
    display: grid;
    grid-template-columns: 1fr 1fr;
    font-size: 12px;
    text-align: left;
}


.slider {
  -webkit-appearance: none;
  width: 100%;
  height: 15px;
  border-radius: 5px;  
  background: linear-gradient(to right, #f7422b 0%, #f7422b var(--value), #161616 var(--value), #161616 100%);
  outline: none;
  opacity: 0.7;
  -webkit-transition: .2s;
  transition: opacity .2s;
  
}

.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 25px;
  height: 25px;
  border-radius: 50%; 
  background: #fff;
}

.slider::-moz-range-thumb {
  width: 25px;
  height: 25px;
  border-radius: 50%;
  background: #fff;
}
</style>
