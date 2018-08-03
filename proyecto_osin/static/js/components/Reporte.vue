<template>
<div class="container">
     <div class="row">
          <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
         <div class="form-group">
                 <label for="persona">Persona</label>
                <select class="form-control input-sm" v-model="combo" @change="getDataAll()">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options" :value="sel.id">{{sel.nombre}}</option>
               </select>
                
        </div>
          </div>
          <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
                    
          </div>
     </div>
      <div class="row">
         <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
             <div class="panel panel-success panel_estilo">
           <div class="panel-body div1 table-responsive">
            <table class="table table-bordered table-hover table-fixed table-striped" style="background:white;">
             <thead>
                 <tr>
                     <th>#</th>
                     <th>Apodo</th>
                     <th>Facebook</th>
                     <th>Twitter</th>
                     <th>Github</th>
                     <th>Google</th>
                     <th>Instagram</th>
                     <th>Acción</th>
                 </tr>
            </thead>
            <tbody>
                 <template v-if="lista!=''">
                <tr v-for="(list,index) in lista">
                     <td>{{index+1}}</td>
                     <td>{{list.apodo_persona}}</td>
                     <td><img crossOrigin="Anonymous" v-bind:id="'facebook_d'+list.id" :src="list.foto_fb" width="100" height="100"></td>
                     <td><img crossOrigin="Anonymous" v-bind:id="'twitter_d'+list.id" :src="list.img_tw" width="100" height="100"></td>
                     <td><img crossOrigin="Anonymous" v-bind:id="'github_d'+list.id" :src="list.img_github" width="100" height="100"></td>
                     <td><img crossOrigin="Anonymous" v-bind:id="'google_d'+list.id" :src="list.img_google" width="100" height="100"></td>
                     <td><img crossOrigin="Anonymous" v-bind:id="'instagram_d'+list.id" :src="list.foto_instagram" width="100" height="100"></td>
                     <td><button class="btn btn-success" v-on:click.prevent="getexInfo(list)"> <i class="fa fa-file-pdf-o"></i> Exportar</button>
                         <button class="btn btn-danger" v-on:click.prevent="getexDelete(list)"> <i class="fa fa-trash-o"></i> Eliminar</button>
                    </td>
                 </tr>
                 </template>
                 <template v-else>
                   <tr>
                       <td colspan="8" align="center">No hay resultados disponibles</td>
                   </tr>
                 </template>
            </tbody>
            </table>
            </div>
            </div>
          </div>
        <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
              <iframe id="pdf_preview" type="application/pdf" src="" width="530" height="400"></iframe>
           </div>
      </div> 
      <div>
        <canvas id="myCanvas" style="display:none"/>
        <canvas id="myCanvas2" style="display:none"/>
        <canvas id="myCanvas3" style="display:none"/>
        <canvas id="myCanvas4" style="display:none"/>
        <canvas id="myCanvas5" style="display:none" />   
      </div>
      
</div>      
</template>

