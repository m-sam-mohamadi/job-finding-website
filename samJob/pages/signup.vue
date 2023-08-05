<script setup>
import path from 'path';

let email = ref('')
let pass1 = ref('')
let pass2 = ref('')
let errors = ref([])
useSeoMeta({
    title:'signup',
    ogTitle:'signup',
    description:'signup description'  
})
async function submitForm() {
    errors.value = []

    await $fetch('http://127.0.0.1:8000/api/v1/users/', {
        method: 'POST',
        body: {
            username: email.value,
            password: pass1.value
        }
    }).then(res => {
        console.log(res);
        useRouter().push({ path: '/login' })
    }).catch(error => {
        if (error.response) {
            for (const prop in error.response._data) {
                errors.value.push(`${prop}:${error.response._data[prop]}`)
            }
        } else if (error.message) {
            errors.value.push('something went wrong. try again later')
            console.log(JSON.stringify(error));
        }
    })
}
</script>

<template>
    <div class="py-10 px-6">
        <div class="max-w-sm mx-auto py-10 px-6 bg-gray-100 rounded-xl">
            <h1 class="mb-6 text-2xl">Signup</h1>
            <form @submit.prevent="submitForm">
                <input v-model="email" type="email" name="em" placeholder="Your email..."
                    class="w-full py-4 px-6 mb-6 rounded-xl">
                <input v-model="pass1" type="password" name="pass" placeholder="Your Password..."
                    class="w-full py-4 px-6 mb-6 rounded-xl">
                <input v-model="pass2" type="password" name="repass" placeholder="Repeat Your Password..."
                    class="w-full mb-6 py-4 px-6 rounded-xl">
                <div class="mb-6 py-4 px-6 bg-rose-400 text-white rounded-xl" v-if="errors.length">
                    <p v-for="error in errors" :key="error.length">
                        {{ error }}
                    </p>
                </div>
                <button class="py-4 px-6 w-full bg-rose-700 text-white rounded-xl">Submit</button>
            </form>
        </div>
    </div>
</template>