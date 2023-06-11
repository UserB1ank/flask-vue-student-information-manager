<script setup>
import {ref} from "vue";
import {ElMessage} from 'element-plus'
import {Plus} from '@element-plus/icons-vue'
import axios from "axios";

//头像上传功能
const imageUrl = ref('')
const uploadRef = ref(null)

const submitUpload = () => {
    uploadRef.value.submit()
}

//上传前显示头像
const handleFileChange = (uploadFile) => {
    imageUrl.value = URL.createObjectURL(uploadFile.raw)
};

//上传成功后设置头像
const handleAvatarSuccess = function (response, uploadFile) {
    if (response.code === 200) {
        imageUrl.value = URL.createObjectURL(uploadFile.raw);
        ElMessage.success(response.message);
    } else {
        ElMessage.error(response.message);
    }
};


//before upload钩子
const beforeAvatarUpload = function (rawFile) {
    let white_lst = ['image/jpeg', 'image/png'];
    if (!white_lst.includes(rawFile.type)) {
        ElMessage.error('图片必须是 JPG|PNG|JPEG 格式!');
        return false;
    } else if (rawFile.size / 1024 / 1024 > 2) {
        ElMessage.error('图片大小不能超过2M!');
        return false;
    }
    return true;
};


</script>


<template>
    <home_nav/>
    <el-upload
            class="avatar-uploader"
            :show-file-list="false"
            :auto-upload="false"
            action="/api/avatar"
            :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload"
            :on-change="handleFileChange"
            ref="uploadRef"
    >
        <img v-if="imageUrl" :src="imageUrl" class="avatar" alt="#"/>
        <el-icon v-else class="avatar-uploader-icon">
            <Plus/>
        </el-icon>
    </el-upload>
    <el-form ref="form" :model="formData" label-width="100px"
             style="max-width: 400px; margin: 0 auto;">
        <el-form-item>
            <el-button type="primary" @click="submitUpload">保存</el-button>
        </el-form-item>
    </el-form>

</template>

<script>
import {ref} from 'vue';
import home_nav from "./part/home_nav.vue";

export default {
    name: 'information',
    components: {
        home_nav
    }
};
</script>


<style>
.avatar-uploader {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 50px; /* 调整上边距 */
    margin-bottom: 50px;
}

.avatar-uploader .avatar {
    width: 178px;
    height: 178px;
    display: block;

}

.avatar-uploader .el-upload {
    border: 1px dashed var(--el-border-color);
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
    border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    text-align: center;
}
</style>