<script setup>
// Vista para que el cliente consulte su tramite por email
import { ref } from 'vue';
import { getFormByEmail } from '@/services/formServices';
import BadgeEstado from '@/components/BadgeEstado.vue';

const email = ref('');
const tramite = ref(null);
const error = ref('');
const loading = ref(false);

async function search() {
    error.value = ''
    tramite.value = null
    loading.value = true
    try {
        const response = await getFormByEmail(email.value)
        tramite.value = response.data
    } catch (err) {
        if (err.response?.status === 404) {
            error.value = 'No se encontro ningun tramite para ese email'
        } else {
            error.value = 'Error al buscar el tramite'
        }
    } finally {
        loading.value = false
    }
}



</script>
<template>
    <div class="p-3">
        <div class="mt-5 p-4 bg-slate-300 max-w-3xl mx-auto rounded-xl">
            <label class="font-bold text-gray-600 text-xs leading-8 uppercase h-6 mx-2">Email</label>
            <div class="flex gap-2 mt-2">
                <div class="bg-white flex-1 p-1 flex border border-gray-200 rounded-xl">
                    <input type="email" v-model="email" placeholder="jhon@doe.com" class="p-1 px-2 appearance-none outline-none w-full text-gray-800">
                </div>
                <button @click="search" class="bg-slate-400 px-4 py-1.5 rounded-lg text-base font-medium text-slate-800 hover:bg-slate-500 transition-colors">
                    Buscar
                </button>
            </div>
        </div>

        <div v-if="error" class="bg-red-50 border border-red-200 text-red-700 text-lg font-medium px-3 py-2.5 rounded-xl max-w-3xl mx-auto mt-4 text-center">
            {{ error }}
        </div>

        <div v-if="loading" class="text-center mt-8 text-gray-600">
            Buscando...
        </div>

        <div v-if="tramite" class="mt-5 p-4 bg-slate-300 max-w-3xl mx-auto rounded-xl space-y-2">
            <div class="flex justify-between items-center">
                <h2 class="font-bold text-gray-700 text-lg">Datos del tramite</h2>
                <BadgeEstado :status="tramite.status" />  
            </div>
            <p><span class="font-semibold">Nombre:</span> {{ tramite.name }} {{ tramite.last_name }}</p>
            <p><span class="font-semibold">DNI:</span> {{ tramite.dni }}</p>
            <p><span class="font-semibold">Email:</span> {{ tramite.email }}</p>
            <p><span class="font-semibold">Teléfono:</span> {{ tramite.phone }}</p>
            <p><span class="font-semibold">Tipo:</span> {{ tramite.form_type === 'Register' ? 'Alta' : 'Baja' }}</p>
        </div>
    </div>
</template>