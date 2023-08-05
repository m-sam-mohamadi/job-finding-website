<script setup> 
import { useUserStore } from '@/stores/user'

let userStore = useUserStore()

function logout(){
    userStore.removeToken()
}
</script>

<template>
    <div>
        <nav class="p-6 flex items-center justify-between bg-rose-800">
            <nuxt-link to="/" class="text-xl text-white">samJob</nuxt-link>
            <div class="flex items-center space-x-4">
                <nuxt-link to="/" class="text-white hover:text-teal-300">Home</nuxt-link>
                <nuxt-link to="/browse" class="text-white hover:text-teal-300">Browse</nuxt-link>
            </div>
        </nav>
        <slot/>
        <footer class="p-6 fixed bottom-0 left-0 w-full flex flex-wrap items-center justify-between bg-gray-900">
            <p class="text-gray-300">copyright (c) M.SAM</p>
            <div class="flex mt-6 md:mt-0 items-center space-x-4">
               <template v-if="userStore.user.isAuthed">
                     <p class="text-white">{{ userStore.user.email }}</p> 
                <nuxt-link  to="/myjobs" class="py-4 px-6 bg-rose-900 hover:bg-rose-700 rounded-xl text-white">My jobs</nuxt-link>
                <nuxt-link  to="/createjob" class="py-4 px-6 bg-rose-600 hover:bg-rose-700 rounded-xl text-white">Create Jobs</nuxt-link>
                <a @click="logout()" class="py-4 px-6 bg-red-600 hover:bg-red-700 rounded-xl text-white">Logout</a>
                </template>  
                <div v-else>
                    <nuxt-link to="/login" class="py-4 px-6 bg-rose-900 my-6 hover:bg-rose-700 rounded-xl text-white">login</nuxt-link>
                <nuxt-link to="/signup" class="py-4 px-6 bg-rose-600 hover:bg-rose-700 my-10 rounded-xl text-white">signup</nuxt-link>
                </div>
            </div>
        </footer>
    </div>
</template>