<template>
    <div class="container">
    <div class="row">
         <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
             <div class="form-group" >  
                <label for="buscador" class="bmd-label-floating">Usuario</label>
                <input type="text" class="form-control" name="buscador" id="buscador" v-model="buscador" autocomplete="off">
            </div>
            <div class="form-group">
                <button class="btn btn-raised btn-primary" type="button" v-on:click.prevent="getScrap_git()"><i class="fa fa-search"></i> Buscar</button>
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
                                    <td rowspan="2" class="estilo_wi_rows"><img :src="list.img_github"></td>
                                    <td class="nombre_info">{{list.nombre_github}}</td>
                               </tr>
                               <tr>
                                    <td class="nombre_link"><a :href="list.nick_github" target="_blank" >{{list.nick_github}}</a></td>
                              </tr>
                          </table>
                      </td>
                      <td align="center">
                <button v-on:click.prevent="getInfo(list)" class="btn  btn-info"><i class="fa fa-eye"></i> Vista previa</button>
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
    <div id="myModal3" class="modal fade" role="dialog">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal">&times;</button>
        <h4 class="modal-title">Información</h4>
      </div>
      <div class="modal-body">
          <table class="table table-bordered tablita table-responsive">
              <tbody>
                  <tr>
                            <td  colspan="3" align="center">
                      <center><img :src="data_info.img_github"></center>
                           </td>
                  </tr>
                  <tr>
                            <td class="info_style"><p class="text-center"><strong>País</strong></p></td>
                            <td class="info_style"><p class="text-center"><strong>Email</strong></p></td> 
                            <td class="info_style"><p class="text-center"><strong>Pagina web</strong></p></td>               
                  </tr>
                  <tr>
                            <td><p class="text-center"><strong>{{data_info.pais_github}}</strong></p></td>
                            <td><p class="text-center"><strong>{{data_info.email_github}}</strong></p></td> 
                            <td><p class="text-center"><strong>ddsd</strong></p></td> 
                  </tr>
                  <tr>
                            <td class="info_style" colspan="3"><p class="text-center"><strong>Biografía</strong></p></td>
                  </tr>
                  <tr>
                            <td colspan="3"><p class="text-center"><strong>{{data_info.biografia_github}}</strong></p></td>
                  </tr>
              </tbody>
          </table>
      
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
import swal from 'sweetalert';
    export default{
       created(){
       },
       data(){
          return{
           lista:[],
           loading: false,
           loading_info: false,
           aparecer:false,
           info_all:[],
           buscador:'',
           data_info:[]     
         }
       },
       methods:{
            mensaje(titulo,texto,icono){
             swal({
                 icon: icono,
                 title: titulo,
                 text: texto,
                 button: true,
                 timer: 1500
              })
           },
           getScrap_git(){
              let buscador=this.buscador;
              this.loading = true;
                   if(buscador!=''){
                     axios.get('http://127.0.0.1:8000/search/gethit',{ 
                            params: { 
                                     buscador: buscador.trim()
                                    }
                        })
                        .then(response=>{ 
                              console.log(response);
                                this.lista=response.data.info_all;
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
               this.data_info=info;
               console.log(info);
               $('#myModal3').modal('show');
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

td.info_style {
    background: #15202a;
    color: white;
}

thead {
    background: #2a3f54;
    color: white;
}
</style>