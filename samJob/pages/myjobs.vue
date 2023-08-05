<script setup>
import { useUserStore } from '@/stores/user'

let userStore = useUserStore()
let jobs = ref('')
onMounted(() => {
    if(!userStore.user.isAuthed){
        useRouter().push('/login')
    }else{
        getJobs()
    }
})
console.log('token'+userStore.user.token);
async function getJobs(){
    await $fetch('http://127.0.0.1:8000/api/v1/jobs/my/',{
        headers:{
            'Authorization':'token '+userStore.user.token,
            'Content-Type':'application/json'
        }
    }) .then((res) => {
        jobs.value = res
    }).catch((error) => {
        console.log(error);
    })
}

function deleteJob(id) {
    console.log(id);
    jobs.value = jobs.value.filter(job=>job.id!==id)
}

useSeoMeta({
    title:'My Jobs',
    ogTitle:'My Jobs',
    description:'jobs description'
})
</script>

<template>
    <div class="py-10 px-6">
        <h1 class="mb-6 text-2xl">my jobs</h1>
        <div class="space-y-4">
            <job :my="true" v-for="job in jobs" :key="job.id" :id="job.id" :salary="job.positionSalary" :title="job.title" :company-name="job.companyName" :created="job.createdAtFormatted"  v-on:deleteJob="deleteJob(job.id)"/> 
        </div>
    </div>
</template>