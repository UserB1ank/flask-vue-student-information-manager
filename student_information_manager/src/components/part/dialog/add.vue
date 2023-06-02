<template>
  <!-- Form -->
    <el-dialog :model-value="dialogFormVisible" title="添加" :close-on-click-modal="false" :show-close="false"
               :destroy-on-close="true">
        <el-form :model="form">
            <el-form-item label="学号" :label-width="formLabelWidth">
                <el-input v-model="form.ID" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="姓名" :label-width="formLabelWidth">
                <el-input v-model="form.name" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="性别" :label-width="formLabelWidth">
                <el-input v-model="form.gender" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="专业" :label-width="formLabelWidth">
<!--                <el-select v-model="form.major" placeholder="请选择专业">-->
<!--                    <el-option label="软件工程" value="软件工程"/>-->
<!--                    <el-option label="计算机科学与技术" value="计算机科学与技术"/>-->
<!--                </el-select>-->
                <el-input v-model="form.major" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="电话" :label-width="formLabelWidth">
                <el-input v-model="form.phone" autocomplete="off"/>
            </el-form-item>
        </el-form>
        <template #footer>
      <span class="dialog-footer">
        <el-button @click="$emit('update:dialogFormVisible',false);clear();">取消</el-button>
        <el-button type="primary" @click="submit">
          确定
        </el-button>
      </span>
        </template>
    </el-dialog>
</template>

<script setup>
import {reactive, ref} from 'vue'
import axios from "axios";
import {ElMessage} from "element-plus";
import router from "../../../route.js";

//添加成功的消息提示
const emits = defineEmits(['update:dialogFormVisible']);
// const dialogFormVisible = ref(false)
const formLabelWidth = '140px'
const form = reactive({
    ID: '',
    name: '',
    gender: '',
    major: '',
    phone: ''
})
const submit = function () {
    const params = new URLSearchParams()
    params.append("id", form.ID)
    params.append('name', form.name)
    params.append('gender', form.gender)
    params.append('major', form.major)
    params.append('phone', form.phone)
    axios.post('/api/add', params).then(res => {
        if (res.data.code === 200) {
            emits('update:dialogFormVisible', false);
            ElMessage({
                message: '添加成功',
                type: 'success',
            })
            setTimeout(()=>{
                router.go(0)
            },800);
            clear();
        } else {
            ElMessage({
                message: "添加失败",
                type: 'error'
            })
        }
        // console.log(res.data);
    })
}
const clear = function () {
    // console.log(form);
    form.name = '';
    form.ID = '';
    form.phone = '';
    form.gender = '';
    form.major = '';
}
</script>


<style scoped>
.dialog-footer button:first-child {
    margin-right: 10px;
}
</style>


<script>
import {ElMessage} from "element-plus";

export default {
    name: "Add",
    props: {
        dialogFormVisible: {
            type: Boolean,
        },

    }
}
</script>

<style scoped>

</style>