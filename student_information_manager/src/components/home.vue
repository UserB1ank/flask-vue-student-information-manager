<script setup>
import url from '../assets/2.png'

</script>
<template>
    <home_nav/>
    <div class="body">
        <el-image class="img" :src="url" />
    </div>

</template>

<script>
import Student_table from "./part/student_table.vue";
import home_nav from "./part/home_nav.vue";

export default {
    name: "Home",
    components: {
        Student_table,
        home_nav,
    },
}
</script>

<style scoped>
.nav * {
    float: left;
    text-decoration: none;
    width: auto;
    height: auto;
}



.inside a {
    margin-left: 80px;
}

.login a {
    position: fixed;
    left: 90%;
    text-align: right;
    background-color: yellow;

}

.demonstration {
    color: var(--el-text-color-secondary);
}

.el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
}
.img{
    height: 700px;
    position: relative;
    left: 300px;
    top:20px;
}
</style>