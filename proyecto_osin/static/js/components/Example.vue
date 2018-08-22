<template>
<div class="container">
      <div class="row">
         <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
             <div class="form-group" >  
                <label for="buscador" class="bmd-label-floating">Usuario</label>
                <input type="text" class="form-control" name="buscador" id="buscador" v-model="buscador" autocomplete="off">
            </div>
            <div class="form-group">
                <button class="btn btn-raised btn-primary" type="button" v-on:click.prevent="getScrap()"><i class="fa fa-search"></i> Buscar</button>
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
                                    <td rowspan="2" class="estilo_wi_rows"><img :src="list.img"></td>
                                    <td class="nombre_info">{{list.name}}</td>
                               </tr>
                               <tr>
                                    <td class="nombre_link"><a :href="list.link" target="_blank" >{{list.link}}</a></td>
                              </tr>
                          </table>
                      </td>
                      <td align="center">
                <button class="btn  btn-info" v-on:click.prevent="getInfo(list)"><i class="fa fa-eye"></i> Vista previa</button>
                     </td>  
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
      <div class="row" v-if="lista!=''">
          <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                       <paginate
                            :page-count="5"
                            :page-range="3"
                            :margin-pages="1"
                            :click-handler="clickCallback"
                            :prev-text="'Anterior'"
                            :next-text="'Siguiente'"
                            :container-class="'pagination'"
                            :page-class="'page-item'">
                        </paginate>
          </div>
       
      </div>
    <!-- Modal INFO-->
    <div id="myModal" class="modal fade" role="dialog">
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
           <form v-on:submit.prevent="getaddInfo()">
              <table class="table table-bordered tablita">
                  <tbody>
                        <tr>
                            <td rowspan="7" align="center">
                              <center><img :src="info_all.photo"></center>
                            </td>
                            <td><p>ID: {{info_all.id}}</p></td>
                        </tr>
                        <tr>
                            <td>
                               <template v-if="info_all.bio!=''"> 
                                <p>Biografía: {{info_all.bio}}</p>
                               </template>
                               <template v-else>
                                <p>Biografía: No tiene biografía</p>   
                               </template>
                            </td> 
                        </tr>
                         <tr>
                            <td><p>Nombres: {{info_all.name}}</p></td>
                        </tr>
                         <tr>
                            <td><p>URL: <a :href="info_all.url" target="_blank">{{info_all.url}}</a></p></td>
                        </tr>
                         <tr>
                            <td>
                               <template v-if="info_all.places!=''">   
                             <p v-for="item in info_all.places"> Ciudad Actual: {{item.ciudad_actual}}</p>
                                 </template>
                              <template v-else>
                            <p> Ciudad Actual: No existe</p>
                              </template>     
                            </td>
                        </tr>
                        <tr>
                             <td>
                            <template v-if="info_all.studies!=''"> 
                      <p v-for="(item,index)  in info_all.studies"> Formacion Academica {{index+1}}: {{item.formacion_academica}}</p>
                            </template>
                            <template v-else>
                      <p> Formacion Academica: No existe </p>   
                            </template>
                             
                             </td>
                        </tr>
                        <tr>
                             <td>
                                <template v-if="info_all.work!=''"> 
                                <p v-for="item in info_all.work"> Empleo: {{item.empleo}}</p>
                               </template>
                               <template v-else>
                                 <p> Empleo: No existe empleo</p>   
                               </template>
                            
                             </td>
                        </tr>
                        <tr>
                           <td class="info_style" colspan="2"><img src="/static/img/iconos/profile.png">Perfiles</td> 
                        </tr>
                        <tr>
                            <td><img src="/static/img/iconos/camera.png">Fotos</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/photos-by/'" >https://www.facebook.com/search/{{info_all.id}}/photos-by/</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/videos.png">Videos</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/videos-by/'" >https://www.facebook.com/search/{{info_all.id}}/videos-by/</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/post.png">Posts</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/stories-by/'" >https://www.facebook.com/search/{{info_all.id}}/stories-by/</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/groups.png">Grupos</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/groups/intersect'" >https://www.facebook.com/search/{{info_all.id}}/groups/intersect</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/events.png">Futuros eventos</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/events-joined'" >https://www.facebook.com/search/{{info_all.id}}/events-joined</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/events.png">Eventos pasados</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/events-joined/in-past/date/events/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/events-joined/in-past/date/events/intersect/</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/game.png">Juegos</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/apps-used/game/apps/intersect'" >https://www.facebook.com/search/{{info_all.id}}/apps-used/game/apps/intersect</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/apps.png">Apps</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/apps-used/'" >https://www.facebook.com/search/{{info_all.id}}/apps-used/</a></td>
                        </tr>
                         <tr>
                           <td class="info_style" colspan="2"><img src="/static/img/iconos/tags.png">Tags</td> 
                        </tr>
                          <tr>
                            <td><img src="/static/img/iconos/camera.png">Fotos</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/photos-of/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/photos-of/intersect/</a></td>
                        </tr>
                          <tr>
                            <td><img src="/static/img/iconos/videos.png">Videos</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/videos-of/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/videos-of/intersect/</a></td>
                        </tr>
                          <tr>
                            <td><img src="/static/img/iconos/post.png">Posts</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/stories-tagged/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/stories-tagged/intersect/</a></td>
                        </tr>
                         <tr>
                           <td class="info_style" colspan="2"><img src="/static/img/iconos/comments.png">Comentarios</td> 
                        </tr>
                          <tr>
                            <td><img src="/static/img/iconos/camera.png">Fotos</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/photos-commented/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/photos-commented/intersect/</a></td>
                        </tr>
                          <tr>
                            <td><img src="/static/img/iconos/videos.png">Videos</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/videos-commented/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/videos-commented/intersect/</a></td>
                        </tr>
                          <tr>
                            <td><img src="/static/img/iconos/post.png">Posts</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/stories-commented/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/stories-commented/intersect/</a></td>
                        </tr>
                         <tr>
                           <td class="info_style" colspan="2"><img src="/static/img/iconos/likes.png">Me gusta</td> 
                        </tr>
                        <tr>
                            <td><img src="/static/img/iconos/camera.png">Fotos</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/photos-liked/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/photos-liked/intersect/</a></td>
                        </tr>
                          <tr>
                            <td><img src="/static/img/iconos/videos.png">Videos</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/videos-liked/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/videos-liked/intersect/</a></td>
                        </tr>
                          <tr>
                            <td><img src="/static/img/iconos/post.png">Posts</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/stories-liked/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/stories-liked/intersect/</a></td>
                        </tr>
                           <tr>
                           <td class="info_style" colspan="2"><img src="/static/img/iconos/location.png">Lugares</td> 
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/everything.png">Todo</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/places-visited/'" >https://www.facebook.com/search/{{info_all.id}}/places-visited/</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/bars.png">Bares</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/places-visited/110290705711626/places/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/places-visited/110290705711626/places/intersect/</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/restaurants.png">Restaurantes</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/places-visited/273819889375819/places/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/places-visited/273819889375819/places/intersect/</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/stores.png">Tiendas</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/places-visited/200600219953504/places/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/places-visited/200600219953504/places/intersect/</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/outdoors.png">Parques</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/places-visited/935165616516865/places/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/places-visited/935165616516865/places/intersect/</a></td>
                        </tr>
                        <tr>
                            <td><img src="/static/img/iconos/hotels.png">Hoteles</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/places-visited/164243073639257/places/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/places-visited/164243073639257/places/intersect/</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/theaters.png">Cine</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/places-visited/192511100766680/places/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/places-visited/192511100766680/places/intersect/</a></td>
                        </tr>
                           <tr>
                           <td class="info_style" colspan="2"><img src="/static/img/iconos/surroundings.png">Personas</td> 
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/family.png">Familia</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/relatives/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/relatives/intersect/</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/friends.png">Amigos</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/friends/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/friends/intersect/</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/friendsoffriends.png">Amigos de amigos</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/friends/friends/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/friends/friends/intersect/</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/work.png">Compañeros de trabajo</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/employees/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/employees/intersect/</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/education.png">Compañeros de clase</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/schools-attended/ever-past/intersect/students/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/schools-attended/ever-past/intersect/students/intersect/</a></td>
                        </tr>
                         <tr>
                            <td><img src="/static/img/iconos/map.png">Locales</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/current-cities/residents-near/present/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/current-cities/residents-near/present/intersect/</a></td>
                        </tr>
                          <tr>
                           <td class="info_style" colspan="2"><img src="/static/img/iconos/intrests.png">Intereses</td> 
                        </tr>
                          <tr>
                            <td><img src="/static/img/iconos/everything.png">Paginas</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/pages-liked/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/pages-liked/intersect/</a></td>
                        </tr>
                          <tr>
                            <td><img src="/static/img/iconos/politics.png">Politica</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/pages-liked/161431733929266/pages/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/pages-liked/161431733929266/pages/intersect/</a></td>
                        </tr>
                          <tr>
                            <td><img src="/static/img/iconos/camera.png">Religion</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/pages-liked/religion/pages/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/pages-liked/religion/pages/intersect/</a></td>
                        </tr>
                          <tr>
                            <td><img src="/static/img/iconos/music.png">Musica</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/pages-liked/musician/pages/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/pages-liked/musician/pages/intersect/</a></td>
                        </tr>
                          <tr>
                            <td><img src="/static/img/iconos/movies.png">Pelicula</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/pages-liked/movie/pages/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/pages-liked/movie/pages/intersect/</a></td>
                        </tr>
                          <tr>
                            <td><img src="/static/img/iconos/book.png">Libros</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/pages-liked/book/pages/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/pages-liked/book/pages/intersect/</a></td>
                        </tr>
                          <tr>
                            <td><img src="/static/img/iconos/location.png">Lugares</td>
                            <td><a target="_blank" :href="'https://www.facebook.com/search/'+info_all.id+'/places-liked/intersect/'" >https://www.facebook.com/search/{{info_all.id}}/places-liked/intersect/</a></td>
                        </tr>
                  </tbody>
              </table>
              <div class="modal-footer">
             <button type="submit" class="btn btn-primary" id="enviofb">Guardar</button>      
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
import Paginate from 'vuejs-paginate';
var token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
var config = {
     headers: {'X-CSRFToken': token}
};
    export default{
        created(){
          
        },
        components: {
         'Paginate':Paginate
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
            mensaje(titulo,texto,icono){
             swal({
                 icon: icono,
                 title: titulo,
                 text: texto,
                 button: true,
                 timer: 1500
              })
            },
            clickCallback (pageNum){
                  this.pag=pageNum;
                  this.getScrap();
            },
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
                              console.log(response);
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
            disabl(valor){
               $("#enviofb").prop('disabled', valor);
            },
           getaddInfo(){
               var crf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
               var biografia=''
               if(this.info_all.bio!=''){
                  biografia=this.info_all.bio;
               }else{
                  biografia="No existe biografia";
               }
               var idfb=this.info_all.id;
               var name=this.info_all.name;
               var foto=this.info_all.photo;
               var url=this.info_all.url;
               
               var cadena_studies=[],cadena_lugares=[],cadena_trabajo=[], cstudies='', clugares='', ctrabajo='';
               if(this.info_all.studies!=''){
                   var studies=this.info_all.studies;
                     for(var i in studies){  
                        cadena_studies.push(studies[i].formacion_academica) 
                     }
                   cstudies=cadena_studies.toString();
               }else{
                   cstudies="No existe estudios";
               }

               if(this.info_all.places!=''){
                   var places=this.info_all.places;
                     for(var i in places){  
                        cadena_lugares.push(places[i].ciudad_actual) 
                     }
                   clugares=cadena_lugares.toString();
               }else{
                   clugares="No existe lugares";
               }

               if(this.info_all.work!=''){
                   var work=this.info_all.work;
                     for(var i in work){  
                        cadena_trabajo.push(work[i].empleo) 
                     }
                   ctrabajo=cadena_trabajo.toString();
               }else{
                   ctrabajo="No existe empleo";
               }
              
               var data={
                     idfb:idfb,
                     name: name,
                     biografia: biografia,
                     foto:foto,
                     url:url,
                     cstudies:cstudies,
                     clugares:clugares,
                     ctrabajo:ctrabajo
                     };
            var sel_thi=this;
            sel_thi.disabl(true);
            setTimeout(function(){sel_thi.disabl(false); }, 2000);         
            axios.post('http://127.0.0.1:8000/search/addfacebook',data,config)
                .then(response=>{
                         console.log(response);
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
           getInfo(info){
             $('#myModal').modal('show');
             let url=info.link; 
             this.loading_info=true;
              this.aparecer=false;
               axios.get('http://127.0.0.1:8000/search/getdet',{ params: { url: url}})
               .then(response=>{
               //  console.log(response.data.info_all);    
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

td.info_style {
    background: #15202a;
    color: white;
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