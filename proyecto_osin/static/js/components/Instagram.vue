<template>
    <div class="container">
    <div class="row">
         <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
             <div class="form-group" >  
                <label for="buscador" class="bmd-label-floating">Usuario</label>
                <input type="text" class="form-control" name="buscador" id="buscador" v-model="buscador" autocomplete="off">
            </div>
            <div class="form-group">
                <button class="btn btn-raised btn-primary" type="button" v-on:click.prevent="getScrap_insta()"><i class="fa fa-search"></i> Buscar</button>
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
                 </tr>
                 </thead>
                <tbody>
                       <template v-if="lista!=''">
                  <tr v-for="(list,index) in lista">
                      <td>{{index+1}}</td>
                      <td>
                          <table class="table table-bordered">
                               <tr>
                                    <td rowspan="2" class="estilo_wi_rows"><img width="73" height="73" :src="list.logo_inta"></td>
                                    <td class="nombre_info">{{list.name_inta}}</td>
                               </tr>
                               <tr>
                                    <td class="nombre_link"><a :href="list.nick_inta" target="_blank" >{{list.nick_inta}}</a></td>
                              </tr>
                          </table>
                      </td>
                      <td align="center">
                <button class="btn btn-info" v-on:click.prevent="getInfoInst(list)"><i class="fa fa-eye"></i> Vista previa</button>
                     </td>  

                     </tr>   
                     </template>
                     <template v-else>
                      	<tr>
        	          <td colspan="3" align="center">No hay resultados disponibles</td>	
        	          </tr>
                     </template>   
                </tbody>
            </table> 
        </div>
                </div>
          </div> 
        </div>  
        <br>
         <div class="row well titulo_busqueda">
        <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
            <p class="text-center" ># HASTAGS</p> 
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
                     <th>Tendencia Hastags</th>
                 </tr>
                 </thead>
                <tbody>
                       <template v-if="info_post!=''">
                  <tr v-for="(listax,index) in info_post">
                      <td>{{index+1}}</td>
                      <td>
                          <table class="table table-bordered">
                               <tr>
                                    <td rowspan="2" class="estilo_wi_rows"><img width="73" height="73" :src="listax.logo_inta"></td>
                                    <td class="nombre_info">{{listax.name_inta}}</td>
                               </tr>
                               <tr>
                                    <td class="nombre_link"><a :href="listax.nick_inta" target="_blank" >{{listax.nick_inta}}</a></td>
                              </tr>
                          </table>
                      </td>
                     </tr>   
                     </template>
                     <template v-else>
                      	<tr>
        	          <td colspan="2" align="center">No hay resultados disponibles</td>	
        	          </tr>
                     </template>   
                </tbody>
            </table> 
        </div>
                </div>
          </div> 
        </div>    
    

           <!-- Modal INFO-->
    <div id="myModalint" class="modal fade" role="dialog">
  <div class="modal-dialog modal-lg">
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
           <form v-on:submit.prevent="getaddInfoinst()">
              <table class="table table-bordered tablita">
                  <tbody>
                   <tr>
                      <td rowspan="4"><center><img :src="data_info.logo_inta"></center></td>
                      <td class="info_style centro">Nombre:</td>
                      <td class="info_style centro">Usuario</td>
                      <td class="info_style centro">URL:</td>
                   </tr>
                   <tr>
                      <td class="centro">{{data_info.name_inta}}</td>
                      <td class="centro">{{data_info.user_inta}}</td>
                      <td class="centro"><a :href="data_info.nick_inta" target="_blank" >{{data_info.nick_inta}}</a></td>
                   </tr>
                   <tr>
                      <td class="info_style centro">Seguidores:</td>
                      <td class="info_style centro">Posts:</td>
                      <td class="info_style centro">Siguiendo:</td>
                   </tr>
                   <tr>
                      <td class="centro" v-if="detalle_info.followers">{{detalle_info.followers}}</td>
                      <td class="centro" v-if="detalle_info.post">{{detalle_info.post}}</td>
                      <td class="centro" v-if="detalle_info.followins">{{detalle_info.followins}}</td>
                   </tr>
                   <tr>
                       <td colspan="4" v-if="detalle_info.followers==undefined" class="text-danger centro">* Si no cargo la data vuelva a cargar porfavor..</td>   
                   </tr>
            
                  </tbody>
              </table>
              <div class="modal-footer">
             <button type="submit" class="btn btn-primary" id="envioinst">Guardar</button>      
             <button type="button" class="btn btn-default" data-dismiss="modal">Cerrar</button>
             </div>
           </form> 
        </div>
      </div>
      
    </div>

  </div>
