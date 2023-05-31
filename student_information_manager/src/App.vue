<script setup xmlns="http://www.w3.org/1999/html">
import axios from 'axios'
import {reactive, ref, onMounted} from "vue";
import {ElMessageBox} from "element-plus";
import Login from "./components/login.vue";

const books = reactive([])

const getStudents = () => {
    axios.get("http://localhost:5000/books/",).then(res => {
        books.splice(0, books.length);
        books.push(...res.data.result);
        console.log('更新数据');
    })
    //页面渲染之后添加数据
    onMounted(() => {
        getStudents();
    })
    //删除数据
    const handleDelete = (index, scope) => {

    }
}
</script>

<template>
    <div class="body">
        <div class="nav">
            <div class="inside">
                <router-link to="/">首页</router-link>
                <router-link to="/manager">Manager</router-link>

            </div>
            <div class="login">
                <router-link to="/login">Login</router-link>
            </div>


        </div>
        <div class="view">
            <router-view></router-view>
        </div>
    </div>

</template>

<script>
    // Cookies.set("name", {foo: "bar"});
</script>
<style>

.nav * {
    float: left;
    text-decoration: none;
    width: auto;
    height: auto;
    /*margin-left: 40px;*/
}

.inside {
    position: fixed;
    left: 40%;
    /*background-color: aqua;*/
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

.view {
    padding-top: 100px;
}

</style>