<script>
import swal from 'sweetalert';
import jsPDF from 'jspdf';
import moment from 'moment';
import 'moment/locale/es';
moment.locale('es');
var crf_tok = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
var config = {
     headers: {'X-CSRFToken': crf_tok}
};
export default {
 created(){
    this.getDataAll();   
    this.getPersonaAs();
 },
  data(){ 
      return{
        lista:[],
        options: [],
        combo:'',
        lista_base:[]
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
     getexDelete(list){
             let url_delete="http://127.0.0.1:8000/reporte/deletereporte/"+list.id;
               var selfdel=this;
               swal({
                    title: "Estas seguro?",
                    text: "Eliminara a "+list.nombre_persona,
                    icon: "warning",
                    buttons: true,
                    dangerMode: true,
              })
              .then((willDelete) => {
                    if (willDelete) {
                   axios.delete(url_delete,config).then(response => {
                       selfdel.mensaje('Excelente',response.data.message,'success');
                       selfdel.getDataAll();
                        })
                        .catch(error => {
                         console.log(error);
                   });
                    } else {
                    console.log("");
                    }
               });
     },
     getexInfo(value){
      
      //twiter
      var id=value.id;
      var img_tw=value.img_tw;
      var inicio_tw=value.inicio_tw;
      var likes_tw=value.likes_tw;
      var biografia_tw=value.biografia_tw;
      var cant_tw=value.cant_tw;
      var nombre_cuenta_tw=value.nombre_cuenta_tw;
      var nombre_tw=value.nombre_tw;
      var pagina_web_tw=value.pagina_web_tw;
      var seguidores_tw=value.seguidores_tw;
      var siguiendo_tw=value.siguiendo_tw;
      var tweets_tw=value.tweets_tw;
      var ubicacion_tw=value.ubicacion_tw;
      var url_tw=value.url_tw;
      //facebook
      var biografia_fb=value.biografia_fb;
      var estudio_fb=value.estudio_fb;
      var foto_fb=value.foto_fb;    
      var lugar_fb=value.lugar_fb;
      var nombres_fb=value.nombres_fb;
      var trabajo_fb=value.trabajo_fb;
      var url_fb=value.url_fb;
      //persona     
      var apodo_persona=value.apodo_persona;
      var nombre_persona=value.nombre_persona; 
      var tregistro_persona=value.tregistro_persona;
      
      //google      
      var nombre_google=value.nombre_google;
      var url_google=value.url_google;
      var img_google=value.img_google;
      var info_google=value.info_google;
      //instagram
      var nombre_instagram=value.nombre_instagram;
      var usuario_instagram=value.usuario_instagram;
      var url_instagram=value.url_instagram;
      var foto_instagram=value.foto_instagram;
      var seguidores_instagram=value.seguidores_instagram;
      var post_instagram=value.post_instagram;
      var siguiendo_instagram=value.siguiendo_instagram;
      //github
      var biografia_github=value.biografia_github;
      var email_github=value.email_github;
      var img_github=value.img_github;
      var nick_github=value.nick_github;
      var nombre_github=value.nombre_github;
      var pagina_github=value.pagina_github;
      var pais_github=value.pais_github;
      var arreglo_fotos=[foto_fb,img_tw,foto_instagram,img_google,img_github];
      var arreglo_x=[];
      var self=this;
      
      var imgfb_new=this.cargarImagen("myCanvas","facebook_d"+id);
      var imgtw_new=this.cargarImagen("myCanvas2","twitter_d"+id);
      var imggit_new=this.cargarImagen("myCanvas3","github_d"+id);
      var imggoogl_new=this.cargarImagen("myCanvas4","google_d"+id);
      var imginstagr_new=this.cargarImagen("myCanvas5","instagram_d"+id);



              var doc = new jsPDF();
                 doc.setFontSize(24);
                         doc.text(42,30, "Reporte de asignacion por persona");
                         doc.line(35, 35, 180, 35);
                         doc.setTextColor(255, 0, 0);
                         doc.setFontSize(14);
                         doc.setTextColor(255, 0, 0);
                         doc.text(12,50, "Datos de persona:");
                         doc.setFontSize(14);
                         doc.setTextColor(1, 5, 3);
                         doc.text(12,60, "* Nombre");
                         doc.text(55,60, ":");
                         doc.text(72,60, nombre_persona);
                         doc.text(12,70, "* Apodo");
                         doc.text(55,70, ":");
                         doc.text(72,70, apodo_persona);
                         doc.text(12,80, "* Fecha de registro");
                         doc.text(55,80, ":");
                         doc.text(72,80,  moment(tregistro_persona).format('LLLL'));
                         doc.line(12, 87, 180, 87);
                         doc.setFontSize(14);
                         doc.setTextColor(255, 0, 0);
                         doc.text(12,95, "Datos de Redes sociales:");
                         doc.setTextColor(1, 5, 93);
                         doc.text(12,105, "- Facebook:"); 
                         doc.setTextColor(1, 5, 3);
                         doc.text(12,115, "* Nombre");
                         doc.text(55,115, ":");
                         doc.text(72,115, nombres_fb);
                         doc.text(12,125, "* Url");
                         doc.text(55,125, ":");
                         doc.text(72,125, url_fb);
                         doc.text(12,135, "* Biografia");
                         doc.text(55,135, ":");
                         doc.text(72,135, biografia_fb);
                         doc.text(12,145, "* Estudio");
                         doc.text(55,145, ":");
                         doc.text(72,145, estudio_fb);
                         doc.text(12,155, "* Lugar");
                         doc.text(55,155, ":");
                         doc.text(72,155, lugar_fb);
                         doc.text(12,165, "* Trabajo");
                         doc.text(55,165, ":");
                         doc.text(72,165, trabajo_fb);
                         doc.text(12,190, "* Foto");
                         doc.text(55,190, ":");
                         doc.addImage(imgfb_new, 72, 175, 30, 30);
                         doc.setTextColor(1, 5, 93);
                         doc.text(12,220, "- Twitter:"); 
                         doc.setTextColor(1, 5, 3);
                         doc.text(12,230, "* Inicio");
                         doc.text(55,230, ":");
                         doc.text(72,230, inicio_tw);
                         doc.text(12,240, "* Likes");
                         doc.text(55,240, ":");
                         doc.text(72,240, likes_tw);
                         doc.text(12,250, "* Biografia");
                         doc.text(55,250, ":");
                         doc.text(72,250, biografia_tw);
                         doc.text(12,260, "* Cantidad Twetts");
                         doc.text(55,260, ":");
                         doc.text(72,260, cant_tw);
                         doc.text(12,270, "* Cuenta");
                         doc.text(55,270, ":");
                         doc.text(72,270, nombre_cuenta_tw);
                         doc.text(12,280, "* Seguidores");
                         doc.text(55,280, ":");
                         doc.text(72,280, seguidores_tw);
                         doc.addPage();
                         doc.text(12,20, "* Siguiendo");
                         doc.text(55,20, ":");
                         doc.text(72,20, siguiendo_tw);
                         doc.text(12,30, "* Ubicacion");
                         doc.text(55,30, ":");
                         doc.text(72,30, ubicacion_tw);
                         doc.text(12,40, "* Tweets");
                         doc.text(55,40, ":");
                         doc.text(72,40, tweets_tw);
                         doc.text(12,50, "* Url");
                         doc.text(55,50, ":");
                         doc.text(72,50, url_tw);
                         doc.text(12,70, "* Foto");
                         doc.text(55,70, ":");
                         doc.addImage(imgtw_new, 72, 60, 70, 70);
                         doc.setTextColor(1, 5, 93);
                         doc.text(12,100, "- Instagram:"); 
                         doc.setTextColor(1, 5, 3);
                         doc.text(12,113, "* Usuario");
                         doc.text(55,113, ":");
                         doc.text(72,113, usuario_instagram);
                         doc.text(12,123, "* Nombre");
                         doc.text(55,123, ":");
                         doc.text(72,123, nombre_instagram);
                         doc.text(12,133, "* Url");
                         doc.text(55,133, ":");
                         doc.text(72,133, url_instagram);
                         doc.text(12,143, "* Seguidores");
                         doc.text(55,143, ":");
                         doc.text(72,143, seguidores_instagram);
                         doc.text(12,153, "* Post");
                         doc.text(55,153, ":");
                         doc.text(72,153, post_instagram);
                         doc.text(12,163, "* Siguiendo");
                         doc.text(55,163, ":");
                         doc.text(72,163, siguiendo_instagram);
                         doc.text(12,183, "* Foto");
                         doc.text(55,183, ":");
                         doc.addImage(imggit_new, 72, 170, 50, 50);
                         doc.setTextColor(1, 5, 93);
                         doc.text(12,213, "- Google:");
                         doc.setTextColor(1, 5, 3);
                         doc.text(12,223, "* Informacion");
                         doc.text(55,223, ":");
                         doc.text(72,223, info_google);
                         doc.text(12,233, "* Nombre");
                         doc.text(55,233, ":");
                         doc.text(72,233, nombre_google);
                         doc.text(12,243, "* Url");
                         doc.text(55,243, ":");
                         doc.text(72,243, url_google);
                         doc.text(12,263, "* Foto");
                         doc.text(55,263, ":");
                         doc.addImage(imggoogl_new, 72, 253, 50, 50);
                         doc.addPage();
                         doc.setTextColor(1, 5, 93);
                         doc.text(12,13, "- Github:");
                         doc.setTextColor(1, 5, 3);
                         doc.text(12,23, "* Nombre");
                         doc.text(55,23, ":");
                         doc.text(72,23, nombre_github);
                         doc.text(12,33, "* Email");
                         doc.text(55,33, ":");
                         doc.text(72,33, email_github);
                         doc.text(12,43, "* Pagina");
                         doc.text(55,43, ":");
                         doc.text(72,43, pagina_github);
                         doc.text(12,53, "* Usuario");
                         doc.text(55,53, ":");
                         doc.text(72,53, nick_github);
                         doc.text(12,63, "* Pais");
                         doc.text(55,63, ":");
                         doc.text(72,63, pais_github);
                         doc.text(12,73, "* Biografia");
                         doc.text(55,73, ":");
                         doc.text(72,73, biografia_github);
                         doc.text(12,93, "* Foto");
                         doc.text(55,93, ":");
                         doc.addImage(imginstagr_new, 72, 83, 50, 40);
               
                         $("#pdf_preview").attr("src", doc.output('datauristring'));
              
     },
     cargarImagen(dcanvan,idmg){

           var cx = document.getElementById(dcanvan); 
           var  ctx = cx.getContext("2d");
           var img = document.getElementById(idmg);
           ctx.drawImage(img, 1, 1);
          return  cx.toDataURL()
     },

     getPersonaAs(){
            axios.get('http://127.0.0.1:8000/api/persona/',{})
                        .then(response=>{ 
                                this.options=response.data;                              
                        })
                        .catch(error=>{
                                console.log(error);
                        }) 
    },
     getDataAll(){
         var id_persona=this.combo;
         if(id_persona==''){
            id_persona=0; 
         }else{
            id_persona=id_persona; 
         }
         axios.get('http://127.0.0.1:8000/reporte/consultall',{ params: { id_persona: id_persona}})
               .then(response=>{
                 this.lista=response.data.info
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
    width: 100%;
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