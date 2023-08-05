<script setup>
let queryRef = ref('')
let query = ''

function searching(){
    queryRef.value = query
}
const {data:categ} = await useFetch('http://127.0.0.1:8000/api/v1/jobs/categories/')

let selectedCategoryRef= ref('')
let selectedCat = []

function toggleCat(id){
    const index = selectedCat.indexOf(id)
    if (index == -1) {
        selectedCat.push(id)
    }else{
        selectedCat.splice(index,1)

    }
    selectedCategoryRef.value = selectedCat.join(',')
}

let {data:jobs} = await useFetch('http://127.0.0.1:8000/api/v1/jobs',{
    query:{
        query:queryRef,
        categories:selectedCategoryRef
    }
})
</script>

<template>
    <div class="grid md:grid-cols-4 gap-3 py-10 px-6">
        <div class="md:col-span-1 px-6 py-6 bg-rose-700 rounded-xl">
            <div class="flex space-x-4">
                <input v-model="query" type="search" placeholder="find a job..." class="w-full px-6 py-4 rounded-xl">
                <button @click="searching()" class="px-6 bg-rose-900 text-white rounded-xl">Search</button>
            </div>
            <hr class="my-6 opacity-30">
            <h3 class="mt-6 text-xl text-white">Categories</h3>
            <div class="mt-6 space-y-4">
                <p class="py-4 px-6 text-white rounded-xl"   v-for="cat in categ" :key="cat.id" @click="toggleCat(cat.id)" :class="{'bg-rose-900':selectedCategoryRef.includes(cat.id)}">{{ cat.title }}</p>
            </div>
        </div>
        <div class="md:col-span-3">
            <div class="space-y-4">

                <job v-for="i in jobs" :key="i.id" :company-name="i.title" :created="i.createdAtFormatted" :salary="i.positionSalary" :id="i.id"/> 

            </div>
        </div>
    </div>
</template>