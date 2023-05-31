<script setup>
import {ref} from 'vue'
import axios from "axios";

import {reactive} from 'vue'
import {getToken, setToken} from "../auth.js";


const form = reactive({
    username: '',
    password: ''
})


const onSubmit = function () {
    const params = new URLSearchParams();
    params.append("username", form.username);
    params.append("password", form.password);
    axios.post("/api/login", params).then(res => {
        document.cookie = "token=" + res.data.data["token"];

        console.log(res.data.data);
    }).catch(error => {
        console.log(error);
    })
}
</script>
<template>
    <div class="my_div">
        <el-form :model="form" class="my_form">
            <el-form-item label="账号">
                <el-col>
                    <el-input
                            v-model="form.username"
                            placeholder="请输入账号"

                    />
                </el-col>
            </el-form-item>
            <el-form-item label="密码">
                <el-col>
                    <el-input
                            v-model="form.password"
                            type="password"
                            placeholder="请输入密码"
                            show-password
                    />
                </el-col>
            </el-form-item>
            <el-form-item class="my_button">
                <el-button>注册</el-button>
                <el-button type="primary" @click="onSubmit">登录</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>
<script>

</script>

<style>
.my_div {
    position: fixed;
    left: 25%;
    top: 10%;
    width: 1000px;
    height: 2000px;
    /*background-color: yellow;*/
}

.my_form {
    display: block;
    position: relative;
    /*background-color: red;*/
    left: 300px;
    top: 100px;
    width: 400px;
}

.my_button {
    position: relative;
    top: 20px;
    left: 35%;
}

</style>
