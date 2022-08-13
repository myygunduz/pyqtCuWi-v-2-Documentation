<template>
    <div class="code">
        <div class="code-head">
            <p v-if="code!='licence'"><i class="fa-brands fa-python"></i> {{title==''?(code + '.py') : title + '.py'}}</p>
            <p v-else><i class="fa-solid fa-certificate"></i> LICENCE</p>
            <div class="copy-btn" @click="copyCode()"><i class="fa-regular fa-clipboard"></i></div>
        </div>
        <div class="code-body">
            <pre><code class="language-python" v-html="codePy" style="font-family: 'Source Code Pro', monospace;"></code></pre>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
export default{
    name: 'CodeHighlight',
    props: {
        code: {
            type: String
        },
        theme: {
            type: String,
        },
        title: {
            type: String,
            default: ''
        }
    },
    data(){
        return {
            keywords:{
                "keywords" : [
                    "and","as","assert","break",
                    "class","continue","def","del",
                    "elif","else","except","False",
                    "finally","for","from","global",
                    "if","import","in","is","lambda",
                    "None","nonlocal","not","or","pass",
                    "raise","return","True","try",
                    "while","with","yield"
                ],
                "operators":[
                    '(',')','[',']','{','}',' = ','.',','
                ],
                'methods':[
                    "addWidget","setLayout","QType","QInputType","show","exec"
                ],
                'QTypes':[
                    'BUTTON','RADIO','CHECKBOX','FILE','SLIDER','SWITCH','NUMBER','PASSWORD','TEXTAREA','TEXT'
                ],
                'class':[
                    'CuWi','QtWidgets','QtWidgets','QWidget','QHBoxLayout'
                ]
            },
            codePy : '',
            copyCodePy: '',
            dark:{
                'keywords':'#d72b36',
                'operator':'#176cd3',
                'method':'#FFC23C',
                'QType':'#D61C4E',
                'string':'#C84B31',
                'comment':'#6C6C6C'
            },
            light:{
                'keywords':'#DA0037',
                'operator':'#176cd3',
                'method':'#1C6DD0',
                'QType':'#DA0037',
                'string':'#C84B31',
                'comment':'#2D4263'
            }
        }
    },
    methods:{
        getStyle() {
        if(this.$props.code=='licence'){
            axios.get('/LICENCE').then(res => {
                this.copyCodePy = res.data;
                this.codePy = res.data;
        })}
        else{
        axios.get(`/py/${this.$props.code}.py`).then(res => {
            var colors = this.$props.theme == 'dark' ? this.dark : this.light;
            this.copyCodePy = res.data;
            this.codePy = res.data;
            this.codePy = this.codePy.replaceAll('\n','/012 ')
            this.codePy = this.codePy.replaceAll('"','/013')
            this.codePy = this.codePy.replaceAll('#','/014#')
            var words = this.codePy.split(' ');
            for (let j = 0; j < words.length; j++) {
                for (let i = 0; i < this.keywords.keywords.length; i++) {
                    var keyword=this.keywords.keywords[i];
                    if(words[j] == keyword){
                        words[j] = '<span style="color:'+colors.keywords+';">'+words[j]+'</span>';
                    }
                }   
            }
            let j = 0;
            
            this.codePy = words.join(' ')
            for (j = 0; j < this.keywords.operators.length; j++) {
                var operator=this.keywords.operators[j];
                this.codePy = this.codePy.replaceAll(operator, '<span style="color:'+colors.operator+';">'+operator+'</span>');
            }
            for (j = 0; j < this.keywords.methods.length; j++) {
                var method=this.keywords.methods[j];
                this.codePy = this.codePy.replaceAll(method, '<span style="color:'+colors.method+';">'+method+'</span>');
            }

            words = this.codePy.split('/014');
            for (let j = 0; j < words.length; j++) {
                if(words[j].startsWith('#')){
                    this.codePy = this.codePy.replaceAll(words[j].split('/012')[0], '<span style="color:'+colors.comment+';font-style: italic;;">'+words[j].split('/012')[0]+'</span>');
                }
            }

            for (j = 0; j < this.keywords.QTypes.length; j++) {
                var QType=this.keywords.QTypes[j];
                this.codePy = this.codePy.replaceAll(QType, '<span style="color:'+colors.QType+';">'+QType+'</span>');
            }

            //change style between two nails
            words = this.codePy.split('/013');
            for (let j = 0; j < words.length; j++) {
                // <span> in words[j]
                
                if(words[j].includes('span')==false){
                    this.codePy = this.codePy.replaceAll(words[j], '<span style="color:'+colors.string+';">'+words[j]+'</span>');
                }
            }
            this.codePy = this.codePy.replaceAll('/012 ', '')
            this.codePy = this.codePy.replaceAll('/013', '<span style="color:'+colors.string+';">"</span>');
            this.codePy = this.codePy.replaceAll('/014', '');
            
        })}},
        copyCode(){
            //copy code to clipboard
            const el = document.createElement('textarea');  
            el.value = this.copyCodePy;                                 
            el.setAttribute('readonly', '');                
            el.style.position = 'absolute';                     
            el.style.left = '-9999px';                      
            document.body.appendChild(el);                  
            const selected =  document.getSelection().rangeCount > 0  ? document.getSelection().getRangeAt(0) : false;                                    
            el.select();                                    
            document.execCommand('copy');                   
            document.body.removeChild(el);                  
            if (selected) {                                 
                document.getSelection().removeAllRanges();    
                document.getSelection().addRange(selected);   
            }
    
        }
    },
    mounted(){
        this.getStyle();
    },
    watch:{
        theme(){
            this.getStyle();
        }
    }
}
</script>


<style>
@import '../styles/theme.css';
@import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro&display=swap');
.code{
    background-color:var(--code-bg-color);
    color:var(--code-color);
    border-radius: 5px;
    position:relative;
    margin:20px 0;

    display:flex;
    flex-direction:column;
    justify-content:center;
    font-family: 'Source Code Pro', monospace;

}
.code-head{
    display:flex;
    flex-direction:row;
    justify-content:space-between;
    align-items:center;
    padding:10px;
    color:var(--code-h-color);
}
.code-head .copy-btn{
    cursor:pointer;
    color:var(--code-color);
    font-size:20px;
    transition:all 0.3s;
}
.code-head .copy-btn:hover{
    color:var(--code-h-color);
}

.code-body{
    padding:10px;
    overflow-x: auto;
}

.keyword{
    color:var(--code-keyword-color);
}

/*animation */

</style>