<script setup>
// Componente raíz, renderiza las vistas según la ruta


</script>

<template>
    <div class="min-h-svh flex flex-col">
      <nav class="bg-gray-400 sticky top-0 z-40 shadow-md">
        <div class="max-w-8xl mx-auto px-25 h-20 flex items-center justify-between">
          <p class="text-slate-800 text-[36px] font-bold text-base tracking-tigth">
            Formularios ISP
          </p>

          <div class="flex items-center gap-2">
            <RouterLink to="/" class="px-3 py-1.5 rounded-lg text-base font-medium text-slate-800 hover:bg-slate-300 transition-colors">
              Crear Formulario
            </RouterLink>
            <p>
              |
            </p>
            <RouterLink to="/check" class="px-3 py-1.5 rounded-lg text-base font-medium text-slate-800 hover:bg-slate-300 transition-colors">
              Consultar Estado
            </RouterLink>
          </div>
        </div>
      </nav>

      <div class="p-3">
        <RouterView />
      </div>
    </div>
</template>

<style scoped></style>
