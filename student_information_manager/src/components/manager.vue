<template>
    <Menu/>
    <div class="body">
        <student_table/>
    </div>

</template>

<script>
import Menu from "./part/menu.vue";
import Student_table from "./part/student_table.vue";

export default {
    name: "manager",
    components: {
        Student_table,
        Menu,
    }
}
</script>

<style scoped>
.nav * {
    float: left;
    text-decoration: none;
    width: auto;
    height: auto;
}

.inside {
    position: fixed;
    left: 40%;
}

.inside a {
    margin-left: 80px;
}

.login a {
    position: fixed;
    left: 90%;
    text-align: right;
    background-color: yellow;

}
</style>