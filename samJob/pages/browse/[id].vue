<script setup>
const route = useRoute()

const {data:job} = await useFetch('http://127.0.0.1:8000/api/v1/jobs/'+route.params.id+'/')
 
useSeoMeta({
    title:job.value.title,
    ogTitle:job.value.titles,
    description:job.value.description
})
</script>

<template>
    <div class="py-10 px-6 grid md:grid-cols-4 gap-3">
        <div class="md:col-span-3">
            <h1 class="mb-6 text-3xl">{{ job.title }}</h1>
            <p class="mb-10">
                {{ job.description }}
            </p>
            <a :href="'mailto:'+ job.companyEmail" class="inline-blocks py-4 px-6 bg-rose-700 rounded-xl text-white">Apply</a>
        </div>
        <div class="md:col-span-1 bg-rose-700 px-6 py-4 text-white rounded-xl">
            <div class="mb-6 text-2xl">Company</div>
            <p class="mb-2">{{ job.companyName }}</p>
            <p class="mb-2">{{ job.companyLocation }}</p>
            <hr class="my-6 opacity-30">

            <h3 class="mb-6 text-2xl"> Position</h3>
            <p class="mb-2">{{ job.positionLocation }}</p>
            <hr class="my-6 opacity-30">
            <p>Posted at {{ job.createdAtFormatted }}</p>
        </div>
    </div>
</template>