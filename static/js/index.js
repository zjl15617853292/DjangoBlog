
var vm = new Vue({
    el:'#app',
    delimiters: ['[[', ']]'],
    data:{
        host,
        show_menu:false,
        is_login:true,
        username:''
    },
    mounted(){
        this.username = getCookie('username')
        this.is_login = getCookie('is_login');
    },

})

