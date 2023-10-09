import { createRouter, createWebHistory } from 'vue-router'
// import store from '../store'

const routes = [
  {
    path: '/app',
    name: 'home',
    component: () => import('../views/HomeView.vue')
  },

  // передача переменных в запросе
  {
    path: '/app/:id',
    name: 'homeParam',
    component: () => import('../views/HomeParam.vue')
  },

  {
    path: '/app/about',
    name: 'about',
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/app/login',
    name: 'login',
    component: () => import('../views/LoginView.vue')
  },
  {
    path: '/app/register',
    name: 'register',
    component: () => import('../views/RegisterView.vue')
  },

  // перенаправление на "главную". В джанге пишем юрл, что при 127.0.0.1:8000/app перенаправляй на index.html
  {
    path: '/',
    redirect: '/app',
  },

  // обработка 404
  {
    path: "/:catchAll(.*)",
    name: "NotFound",
    component: () => import('../views/404View.vue')
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Если система детектид, что мы неавторизованы, то она автоматически кидает нас на авторизацию (логин)

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
//     next({ name: 'login', query: { to: to.path } });
//   } else {
//     next()
//   }
// })

export default router
