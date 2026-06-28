<script setup>
// Vista del formulario de solicitud de alta/baja
import { ref } from 'vue'
import { createForm, uploadFile } from '../services/formServices'


const form = ref({
    name: '',
    last_name: '',
    dni: '',
    phone: '',
    email: '',
    form_type: 'Register',
    dniImage: '',
    taxImage: ''
})

const error = ref('')
const success = ref(false)
const formKey = ref(0)

async function handleSubmit() {
  error.value = ''
  success.value = false
  try {
    await createForm({...form.value})
    success.value = true
    form.value = {
      name: '',
      last_name: '',
      dni: '',
      phone: '',
      email: '',
      form_type: 'Register',
      dniImage: '',
      taxImage: ''
    }
    formKey.value++
  } catch (err) {
    if (err.response?.status === 409) {
      error.value = 'Ya tenes un formulario pendiente'
    } else if (err.response?.status === 400) {
      error.value = 'Formato incorrecto'
    } else if (err.response?.status === 404) {
      error.value = 'Ese cliente no existe'
    } else {
      error.value = 'Error al enviar el formulario'
    }
  }
}

async function handleFile(event, field) {
  const file = event.target.files[0]
  if (!file) return

  const allowedExtensions = ['image/jpeg', 'image/png']
  if (!allowedExtensions.includes(file.type)) {
    error.value = 'Formato de archivo no permitido'
    event.target.value = ''
    form.value[field] = ''
    return
  }

  error.value = ''
  try {
    const response = await uploadFile(file)
    form.value[field] = response.data
  } catch (err) {
    error.value = 'Error al subir el archivo'
    event.target.value = ''
    form.value[field] = ''
  }
}

</script>

<template>
    <div class="p-3">
        <form :key="formKey" @submit.prevent="handleSubmit">
          <div class="mt-5 p-4 bg-slate-300 max-w-3xl mx-auto rounded-xl">
            <label class="font-bold text-gray-600 text-xs leading-8 uppercase h-6 mx-2 mt-3">Tipo de formulario</label>
            <select v-model="form.form_type" class="w-full border-2 border-gray-200 rounded-xl px-3 py-3 text-base focus:outline-none focus:border-slate-400 disabled:opacity-50 bg-white transition-colors">
              <option value="Register">Alta</option>
              <option value="Unregister">Baja</option>
            </select>
          </div>

          <div class="mt-5 p-4 bg-slate-300 max-w-3xl mx-auto rounded-xl">
            <div>
              <label class="font-bold text-gray-600 text-xs leading-8 uppercase h-6 mx-2 mt-3">First Name</label>
              <div class="w-180 flex-1 mx-2">
                  <div class="bg-white my-2 p-1 flex border border-gray-200 w-full rounded-xl">
                      <input type="text" required minlength="3" maxlength="255" v-model="form.name" placeholder="First Name" class="p-1 px-2 appearance-none outline-none w-full text-gray-800">
                  </div>
              </div>
              <label class="font-bold text-gray-600 text-xs leading-8 uppercase h-6 mx-2 mt-3">Last Name</label>
              <div class="w-180 flex-1 mx-2">
                  <div class="bg-white my-2 p-1 flex border border-gray-200 rounded-xl">
                      <input type="text" required minlength="3" maxlength="255" v-model="form.last_name" placeholder="Last Name" class="p-1 px-2 appearance-none outline-none w-full text-gray-800">
                  </div>
              </div>
              <div class="w-180 mx-2 flex-1">
                  <label class="font-bold h-6 mt-3 text-gray-600 text-xs leading-8 uppercase"> DNI</label>
                  <div class="bg-white my-2 p-1 flex border border-gray-200 rounded-xl">
                      <input type="text" required minlength="8" maxlength="8" v-model="form.dni" placeholder="xx.xxx.xxx" class="p-1 px-2 appearance-none outline-none w-full text-gray-800">
                  </div>
              </div>
              <div class="w-180 mx-2 flex-1">
                  <label class="font-bold h-6 mt-3 text-gray-600 text-xs leading-8 uppercase"> Phone</label>
                  <div class="bg-white my-2 p-1 flex border border-gray-200 rounded-xl">
                      <input type="tel" required maxlength="12" @input="form.phone = form.phone.replace(/\D/g, '')" v-model="form.phone" placeholder="1122334455" class="p-1 px-2 appearance-none outline-none w-full text-gray-800">
                  </div>
              </div>
              <div class="w-180 mx-2 flex-1">
                  <label class="font-bold h-6 mt-3 text-gray-600 text-xs leading-8 uppercase"> Email</label>
                  <div class="bg-white my-2 p-1 flex border border-gray-200 rounded-xl">
                    <input type="email" required v-model="form.email" placeholder="jhon@doe.com" class="p-1 px-2 appearance-none outline-none w-full text-gray-800">
                  </div>
              </div>
              <div class="w-180 mx-2 flex-1">
                  <label class="font-bold h-6 mt-3 text-gray-600 text-xs leading-8 uppercase"> DNI Image</label>
                  <div class="bg-white my-2 p-1 flex border border-gray-200 rounded-xl">
                    <input type="file" accept="image/jpeg, image/png" required @change="e => handleFile(e, 'dniImage')" class="p-1 px-2 outline-none w-full text-gray-800">
                  </div>
              </div>
              <div class="w-180 mx-2 flex-1">
                  <label class="font-bold h-6 mt-3 text-gray-600 text-xs leading-8 uppercase"> Tax Image</label>
                  <div class="bg-white my-2 p-1 flex border border-gray-200 rounded-xl">
                    <input type="file" accept="image/jpeg, image/png" required @change="e => handleFile(e, 'taxImage')" class="p-1 px-2 outline-none w-full text-gray-800">
                  </div>
              </div>

              <div v-if="error" class="bg-red-50 border border-red-200 text-red-700 text-lg font-medium px-3 py-2.5 rounded-xl w-80 text-center mx-auto mt-8">
                {{ error }}
              </div>

              <div class="pt-8 pb-2 w-180 mx-2 flex ">
                <button type="submit" class="bg-slate-400 px-3 py-1.5 rounded-lg text-base font-medium text-slate-800 hover:bg-slate-500 transition-colors ml-auto w-30 ">
                  Enviar
                </button>
              </div>

              <div v-if="success" class="bg-green-50 border border-green-200 text-green-700 text-lg font-medium px-3 py-2.5 rounded-xl w-80 text-center mx-auto mt-8">
                ¡Formulario enviado correctamente!
              </div>

            </div>
          </div>
        </form>
      </div>
</template>