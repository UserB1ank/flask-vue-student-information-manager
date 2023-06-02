<template>
  <!-- Form -->
    <el-dialog :model-value="dialogFormVisible" title="编辑" :close-on-click-modal="false" :show-close="false">
        <el-form :model="form">
            <el-form-item label="Promotion name" :label-width="formLabelWidth">
                <el-input v-model="form.name" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="Zones" :label-width="formLabelWidth">
                <el-select v-model="form.region" placeholder="Please select a zone">
                    <el-option label="Zone No.1" value="shanghai"/>
                    <el-option label="Zone No.2" value="beijing"/>
                </el-select>
            </el-form-item>
        </el-form>
        <template #footer>
      <span class="dialog-footer">
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


// const dialogFormVisible = ref(false)
const formLabelWidth = '140px'
const form = reactive({
    name: '',
    region: '',
    date1: '',
    date2: '',
    delivery: false,
    type: [],
    resource: '',
    desc: '',
})
</script>
<style scoped>
.dialog-footer button:first-child {
    margin-right: 10px;
}
</style>


<script>
export default {
    name: "Edit",
    props: {
        dialogFormVisible: {
            type: Boolean,
        }
    }
}
</script>

<style scoped>

</style>