"use strict";(self["webpackChunkuchim_vue"]=self["webpackChunkuchim_vue"]||[]).push([[661],{1661:function(e,t,o){o.r(t),o.d(t,{default:function(){return h}});var n=o(3396),s=o(9242),a=o(7139);function r(e,t,o,r,i,u){return(0,n.wg)(),(0,n.iD)("div",null,[(0,n.wy)((0,n._)("input",{"onUpdate:modelValue":t[0]||(t[0]=e=>i.email=e),type:"email"},null,512),[[s.nr,i.email]]),(0,n.wy)((0,n._)("input",{"onUpdate:modelValue":t[1]||(t[1]=e=>i.password=e),type:"password"},null,512),[[s.nr,i.password]]),(0,n._)("button",{onClick:t[2]||(t[2]=e=>u.login())},"Войти"),(0,n.Uk)(" "+(0,a.zw)(i.errors),1)])}o(7658);var i=o(4161),u={name:"LogIn",data(){return{email:"",password:"",errors:[]}},mounted(){document.title="Авторизация"},methods:{async login(){i.Z.defaults.headers.common["Authorization"]="",localStorage.removeItem("token");const e={email:this.email,password:this.password};await i.Z.post("auth/token/login/",e).then((e=>{const t=e.data.auth_token;this.$store.commit("setToken",t),i.Z.defaults.headers.common["Authorization"]="Token "+t,localStorage.setItem("token",t),this.$router.push("/")})).catch((e=>{if(e.response)for(const t in e.response.data)this.errors.push(`${t}: ${e.response.data[t]}`);else this.errors.push("Something went wrong. Please try again"),console.log(JSON.stringify(e))}))}}},l=o(89);const d=(0,l.Z)(u,[["render",r]]);var h=d}}]);
//# sourceMappingURL=661.fab27632.js.map