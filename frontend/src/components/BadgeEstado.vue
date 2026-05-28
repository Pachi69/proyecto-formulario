<script setup>
// Muestra el estado del tramite (Pending/Accepted/Rejected)
import { computed } from 'vue'

const props = defineProps({
    status: String
})

const config = computed(() => {
    switch (props.status) {
        case 'Accepted': return { text: 'Aprobado', class: 'bg-green-100 text-green-700 border-green-200' }
        case 'Rejected': return { text: 'Rechazado', class: 'bg-red-100 text-red-700 border-red-200' }
        default: return { text: 'Pendiente', class: 'bg-yellow-100 text-yellow-700 border-yellow-200' }
    }
})
</script>

<template>
    <span :class="['border px-3 py-1 rounded-full text-sm font-semibold', config.class]">
        {{ config.text }}
    </span>
</template>