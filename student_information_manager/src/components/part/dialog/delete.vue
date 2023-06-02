<template>
  <!-- Form -->
    <el-dialog :model-value="dialogFormVisible" title="删除" :close-on-click-modal="false" :show-close="false">
        <el-form :model="form">
            <el-form-item label="学号" :label-width="formLabelWidth">
                <el-input v-model="form.ID" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="Zones" :label-width="formLabelWidth">
            </el-form-item>
        </el-form>
        <template #footer>
      <span class="dialog-footer">
        <el-button type="primary" @click="query">
          查询
        </el-button>
        <el-button @click="$emit('update:dialogFormVisible',false)">取消</el-button>
        <el-button type="primary" @click="$emit('update:dialogFormVisible',false)">
          确定
        </el-button>
      </span>
        </template>
    </el-dialog>
</template>

<script setup>
import {reactive, ref} from 'vue'
import axios from "axios";

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
    axios.post("/api/query",params).then(function (res) {
        console.log(res.data);
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
    name: "Delete",
    props: {
        dialogFormVisible: {
            type: Boolean,
        }
    }
}
</script>

<style scoped>

</style>