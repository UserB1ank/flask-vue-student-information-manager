<script setup>
import axios from "axios";
import {onBeforeUpdate, onMounted, reactive, ref} from "vue";
import {removeToken} from "../../auth.js";
import router from "../../route.js";

const tableData = reactive([]);
onMounted(() => {
    axios.get("/api/manager").then(function (res) {
        if (res.data.code === 200) {
            tableData.push(...res.data.data);
        } else {//如果token验证失败
            removeToken()
            router.push('/')
        }
    })
})
</script>

<template>
    <el-table style="width: 100%" :data="tableData">
        <el-table-column prop="id" label="学号" width="180"/>
        <el-table-column prop="name" label="姓名" width="180"/>
        <el-table-column prop="gender" label="性别" width="180"/>
        <el-table-column prop="major" label="专业" width="180"/>
        <el-table-column prop="phone" label="手机号"/>
    </el-table>
</template>
<script>
export default {
    name: "student_table"
}
</script>

