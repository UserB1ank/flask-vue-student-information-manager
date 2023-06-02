<template>
    <home_nav/>

    <el-descriptions title="Author">
        <el-descriptions-item label="Username">userb1ank</el-descriptions-item>
        <el-descriptions-item label="Telephone">18100000000</el-descriptions-item>
        <el-descriptions-item label="Place">Suzhou</el-descriptions-item>
        <el-descriptions-item label="University">
            <el-tag size="small">CCZU</el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="Address"
        >Xiangcheng District, Suzhou, Jiangsu
            Province
        </el-descriptions-item
        >
    </el-descriptions>


</template>

<script>
import Home_nav from "./part/home_nav.vue";

export default {
    name: "about",
    components: {Home_nav}
}
</script>

<style scoped>

</style>