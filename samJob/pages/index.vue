<script setup>
const {data:jobs} = await useFetch('http://127.0.0.1:8000/api/v1/jobs/newest/')
 
useSeoMeta({
    title:'find job',
    ogTitle:'find job',
    description:'find job description'  
})
</script>


<template>
    <div class=" mb-20">
      <div class="py-20 px-6 bg-rose-700 text-center">
        <h1 class="mb-12 text-5xl text-white">find job</h1>
        <nuxt-link to="/browse" class="inline-block py-4 px-8 bg-rose-900 text-white rounded-xl">Browse</nuxt-link>
      </div>
      <div class="py-10 px-6 ">
        <h2 class="mb-8 text-2xl text-center">
            newest jobs
        </h2>
        <div class="space-y-4"> 
            <job v-for="i in jobs" :key="i.id" :company-name="i.title" :created="i.createdAtFormatted" :salary="i.positionSalary" :id="i.id"/> 
        </div>
      </div>
    </div>
</template>