</div>

    </div>  
</template>
<script>
import swal from 'sweetalert';
var tokent = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
var config = {
     headers: {'X-CSRFToken': tokent}
};
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
           info_post:[],
           git_web:'',
           buscador:'',
           data_info:[],
           detalle_info:{
               post:'',
               followers:'',
               followins:''
           }     
         }
       },
       methods:{
            disabl(valor){
               $("#envioinst").prop('disabled', valor);
            },
            mensaje(titulo,texto,icono){
             swal({
                 icon: icono,
                 title: titulo,
                 text: texto,
                 button: true,
                 timer: 1500
              })
           },
           getInfoInst(list){
                $('#myModalint').modal('show');
               this.data_info=list; 
               this.loading_info = true;
               this.aparecer=false;
               var username_instahram=list.user_inta;
               console.log(username_instahram);
               axios.get('http://127.0.0.1:8000/search/getinstadet',{ 
                            params: { 
                                     username_instahram: username_instahram.trim()
                                    }
                        })
                        .then(response=>{
                              console.log(response);
                              var post=response.data.info[0];
                              var followers=response.data.info[1];
                              var followins=response.data.info[2];
                              this.detalle_info.post=post;
                              this.detalle_info.followers=followers;
                              this.detalle_info.followins=followins;
                              this.loading_info = false;
                              this.aparecer=true;
                        })
                        .catch(error=>{
                                console.log(error);
                        })
              
               
                  
           },
           getaddInfoinst(){
            var foto_instagram=this.data_info.logo_inta;
            var nombre_instagram=this.data_info.name_inta;
            var usuario_instagram=this.data_info.user_inta;
            var url_instagram=this.data_info.nick_inta;
            //esto viene de otro array
            var seguidores_instagram=this.detalle_info.followers;
            var post_instagram=this.detalle_info.post;
            var siguiendo_instagram=this.detalle_info.followins;

            var data={
                     foto_instagram:foto_instagram,
                     nombre_instagram: nombre_instagram,
                     url_instagram:url_instagram,
                     usuario_instagram: usuario_instagram,
                     seguidores_instagram:seguidores_instagram,
                     post_instagram:post_instagram,
                     siguiendo_instagram:siguiendo_instagram,
                     };           
            var sel_thi=this;
            sel_thi.disabl(true);
            setTimeout(function(){sel_thi.disabl(false); }, 2000);  
            axios.post('http://127.0.0.1:8000/search/addainstagram',data,config)
                .then(response=>{
                          if(response.data.success){
                           this.mensaje(response.data.success,'','success');
                          }else if(response.data.fail){
                           this.mensaje(response.data.fail,'','error');
                          } 
                     })
                .catch(error=>{
                     if(error.response.status==500){
                          this.mensaje('Ya existe este registro','','error');
                          console.clear();
                     }
                
                })
           },
           getScrap_insta(){
              let buscador=this.buscador;
              this.loading = true;
                   if(buscador!=''){
                     axios.get('http://127.0.0.1:8000/search/getinsta',{ 
                            params: { 
                                     buscador: buscador.trim()
                                    }
                        })
                        .then(response=>{ 
                                this.lista=response.data.info_users;
                                this.info_post=response.data.info_post;
                                this.loading = false;
                               
                        })
                        .catch(error=>{
                                console.log(error);
                        }) 
                  }else{
                      console.log("Dato no ingresado");
                  } 
           }
       } 
    }
</script>
<style scoped>

.centro{
  text-align:center;
}

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