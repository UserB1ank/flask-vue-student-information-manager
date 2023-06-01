<script setup>
import {ref} from 'vue'
import axios from "axios";

import {reactive} from 'vue'
import {getToken, removeToken, setToken} from "../auth.js";
import router from "../route.js";


const form = reactive({
    username: '',
    password: ''
})

const onSubmit = function () {
    removeToken();
    const params = new URLSearchParams();
    params.append("username", form.username);
    params.append("password", form.password);
    axios.post("/api/login", params).then(res => {
        let token = res.data.data["token"];
        // alert(token);
        if (token) {
            setToken(token);
            router.push('/manager')
        } else {
            alert("登录失败，错误的用户名或者密码");
        }
    }).catch(error => {
        console.log(error);
    })
}

const onRegister = () => {
    router.push('/register');
    return true
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
                <el-button @click="onRegister">注册</el-button>
                <el-button type="primary" @click="onSubmit">登录</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>
<script>

</script>

<style scoped>
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
