<template>
<div class="container">
      <div class="row">
         <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
              <div class="form-group" >  
                <label for="buscador" class="bmd-label-floating">Hastag</label>
                <input type="text" class="form-control" name="buscador" id="buscador" v-model="buscador"  autocomplete="off">
             </div>
              <div class="form-group">
                <button class="btn btn-raised btn-primary" type="button" v-on:click.prevent="gethas()"><i class="fa fa-search"></i> Buscar</button>
            </div> 
         </div>
       </div>
       <div class="row">
           <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
              <div v-html="saludo"></div>
           </div>            
       </div>
</div>
</template>
<script>
 export default{
     created(){
        this.gethas();
     },
     data(){
         return{
           'saludo':'',
           'buscador':''
         }
     },
     methods:{
      gethas(){
          var buscador=this.buscador;
          if(buscador!=''){
          var src="https://www.hashatit.com/hashtags/"+buscador+"/all/embed";   
          var url_as='<iframe src="'+src+'" width="100%" height="1200"></iframe>';
          this.saludo=url_as;
          }else{
           this.saludo='';  
          }
          return this.saludo;  
      }
     }
     
 }
</script>
<style>
.popupWrap>p>a>img{
    display:none;
}
</style>