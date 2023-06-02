<script setup>
import {onMounted, ref} from 'vue'
import {getToken} from "../../auth.js";

const activeIndex = ref('1')
let show_login = ref(true)
//判断当前用户是否已经登录
onMounted(function () {
    let token = getToken();
    if (token) {
        show_login.value = false;
    }
})
//处理下拉框选择
const handleSelect = (key, keyPath) => {
    if (key === "2-1") {
        add();
        // console.log(add_dialog.value);
    } else if (key === "2-2") {
        Del();
    }
}
//增加
const add_dialog = ref(false);
const add = () => {
    add_dialog.value = true;
    console.log("增加");
}
const del_dialog = ref(false);
const Del = () => {
    del_dialog.value = true;
    console.log(("删除"));
}

</script>
<template>
    <div class="header">
        <el-menu
                :default-active="activeIndex"
                class="el-menu-demo Menu"
                mode="horizontal"
                @select="handleSelect"
        >
            <el-menu-item index="1">学生信息管理系统</el-menu-item>
            <el-sub-menu index="2">
                <template #title>编辑</template>
                <el-menu-item index="2-1">
                    添加
                </el-menu-item>
                <el-menu-item index="2-2">查询</el-menu-item>
            </el-sub-menu>
            <el-menu-item index="3" disabled>Info</el-menu-item>
        </el-menu>
        <ul class="login" v-if="show_login">
            <li>
                <router-link to="/login">login</router-link>
            </li>
        </ul>
        <ul class="user" v-if="!show_login">
            <li>
                <Avatar/>
            </li>
        </ul>
    </div>
    <div class="h-6"/>
    <Add v-model:dialog-form-visible="add_dialog"/>
    <Query v-model:dialog-form-visible="del_dialog"/>
</template>

<script>
import Avatar from "./avatar.vue";
import Query from "./dialog/query.vue";
import Edit from "./dialog/edit.vue";
import Add from "./dialog/add.vue";

export default {
    name: "Menu",
    components: {
        Avatar,
        Add,
        Query,
        Edit,
    }
}
</script>
<style scoped>
.header {
    display: flex;
    justify-content: space-between;
}

.Menu {
    width: 100%;
}

.user {
    margin: 0;
    padding: 0;
    list-style-type: none;
}

.user {

}

.login {
    margin: 0;
    padding: 0;
    list-style-type: none;
}

.login ul {
    display: flex;
    align-items: center;
}

.login li {
    display: flex;
    float: left;
    position: relative;
    width: 150px;
    height: 50px;
    align-items: center;
    border: 2px solid #409eff;
}

.login a {
    color: #409eff;
    position: relative;
    font-size: 14px;
    font-weight: 300;
    width: 200px;
    text-align: center;
    /*left: 50px;*/
    text-transform: uppercase;
    background-color: transparent;
    text-decoration: none;
}

.login li:hover a {
    color: white;
}

.login li:hover {
    border-radius: 12px;
    background-color: #409eff;
    -webkit-transition-duration: 1.5s;
    transition-duration: 1.5s;
    -webkit-box-shadow: 10px 10px 99px 6px #409eff;
    -moz-box-shadow: 10px 10px 99px 6px #409eff;
    box-shadow: 10px 10px 99px 6px #409eff;
}


</style>