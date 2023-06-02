<script setup>
import axios from "axios";
import {onBeforeUpdate, onMounted, reactive, ref} from "vue";
import {removeToken} from "../../auth.js";
import router from "../../route.js";
import {ElMessage} from "element-plus";

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

const form_column = ref([]);

const handleEdit = (index,row) => {
    // console.log(row);
    form_column.value = row;
    // console.log(form_column.value);
    edit();
    // form_column.value=[];
}
const handleDelete = (index, row) => {
    const params = new URLSearchParams()
    params.append('ID', row.id)
    params.append('name', row.name)
    params.append('gender', row.gender)
    axios.post('/api/delete', params).then(res => {
        if (res.data.code === 200) {
            ElMessage({
                message: '删除成功',
                type: "success"
            });
            tableData.splice(index, 1);
            // router.go(0);
        } else {
            ElMessage({
                message: '删除失败',
                type: 'error'
            })
        }
    })
}

//控制编辑窗口的显示
const edit_dialog = ref(false);
const edit = () => {
    edit_dialog.value = true;
    console.log(("修改"));
}
</script>

<template>
    <el-table stripe border style="width: 100%" :data="tableData" :table-layout="'auto'">
        <el-table-column prop="id" label="学号" width="180"/>
        <el-table-column prop="name" label="姓名" width="180"/>
        <el-table-column prop="gender" label="性别" width="180"/>
        <el-table-column prop="major" label="专业" width="180"/>
        <el-table-column prop="phone" label="手机号"/>
        <el-table-column label="Operations">
            <template #default="scope">
                <el-button size="small" @click="handleEdit(scope.$index, scope.row)"
                >编辑
                </el-button
                >
                <el-button
                        size="small"
                        type="danger"
                        @click="handleDelete(scope.$index, scope.row)"
                >删除
                </el-button
                >
            </template>
        </el-table-column>
    </el-table>
    <Edit v-model:dialog-form-visible="edit_dialog" :form="form_column"/>
</template>
<script>
import Edit from "./dialog/edit.vue";

export default {
    name: "student_table",
    components: {
        Edit,
    }
}
</script>

