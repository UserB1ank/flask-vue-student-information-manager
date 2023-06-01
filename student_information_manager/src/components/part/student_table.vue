<script setup>
import axios from "axios";
import {onBeforeUpdate, onMounted, ref} from "vue";

const tableData = ref();
onMounted(() => {
    axios.get("/api/manager").then(function (res) {
        // let data = JSON.parse(res.data);
        console.log(res.data);
    })
})
</script>

<template>
    <el-table style="width: 100%" v-model="tableData">
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

