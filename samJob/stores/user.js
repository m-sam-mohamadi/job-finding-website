import {defineStore} from 'pinia'

export const useUserStore = defineStore('user',{
    
    state:()=>({
        user:{
            isAuthed:false,
            email:null,
            token:null
        }
    }),

    actions:{
        initStore(){
            this.user.isAuthed = false
            if (localStorage.getItem('user.token')) {
                this.user.token = localStorage.getItem('user.token')
                this.user.email = localStorage.getItem('user.email')
                this.user.isAuthed = true
                console.log('init user',this.user);
            }
        },
        setToken(token,email){
            this.user.token = token
            this.user.email = email
            this.user.isAuthed = true
            localStorage.setItem('user.token',token)
            localStorage.setItem('user.email',email)
        },
        removeToken(){
            this.user.token = null
            this.user.email = null
            this.user.isAuthed = false

            localStorage.setItem('user.token','')
            localStorage.setItem('user.email','')
        }
    }
})