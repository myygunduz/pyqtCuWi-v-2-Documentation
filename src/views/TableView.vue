<template>
    <div class="table">
        <div class="header">
            <div class="header-item"
            v-for="(title,index) in data.header"
            :key="index">
            {{title}}</div>
        </div>
        <div class="rows"
        v-for="(row,index) in data.rows"
        :key="index">
            <div class="row"
            v-for="(cell,index) in row"
            :key="index">
            {{cell}}</div>
        </div>
        <div class="footer"
        v-for="(note,index) in data.footer"
        :key="index"
        :id="note.mode">
            <i class="fa-solid fa-triangle-exclamation" v-if="note.mode=='warning'"></i>
            <i class="fa-solid fa-circle-info" v-if="note.mode=='info'"></i>

            <p>{{note.title}}</p>
            <p>{{note.content}}</p>
        </div>
        <div v-if="data.footer==''">
            <br>
        </div>
    </div>
</template>

<script>
export default{
    name:'TableView',
    props:{
        data:{
            type:Array,
            default:function(){
                return []
            }
        }
    }
}
</script>



<style>
@import '../styles/theme.css';

.table{
    width:100%;
    background-color: var(--table-bg-color);
    border-radius:12px;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    margin:20px 0;
}

.header{
    background-color: var(--table-bg-color);
    border-top-left-radius: 12px;
    border-top-right-radius: 12px;
}

.header,
.rows{
    width: 100%;
    display:flex;
    align-items: center;
    justify-content: space-around;

    border-bottom: 1px solid var(--table-bg-color);

    padding:5px 10px;
}
.rows:hover{
    background-color: var(--table-row-hover-bg-color);
}

.header-item{
    width:100%;
    height:100%;
    font-size:20px;
    color: var(--table-color);

    
    text-align: center;
}

.row{
    width: 100%;
    display:flex;
    align-items: center;
    padding:0 5px;
}

.footer{
    width: 100%;
    display:flex;
    align-items: center;
    padding:5px 10px;
    border-radius: 20px;
    margin:10px;
}

#warning{
    background-color: var(--table-warning-bg-color);
    color: var(--table-warning-color);
    border:2px solid var(--table-warning-color);
    display: grid;
    grid-template-columns: 5% 10% 80%;
}
#info{
    background-color: var(--table-info-bg-color);
    color: var(--table-info-color);
    border:2px solid var(--table-info-color);
    display: grid;
    grid-template-columns: 5% 10% 80%;
}

</style>