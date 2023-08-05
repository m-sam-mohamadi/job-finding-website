<script setup>
import path from 'path';
import {useUserStore} from '@/stores/user'

const store = useUserStore()
let email = ref('')
let pass1 = ref('') 
let errors = ref([ ])
useSeoMeta({
    title:'login',
    ogTitle:'login',
    description:'login description'  
})
async function submitForm(){
    errors.value = []

    await $fetch('http://127.0.0.1:8000/api/v1/token/login/',{
        method:'POST',
        body:{
            username:email.value,
            password:pass1.value
        }
    }).then(res=>{
        console.log(res);
        store.setToken(res.auth_token,email.value  )
        useRouter().push({path:'/'})
    }).catch(error=>{
        if (error.response) {
            for (const prop in error.response._data){
            errors.value.push(`${prop}:${error.response._data[prop]}`)
            }
        }else if(error.message){
            errors.value.push('something went wrong. try again later')
            console.log(JSON.stringify(error));
        }
    })
}
</script>

<template>
    <div class="py-10 px-6">
        <div class="max-w-sm mx-auto py-10 px-6 bg-gray-100 rounded-xl">
            <h1 class="mb-6 text-2xl">Login</h1>
            <form @submit.prevent="submitForm">
                <input v-model="email" type="email" name="em" placeholder="Your email..." class="w-full py-4 px-6 mb-6 rounded-xl"  >
                <input v-model="pass1" type="password" name="pass" placeholder="Your Password..." class="w-full py-4 px-6 mb-6 rounded-xl" >
                 <div class="mb-6 py-4 px-6 bg-rose-400 text-white rounded-xl"
                v-if="errors.length"
                >
                <p 
                v-for="error in errors" 
                :key="error.length">
            {{ error }}
            </p>
                </div>
                <button class="py-4 px-6 w-full bg-rose-700 text-white rounded-xl">Submit</button>
            </form>
        </div>
    </div>
</template>