import login from "./components/login.vue";
import register from "./components/register.vue";
import Home from "./components/home.vue";
import manager from './components/manager.vue';
import {createRouter, createWebHistory} from 'vue-router'
import Cookies from "js-cookie";
import {getToken} from "./auth.js";
import Manager from "./components/manager.vue";
import about from "./components/about.vue";
//定义路由
const routes = [
    {
        path: '/',
        component: Home
    },
    {
        path: '/manager',
        component: Manager,
        meta: {
            requireAuth: true,
        }
    },
    {
        path: '/login',
        component: login
    },
    {
        path: '/register',
        component: register
    },
    {
        path:'/about',
        component: about
    }

];
//路由
const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach(function (to, from, next) {
    if (to.meta.requireAuth && !getToken()) {
        // alert("请先登录");
        next('/login');
    } else {
        next();
    }
})

export default router;