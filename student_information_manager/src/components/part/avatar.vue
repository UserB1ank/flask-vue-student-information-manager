<script setup>
import {ArrowDown} from '@element-plus/icons-vue'
import {removeToken} from "../../auth.js";
import {ElMessage} from "element-plus";
import router from "../../route.js";
import {onMounted, ref} from "vue";
import axios from "axios";

const logout = () => {
    // console.log("213")
    removeToken();
    setTimeout(() => {
        router.go(0);
    }, 1000)
    ElMessage({
        message: "注销成功",
        type: "success",
    })
}

const imageUrl = ref('');
onMounted(function () {
    axios.get('/api/avatar').then(function (res) {
        imageUrl.value = res.data.data;
    })
})
</script>
<template>
    <div class="demo-type">

        <el-dropdown>
            <el-button type="primary" class="dropdown">
                <div>
                    <el-avatar
                            :src="imageUrl"
                    />
                </div>
            </el-button>
            <template #dropdown>
                <el-dropdown-menu>
                    <el-dropdown-item @click="router.push('/')">首页</el-dropdown-item>
                    <el-dropdown-item @click="router.push('/manager')">学生信息管理系统</el-dropdown-item>
                    <el-dropdown-item @click="router.push('/information')">个人信息</el-dropdown-item>
                    <el-dropdown-item @click="logout">注销</el-dropdown-item>
                </el-dropdown-menu>
            </template>
        </el-dropdown>
    </div>
</template>

<script>
export default {
    name: "Avatar",
}
</script>


<style scoped>
.demo-type {
    display: flex;
}

.demo-type > div {
    flex: 1;
    text-align: center;
}

.demo-type > div:not(:last-child) {
    border-right: 1px solid var(--el-border-color);
}

.example-showcase .el-dropdown + .el-dropdown {
    margin-left: 15px;
}

.example-showcase .el-dropdown-link {
    cursor: pointer;
    color: var(--el-color-primary);
    display: flex;
    align-items: center;
}

.dropdown {
    height: 50px;
}
</style>
