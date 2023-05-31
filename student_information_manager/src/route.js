import login from "./components/login.vue";
import manager from "./components/manager.vue";
import register from "./components/register.vue";
import Main from "./App.vue"
import {createRouter, createWebHistory} from 'vue-router'
import {getToken, setToken} from "./auth.js";
//定义路由
const routes = [
    {
        path: '/',
        component: Main
    },
    {
        path: '/login',
        component: login
    },
    {
        path: '/manager',
        component: manager,
        meta: {
            requireAuth: true,
        }
    },
    {
        path: '/register',
        component: register
    }

];
//路由
const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach(function (to, from, next) {
    if (to.meta.requireAuth&&!document.cookie) {
        console.log("需要验证");
        next('/');
    } else {
        next();
    }
})

export default router;