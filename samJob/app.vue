<script setup>
import {useUserStore} from '@/stores/user' 
const store = useUserStore()
onMounted(() => {
  store.initStore()
}) 
</script>

<template>
  <div class="mb-20">
    <NuxtLayout>
      <NuxtPage/>
    </NuxtLayout>
  </div>
</template>
