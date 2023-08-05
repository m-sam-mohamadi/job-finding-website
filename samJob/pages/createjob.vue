<script setup>
import { useUserStore } from '@/stores/user'

let userStore = useUserStore()
let jobs = ref('')
onMounted(() => {
    if(!userStore.user.isAuthed){
        useRouter().push('/login')
    } 
})
const {data:categ} = await useFetch('http://127.0.0.1:8000/api/v1/jobs/categories/')
let category = ref('')
let title = ref('')
let description = ref('')
let positionSalary = ref('')
let errors = ref([])
let companyName = ref('')
let companyEmail = ref('')
let companyLocation = ref('') 

async function submitForm() {
    errors.value = []
    if(category.value == '') errors.value.push('you must select category')
    if(title.value == '') errors.value.push('you must select title')
    if(description.value == '') errors.value.push('you must select description')
    if(positionSalary.value == '') errors.value.push('you must select positionSalary')
    if(companyName.value == '') errors.value.push('you must select companyName')
    if(companyEmail.value == '') errors.value.push('you must select companyEmail')
    if(companyLocation.value == '') errors.value.push('you must select companyLocation')
    if(errors.value.length==0){

    
    await $fetch('http://127.0.0.1:8000/api/v1/jobs/created/', {
        method: 'POST',
        headers:{
            'Authorization':'token '+userStore.user.token,
            'Content-Type':'application/json'
        },
        body: {
            category:category.value,
            title:title.value ,
            description:description.value,
            positionSalary:positionSalary.value,
            companyName:companyName.value,
            companyEmail:companyEmail.value,
            companyLocation:companyLocation.value,
        }
    }).then(res => {
        console.log(res);
        useRouter().push({ path: '/myjobs' })
    }).catch(error => {
        if (error.response) {
            for (const prop in error.response._data) {
                errors.value.push(`${prop}:${error.response._data[prop]}`)
            }
        } else if (error.message) {
            errors.value.push('something went wrong. try again later')
            console.log(JSON.stringify(error));
        }
    })}  
}


useSeoMeta({
    title:'create job',
    ogTitle:'create job',
    description:'create job description'
})
</script>
<template>
    <div class="py-10 px-6 mb-20">
        <h1 class="mb-6 text-2xl">Create Job</h1>
        <form @submit.prevent="submitForm" class="space-y-4">
            <div>
                <label name="cat">Category</label>
                <select name="cat" v-model="category" id="cat" class="w-full p-4 rounded-xl bg-gray-100">
                    <option value="">Select Category</option>
                    <option  v-for="cat in categ" :key="cat.id"  :value="cat.id">{{ cat.title }}</option> 
                </select> 
            </div>
            <div>
                <label for="title">Title</label>
                <input v-model="title" name="title" class="w-full p-4 rounded-xl bg-gray-100" type="text"> 
            </div>
            <div>
                <label for="desc">Description</label>
                <input v-model="description"  name="desc"  class="w-full p-4 rounded-xl bg-gray-100" type="text"> 
            </div>
            <div>
                <label for="sal">Salary</label>
                <input v-model="positionSalary"  name="sal"  class="w-full p-4 rounded-xl bg-gray-100" type="text"> 
            </div>
            <div>
                <label for="comp">Company Name</label>
                <input v-model="companyName"  name="comp" class="w-full p-4 rounded-xl bg-gray-100" type="text"> 
            </div>
            <div>
                <label for="Loc">Company Location</label>
                <input  v-model="companyLocation "  name="comp" class="w-full p-4 rounded-xl bg-gray-100" type="text"> 
            </div>
            <div>
                <label for="em">Company Email</label>
                <input v-model="companyEmail"  name="em" class="w-full p-4 rounded-xl bg-gray-100" type="text"> 
            </div>
            <div class="mb-6 py-4 px-6 bg-rose-400 text-white rounded-xl" v-if="errors.length">
                    <p v-for="error in errors" :key="error.length">
                        {{ error }}
                    </p>
                </div>
            <button class="py-4 px-6  bg-rose-700 text-white rounded-xl" type="submit">Submit</button>

        </form>
    </div>
</template>