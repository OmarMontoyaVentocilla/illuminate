<template>
<div class="container">
      <div class="row">
         <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
             <div class="form-group" >  
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
              <i class="fa fa-spinner fa-spin" style="font-size:48px"></i> Cargando....
            </div> 
         </div>    
      </div>     
      <div class="row">
          <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                <div class="panel panel-success panel_estilo">
           <div class="panel-body div1 table-responsive">
            <table class="table table-bordered table-hover table-fixed table-striped" style="background:white;">
                 <thead>
                 <tr>
                     <th>#</th>
                     <th>Datos</th>
                     <th>Info</th>
                     <th>Asignar</th>
                 </tr>
                 </thead>
                <tbody>
                      <template v-if="lista!=''">
                  <tr v-for="(list,index) in lista">
                      <td>{{index+1}}</td>
                      <td>
                          <table class="table table-bordered">
                               <tr>
                                    <td rowspan="2" class="estilo_wi_rows"><img :src="list.img"></td>
                                    <td class="nombre_info">{{list.name}}</td>
                               </tr>
                               <tr>
                                    <td class="nombre_link"><a :href="list.link" target="_blank" >{{list.link}}</a></td>
                              </tr>
                          </table>
                      </td>
                      <td align="center">
                <button class="btn btn-raised btn-primary" v-on:click.prevent="getInfo(list)">Ver</button>
                     </td>  
                     <td align="center"><input type="checkbox" name=""></td> 
                     </tr>   
                     </template>
                     <template v-else>
                      	<tr>
        	          <td colspan="4" align="center">No hay resultados disponibles</td>	
        	          </tr>
                     </template>   
                </tbody> 
            </table>
           </div>
        </div>
          </div> 
      </div>

    <!-- Modal INFO-->
    <div id="myModal" class="modal fade" role="dialog">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">Información</h4>
      </div>
      <div class="modal-body">
        <div v-show="loading_info">
           <i class="fa fa-spinner fa-spin" style="font-size:48px"></i> Cargando info....
        </div>
        <div class="row" v-show="aparecer"> 
              <table class="table table-bordered tablita">
                  <tbody>
                        <tr>
                            <td rowspan="5" align="center">
                              <center><img :src="info_all.photo"></center>
                                </td>
                            <td><p>Id: {{info_all.id}}</p></td>
                        </tr>
                        <tr>
                            <td><p>Biografía: {{info_all.bio}}</p></td> 
                        </tr>
                         <tr>
                            <td><p>Nombres: {{info_all.name}}</p></td>
                        </tr>
                         <tr>
                            <td><p>URL: <a :href="info_all.url" target="_blank">{{info_all.url}}</a></p></td>
                        </tr>
                         <tr>
                            <td>
                               <p>{{ciudad}}</p>
                            </td>
                        </tr>
                  </tbody>
              </table>
        </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Cerrar</button>
      </div>
    </div>

  </div>
</div>

</div>     
</template>
<script>
  
    export default{
        created(){
          
        },
        data(){ 
            return{
              lista:[],
              ciudad:'',
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
                               
                        })
                        .catch(error=>{
                                console.log(error);
                        }) 
                  }else{
                      console.log("Dato no ingresado");
                  } 
           },
           getInfo(info){
             $('#myModal').modal('show');
             let url=info.link; 
             this.loading_info=true;
              this.aparecer=false;
               axios.get('http://127.0.0.1:8000/search/getdet',{ params: { url: url}})
               .then(response=>{
                 console.log(response.data.info_all);    
                 console.log(response.data.info_all.places);  
                this.info_all=response.data.info_all;
                
                this.loading_info=false;
                this.aparecer=true;
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

.panel.panel-success.panel_estilo {
    border: 1px solid #2a3f54;
    -webkit-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
    -moz-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
     box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
    width: 80%;
    margin: auto;
}

table.table.table-bordered.tablita {
    box-shadow: 0px 2px 8px 3px rgba(0,0,0,0.75);
}

td.estilo_wi_rows {
    width: 124px;
}

td.nombre_info {
    color: black;
    font-size: 15px;
}

td.nombre_link a {
    color: #2a3f54;
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
    background: #2a3f54;
    color: white;
}
</style>