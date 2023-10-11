import Vue, {h} from 'vue'
import Router from 'vue-router'
import Login from '@/views/Login'
import Register from '@/views/Register'
import Main from '@/views/Main'
import HelloWorld from '@/components/HelloWorld'
import a from '@/components/Cha_comp/a'
import b from '@/components/Cha_comp/b'
import c from '@/components/Cha_comp/c'
import d from '@/components/Cha_comp/d'
import aa from '@/components/Cha_comp/aa'
import i3 from "../components/Mana_comp/i3.vue";
import h3 from "../components/Mana_comp/h3.vue";
import g3 from "../components/Mana_comp/g3.vue";
import f3 from "../components/Mana_comp/f3.vue";
import j3 from "../components/Mana_comp/j3.vue";

Vue.use(Router)

export default new Router({
  routes: [
    {
      //登录
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      // 注册
      path: '/Register',
      name: 'Register',
      component: Register,
    },
    {
      // 首页
      path: '/Main',
      name: 'Main',
      component: Main,
      children: [
        {
          // 个人信息
          path: "/aa",
          name: "aa",
          component: aa,
        },
        {
          // 提交成绩单
          path: "/a",
          name: "a",
          component: a,
        },
        {
          // 提交综测信息
          path: "/b",
          name: "b",
          component: b,
        },
        {
          // 就业预测
          path: "/c",
          name: "c",
          component: c,
        },
        {
          // 操作记录
          path: "/d",
          name: "d",
          component: d,
        },
        {
          // 申请信息
          path: "/f3",
          name: "f3",
          component: f3,
        },
        {
          // 文件上传
          path: "/g3",
          name: "g3",
          component: g3,
        },
        {
          // 权限管理
          path: "/h3",
          name: "h3",
          component: h3,
        },
        {
          // 组织管理
          path: "/i3",
          name: "i3",
          component: i3,
        },
        {
          // 重置密码
          path: "/j3",
          name: "j3",
          component: j3,
        },
      ]
    }

  ]
})
