<template>
  <!-- Form -->
    <el-dialog :model-value="dialogFormVisible" title="查询" :close-on-click-modal="false" :show-close="false">
        <el-form :model="form">
            <el-form-item label="学号" :label-width="formLabelWidth">
                <el-input v-model="form.ID" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="查询结果" :label-width="formLabelWidth">
                <el-form-item label="姓名">
                    <el-input v-model="form.name" autocomplete="off" disabled/>
                </el-form-item>
                <el-form-item label="性别">
                    <el-input v-model="form.gender" autocomplete="off" disabled/>
                </el-form-item>
                <el-form-item label="专业">
                    <el-input v-model="form.major" autocomplete="off" disabled/>
                </el-form-item>
                <el-form-item label="电话">
                    <el-input v-model="form.phone" autocomplete="off" disabled/>
                </el-form-item>
            </el-form-item>
        </el-form>
        <template #footer>
      <span class="dialog-footer">
        <el-button type="primary" @click="query">
          查询
        </el-button>
        <el-button @click="$emit('update:dialogFormVisible',false)">取消</el-button>
      </span>
        </template>
    </el-dialog>
</template>

<script setup>
import {reactive, ref} from 'vue'
import axios from "axios";
import {ElMessage} from "element-plus";

const formLabelWidth = '140px'
const form = reactive({
    ID: '',
    name: '',
    gender: '',
    major: '',
    phone: ''
})
const query = function () {
    const params = new URLSearchParams();
    params.append("ID", form.ID);
    axios.post("/api/query", params).then(function (res) {
        if (res.data.code === 200) {
            form.name = res.data.data.name;
            form.gender = res.data.data.gender;
            form.major = res.data.data.major;
            form.phone = res.data.data.phone;
            ElMessage({
                message: "查询成功",
                type: "success"
            })
        } else {
            ElMessage({
                message: "查询失败",
                type: "error"
            })
        }
    })
}


</script>
<style scoped>
.dialog-footer button:first-child {
    margin-right: 10px;
}
</style>


<script>
export default {
    name: "Query",
    props: {
        dialogFormVisible: {
            type: Boolean,
        }
    }
}
</script>
