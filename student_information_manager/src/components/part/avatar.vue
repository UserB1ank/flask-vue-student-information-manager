<script setup>
import {UserFilled} from '@element-plus/icons-vue'
</script>
<template>
    <div class="demo-type">
        <div>
            <el-avatar
                    src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
            />
        </div>
    </div>
</template>

<script>
export default {
    name: "Avatar"
}
</script>


<style scoped>
.demo-type {
    display: flex;
}

.demo-type > div {
    flex: 1;
    text-align: center;
}

.demo-type > div:not(:last-child) {
    border-right: 1px solid var(--el-border-color);
}
</style>
