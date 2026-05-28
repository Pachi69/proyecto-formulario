// Define las rutas de la aplicación
import ConsultaEstadoView from '@/views/ConsultaEstadoView.vue'
import FormularioView from '@/views/FormularioView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'form',
    component: FormularioView,
    meta: { requiresAuth: false },
  },
  {
    path: '/check',
    name: 'check',
    component: ConsultaEstadoView,
    meta: { requiresAuth: false },
  }
]


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
})

export default router
