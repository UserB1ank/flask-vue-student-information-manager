<template>
    <div>
        <el-col>
            <el-input
                    v-model="input"
                    type="password"
                    placeholder="Please input password"
                    show-password
            />
        </el-col>
    </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
const input = ref('')
</script>

<style scoped>

</style>