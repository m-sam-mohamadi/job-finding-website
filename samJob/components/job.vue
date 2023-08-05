<script setup>
import {useUserStore} from '@/stores/user'
const userStore = useUserStore()
const emit = defineEmits(['deleteJob'])

const props = defineProps({
    my: {
        type: [Boolean]
    },
    companyName:{
        type:String
    },
    salary:{
        type:String
    },
    created:{
        type:String
    },
    id:{
        type:Number
    }
})

async function deleteJob(id){

    await $fetch('http://127.0.0.1:8000/api/v1/jobs/'+id+'/delete/', {
        method: 'DELETE',
        headers:{
            'Authorization':'token '+userStore.user.token,
            'Content-Type':'application/json'
        }}).then((res) => {
            console.log(res);
            emit('deleteJob',id)
        }).catch((err) => {
            console.log(err);
        })



}

console.log('job id:'+props.id);
</script>


<template>
    <div class="space-y-4">
        <div class="p-6 flex items-center justify-between bg-gray-100 rounded-xl">
            <div>
                <h3 class="mb-2 text-xl font-semibold "> job position</h3>
                <p class="text-gray-600">{{ companyName }}</p>
            </div>
            <div>
                <p class="mb-2">world wide</p>
                <p>{{ salary }}</p>
            </div>
            <div>
                <p>posted at {{ created }}</p>
            </div>
            <div>

                <nuxt-link :to="`/browse/${id}`" class="py-4 px-6 bg-rose-700 text-white rounded-xl">Details</nuxt-link>
                <nuxt-link v-if="my"  :to="`/editjob/${id}`" class="py-4 px-6 mx-6 bg-blue-700 text-white rounded-xl">Edit</nuxt-link>
                <a @click="deleteJob(id)" v-if="my"  class="py-4 px-6 bg-red-700 text-white rounded-xl">Delete</a>
            </div>
        </div>
    </div>
</template>