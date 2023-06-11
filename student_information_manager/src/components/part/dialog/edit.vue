<template>
  <!-- Form -->
    <el-dialog :model-value="dialogFormVisible" title="编辑" :close-on-click-modal="false" :show-close="false">
        <el-form :model="form">
            <el-form-item label="学号" :label-width="formLabelWidth">
                <el-input v-model="form.id" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="姓名" :label-width="formLabelWidth">
                <el-input v-model="form.name" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="性别" :label-width="formLabelWidth">
                <el-input v-model="form.gender" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="专业" :label-width="formLabelWidth">
                <el-input v-model="form.major" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="电话" :label-width="formLabelWidth">
                <el-input v-model="form.phone" autocomplete="off"/>
            </el-form-item>
        </el-form>
        <template #footer>
      <span class="dialog-footer">
        <el-button @click="$emit('update:dialogFormVisible',false)">取消</el-button>
        <el-button type="primary" @click="submit">
          确定
        </el-button>
      </span>
        </template>
    </el-dialog>
</template>

<script setup>
import {reactive, ref} from 'vue'

//保存初始的数据用于查询

//修改后的数据

const formLabelWidth = '140px'
</script>
<style scoped>
.dialog-footer button:first-child {
    margin-right: 10px;
}
</style>


<script>
import axios from "axios";
import {ElMessage} from "element-plus";
import router from "../../../route.js";
import {ref} from "vue";
const backup = ref({})
export default {
    name: "Edit",

    props: {
        dialogFormVisible: {
            type: Boolean,
        },
        form: {
            type: Object,
        }
    },
    methods: {
        submit: function () {
            backup.value = this.form
            const params = new URLSearchParams();
            console.log(backup.value);
            params.append("backup_id", backup.value.id);
            params.append("data_id", this.form.id);
            params.append("data_name", this.form.name);
            params.append("data_gender", this.form.gender);
            params.append("data_major", this.form.major);
            params.append("data_phone", this.form.phone);
            axios.post("/api/update", params).then(res => {
                if (res.data.code === 200) {
                    ElMessage({
                        message: res.data.message,
                        type: 'success'
                    })
                    this.$emit('update:dialogFormVisible', false);

                    setTimeout(() => {
                        router.go(0);
                    }, 800);
                } else {
                    ElMessage({
                        message: res.data.message,
                        type: 'error'
                    })
                }
            })
        }
    }
}
</script>

<style scoped>

</style>