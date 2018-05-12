<template>
<div class="container">
      <div class="row">
         <div class="col-lg-12">
             <div class="form-group" >  
                 <!-- @keyup="getScrap()" -->
                <!-- <input type="hidden" name="_token" :value="csrf"> -->
                <label for="buscador" class="bmd-label-floating">Usuario</label>
                <input type="text" class="form-control" name="buscador" id="buscador" v-model="buscador" autocomplete="off">
            </div>
           <div class="form-group">
               <select class="form-control input-sm" v-model="pag" @change="getScrap()">
                 <option value="">Seleccione</option>
                 <option v-for="sel in seleccion" :value="sel.id">{{sel.nombre}}</option>
               </select>
           </div>
            <div class="form-group">
                <button class="btn btn-raised btn-primary" type="button" v-on:click.prevent="getScrap()">Buscar</button>
            </div> 
            <div class="form-group" v-show="loading">
              <!-- <i class="fa fa-spinner fa-spin" style="font-size:24px"></i> -->
              <i class="fas fa-spinner fa-spin" style="font-size:48px"></i> Cargando....
            </div> 
         </div>    
      </div>     
      <div class="row">
          <div class="col-lg-12">
                <div class="panel panel-success">
           <div class="panel-body div1 table-responsive">
            <table class="table table-bordered table-hover table-fixed table-striped" style="background:white;">
                 <thead>
                 <tr>
                     <th>#</th>
                     <th>Usuario</th>
                     <th>Link</th>
                     <th>Imagen</th>
                     <th>Info</th>
                 </tr>
                 </thead>
                <tbody>
                      <template v-if="lista!=''">
                  <tr v-for="(list,index) in lista">
                      <td>{{index+1}}</td>
                      <td>{{list.name}}</td>
                      <td><a  :href="list.link" target="_blank" >{{list.link}}</a></td>
                      <td><img :src="list.img"></td>  
                      <td><button class="btn btn-raised btn-primary" v-on:click.prevent="getInfo(list)">Info</button></td>   
                  </tr>   
                     </template>
                     <template v-else>
                      	<tr>
        	          <td colspan="5" align="center">No hay resultados disponibles</td>	
        	          </tr>
                     </template>   
                </tbody> 
            </table>
           </div>
        </div>
          </div> 
      </div>
      <div class="row" v-show="loading_info">
           <i class="fas fa-spinner fa-spin" style="font-size:48px"></i> Cargando info....
      </div><br>
      <div class="row" v-show="aparecer"> 
              <div class="col-lg-6">
               <p class="text-center">Perfil:</p>
              </div>
              <div class="col-lg-6">
                 <p>Id: {{info_all.id}}</p> 
                 <p>Bio: {{info_all.bio}}</p>
                 <p>Nombres: {{info_all.name}}</p>
                 <p><img :src="info_all.photo"></p>
                 <p>URL: <a :href="info_all.url" target="_blank">{{info_all.url}}</a></p>
              </div>
      </div>
</div>     
</template>
<script>
  
    export default{
        created(){
           //this.getScrap();
        },
        data(){ 
            return{
              lista:[],
              seleccion: [
 		            { id: '1' , nombre: '1' },
 		            { id: '2' , nombre: '2' },
 		            { id: '3' , nombre: '3' },
 		            { id: '4' , nombre: '4' },
 		            { id: '5' , nombre: '5' },
 		            { id: '6' , nombre: '6' },
 		            { id: '7' , nombre: '7' }
 		      ],
              pag:'',
              loading: false,
              loading_info: false,
              aparecer:false,
              info_all:[],
              buscador:''      
            }
        },
        methods:{
           getScrap(){
              let buscador=this.buscador;
              this.loading = true;
              let pag=this.pag;
                  if(buscador!=''){
                     axios.get('http://127.0.0.1:8000/search/getauto',{ 
                            params: { 
                                     buscador: buscador.trim(),
                                     pag:pag
                                    }
                        })
                        .then(response=>{   
                                this.lista=response.data.valor;
                                 this.loading = false;
                                console.log(response);
                        })
                        .catch(error=>{
                                console.log(error);
                        }) 
                  }else{
                      console.log("Dato no ingresado");
                  } 
           },
           getInfo(info){
               let url=info.link; 
               this.loading_info=true;
                this.aparecer=true;
               axios.get('http://127.0.0.1:8000/search/getdet',{ params: { url: url}})
               .then(response=>{
                 console.log(response.data.info_all);  
                this.info_all=response.data.info_all;
                this.loading_info=false;
              }).catch(error=>{
                  console.log(error);
              })  
           } 
        }
    }
</script>
<style scoped>

.table-bordered, .table-bordered>tbody>tr>td, .table-bordered>tbody>tr>th, .table-bordered>tfoot>tr>td, .table-bordered>tfoot>tr>th, .table-bordered>thead>tr>td, .table-bordered>thead>tr>th {
    border: 1px solid #afa8a8;
}

.div1{
     overflow-y:scroll;
     height:400px;
     width:100%;
     background: #ecf0f5;
}

.div1 table {
    width:100%;
}


thead {
    background: #379e61f0;
    color: white;
}
</style>