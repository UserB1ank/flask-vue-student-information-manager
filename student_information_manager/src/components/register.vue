<script setup>
import axios from "axios";

import {reactive, ref} from 'vue'
import {ElMessage} from "element-plus";
import router from "../route.js";
import Home_nav from "./part/home_nav.vue";

const labelPosition = ref('right')

const formLabelAlign = reactive({
    username: '',
    password: '',
    phone: '',
})
const onSubmit = function () {
    const params = new URLSearchParams();
    params.append('username', formLabelAlign.username)
    params.append('password', formLabelAlign.password)
    params.append('phone', formLabelAlign.phone)
    axios.post("/api/register", params).then(res => {
        router.push('/login')
        ElMessage({
            message: res.data.message + '，请登录',
            type: "success"
        })
    }).catch(e => {
        ElMessage({
            message: e.message,
            type:'error'
        })
    })
}

</script>

<template>
    <home_nav/>
    <div style="margin: 20px "/>
    <div class="outside">
        <h1>注册</h1>
        <el-form
                label-width="100px"
                :model="formLabelAlign"
                style="max-width: 460px"
                class="form"
        >
            <el-form-item label="账号">
                <el-input v-model="formLabelAlign.username"/>
            </el-form-item>
            <el-form-item label="密码">
                <el-input v-model="formLabelAlign.password" show-password/>
            </el-form-item>
            <el-form-item label="电话号码">
                <el-input v-model="formLabelAlign.phone"/>
            </el-form-item>
            <el-form-item class="my_button">
                <el-button type="primary" @click="onSubmit">注册</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>


<script>
export default {
    name: "register"
}
</script>

<style scoped>
.outside {
    /*background-color: #409eff;*/
    height: 800px;
}

h1 {
    position: relative;
    top: 20%;
    left: 49%;
}

button {
    position: relative;
    left: 40%;
}

.form {
    position: relative;
    top: 20%;
    left: 35%;
}
</style>