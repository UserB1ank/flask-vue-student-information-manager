<script setup>
import axios from "axios";
import {onMounted} from "vue";

onMounted(()=>{
    // axios.get()
})
</script>

<template>
    <el-table :data="tableData" style="width: 100%">
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

