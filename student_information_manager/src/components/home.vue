<template>
    <home_nav/>
    <div class="body">
    </div>

</template>

<script>
import Menu from "./part/menu.vue";
import Student_table from "./part/student_table.vue";
import home_nav from "./part/home_nav.vue";

export default {
    name: "Home",
    components: {
        Student_table,
        home_nav,
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