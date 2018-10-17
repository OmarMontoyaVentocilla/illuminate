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
                     <td>
                <img v-if="list.foto_fb!=''" crossOrigin="Anonymous" v-bind:id="'facebook_d'+list.id" :src="list.foto_fb" width="100" height="100">
                <img v-if="list.foto_fb==''" crossOrigin="Anonymous" v-bind:id="'facebook_d'+list.id" src="https://scrat.hellocoton.fr/img/classic/des-avatars-incognito-pour-facebook-7846209.jpg" width="100" height="100">
                
                </td>
                     <td><img  crossOrigin="Anonymous" v-bind:id="'twitter_d'+list.id" :src="list.img_tw" width="100" height="100"></td>
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
      console.log(value);
      var incognito="https://scrat.hellocoton.fr/img/classic/des-avatars-incognito-pour-facebook-7846209.jpg";
      //twiter
      var id=value.id;
      if(value.img_tw!=''){
        var img_tw=value.img_tw;
      }else{
         var img_tw=incognito; 
      }
      
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
      
      if(value.foto_fb!=''){
         var foto_fb=value.foto_fb;  
      }else{
          var foto_fb=incognito;  
      }
        

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

      if(value.img_google!=''){
      var img_google=value.img_google;
      }else{
       var img_google=incognito;    
      }

      var info_google=value.info_google;
      //instagram
      var nombre_instagram=value.nombre_instagram;
      var usuario_instagram=value.usuario_instagram;
      var url_instagram=value.url_instagram;

      if(value.foto_instagram!=''){
      var foto_instagram=value.foto_instagram;
      }else{
       var foto_instagram=incognito;    
      }
      
      var seguidores_instagram=value.seguidores_instagram;
      var post_instagram=value.post_instagram;
      var siguiendo_instagram=value.siguiendo_instagram;
      //github
      var biografia_github=value.biografia_github;
      var email_github=value.email_github;

      if(value.img_github!=''){
      var img_github=value.img_github;
      }else{
       var img_github=incognito;    
      }

      var nick_github=value.nick_github;
      var nombre_github=value.nombre_github;
      var pagina_github=value.pagina_github;
      var pais_github=value.pais_github;


      var arreglo_fotos=[foto_fb,img_tw,foto_instagram,img_google,img_github];
      var arreglo_x=[];
      var self=this;
      

      if(value.foto_fb!=''){
       var imgfb_new=this.cargarImagen("myCanvas","facebook_d"+id);
      }else{
       var imgfb_new="No hay informacion" ;  
      }
      
      if(value.img_tw!=''){
          var imgtw_new=this.cargarImagen("myCanvas2","twitter_d"+id);
      }else{
          var imgtw_new="No hay informacion"; 
      }


      if(value.img_google!=''){
          var imggoogl_new=this.cargarImagen("myCanvas4","google_d"+id);
      }else{
          var imggoogl_new="No hay informacion";
      }

      if(value.img_github!=''){
         var imggit_new=this.cargarImagen("myCanvas3","github_d"+id);
      }else{
          var imggit_new="No hay informacion"; 
      }
     
       if(value.foto_instagram!=''){
         var imginstagr_new=this.cargarImagen("myCanvas5","instagram_d"+id);
      }else{
          var imginstagr_new="No hay informacion"; 
      }
      
//aqui es el reporee
                     var doc = new jsPDF('p','','a4');
                         
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
                         doc.text(72,115, doc.splitTextToSize(nombres_fb,120));
                         doc.text(12,125, "* Url");
                         doc.text(55,125, ":");
                         doc.text(72,125, doc.splitTextToSize(url_fb,120));
                         doc.text(12,135, "* Biografia");
                         doc.text(55,135, ":");
                         doc.text(72,135, doc.splitTextToSize(biografia_fb,120));
                         doc.text(12,148, "* Estudio");
                         doc.text(55,148, ":");
                         doc.text(72,148, doc.splitTextToSize(estudio_fb,120));
                         doc.text(12,155, "* Lugar");
                         doc.text(55,155, ":");
                         doc.text(72,155, doc.splitTextToSize(lugar_fb,120));
                         doc.text(12,165, "* Trabajo");
                         doc.text(55,165, ":");
                         doc.text(72,165, doc.splitTextToSize(trabajo_fb,120));
                         doc.text(12,190, "* Foto");
                         doc.text(55,190, ":");
                         if(value.foto_fb!=''){
                         doc.addImage(imgfb_new, 72, 175, 30, 30);
                         }else{
                           doc.text(72,190,imgfb_new);   
                         }
                         doc.setTextColor(1, 5, 93);
                         doc.text(12,220, "- Twitter:"); 
                         doc.setTextColor(1, 5, 3);
                         doc.text(12,230, "* Inicio");
                         doc.text(55,230, ":");
                         doc.text(72,230, doc.splitTextToSize(inicio_tw,120));
                         doc.text(12,240, "* Likes");
                         doc.text(55,240, ":");
                         doc.text(72,240, doc.splitTextToSize(likes_tw,120));
                         doc.text(12,249, "* Biografia");
                         doc.text(55,249, ":");
                         doc.text(72,249, doc.splitTextToSize(biografia_tw,120));
                         doc.text(12,272, "* Cantidad Twetts");
                         doc.text(55,272, ":");
                         doc.text(72,272, doc.splitTextToSize(cant_tw,120));
                         doc.text(12,279, "* Cuenta");
                         doc.text(55,279, ":");
                         doc.text(72,279, doc.splitTextToSize(nombre_cuenta_tw,120));
                         doc.text(12,284, "* Seguidores");
                         doc.text(55,284, ":");
                         doc.text(72,284, doc.splitTextToSize(seguidores_tw,120));
                         doc.addPage();
                         doc.text(12,20, "* Siguiendo");
                         doc.text(55,20, ":");
                         doc.text(72,20, doc.splitTextToSize(siguiendo_tw,120));
                         doc.text(12,30, "* Ubicacion");
                         doc.text(55,30, ":");
                         doc.text(72,30, doc.splitTextToSize(ubicacion_tw,120));
                         doc.text(12,40, "* Tweets");
                         doc.text(55,40, ":");
                         doc.text(72,40, doc.splitTextToSize(tweets_tw,120));
                         doc.text(12,50, "* Url");
                         doc.text(55,50, ":");
                         doc.text(72,50, doc.splitTextToSize(url_tw,120));
                         doc.text(12,70, "* Foto");
                         doc.text(55,70, ":");
                          if(value.img_tw!=''){
                           doc.addImage(imgtw_new, 72, 60, 70, 70);
                         }else{
                           doc.text(72,190,imgtw_new);   
                         }

                         doc.setTextColor(1, 5, 93);
                         doc.text(12,100, "- Instagram:"); 
                         doc.setTextColor(1, 5, 3);
                         doc.text(12,113, "* Usuario");
                         doc.text(55,113, ":");
                         doc.text(72,113, doc.splitTextToSize(usuario_instagram,120));
                         doc.text(12,123, "* Nombre");
                         doc.text(55,123, ":");
                         doc.text(72,123, doc.splitTextToSize(nombre_instagram,120));
                         doc.text(12,133, "* Url");
                         doc.text(55,133, ":");
                         doc.text(72,133, doc.splitTextToSize(url_instagram,120));
                         doc.text(12,143, "* Seguidores");
                         doc.text(55,143, ":");
                         doc.text(72,143, doc.splitTextToSize(seguidores_instagram,120));
                         doc.text(12,153, "* Post");
                         doc.text(55,153, ":");
                         doc.text(72,153, doc.splitTextToSize(post_instagram,120));
                         doc.text(12,163, "* Siguiendo");
                         doc.text(55,163, ":");
                         doc.text(72,163, doc.splitTextToSize(siguiendo_instagram,120));
                         doc.text(12,183, "* Foto");
                         doc.text(55,183, ":");
                          if(value.foto_instagram!=''){
                          doc.addImage(imginstagr_new, 72, 170, 50, 30);
                         }else{
                           doc.text(72,190,imginstagr_new);   
                         }
  
                         doc.setTextColor(1, 5, 93);
                         doc.text(12,213, "- Google:");
                         doc.setTextColor(1, 5, 3);
                         doc.text(12,223, "* Informacion");
                         doc.text(55,223, ":");
                         doc.text(72,223, doc.splitTextToSize(info_google,120));
                         doc.text(12,264, "* Nombre");
                         doc.text(55,264, ":");
                         doc.text(72,264, doc.splitTextToSize(nombre_google,120));
                         doc.text(12,273, "* Url");
                         doc.text(55,273,    ":");
                         doc.text(72,273, doc.splitTextToSize(url_google,120));
                         doc.addPage();
                         doc.text(12,13, "* Foto");
                         doc.text(55,13, ":");
                         if(value.foto_instagram!=''){
                          doc.addImage(imggoogl_new, 72, 12, 50, 50);
                         }else{
                           doc.text(22,190,imggoogl_new);   
                         }
                         
                         doc.setTextColor(1, 5, 93);
                         doc.text(12,53, "- Github:");
                         doc.setTextColor(1, 5, 3);
                         doc.text(12,61, "* Nombre");
                         doc.text(55,61, ":");
                         doc.text(72,61, doc.splitTextToSize(nombre_github,120));
                         doc.text(12,69, "* Email");
                         doc.text(55,69, ":");
                         doc.text(72,69, doc.splitTextToSize(email_github,120));
                         doc.text(12,77, "* Pagina");
                         doc.text(55,77, ":");
                         doc.text(72,77, doc.splitTextToSize(pagina_github,120));
                         doc.text(12,84, "* Usuario");
                         doc.text(55,84, ":");
                         doc.text(72,84, doc.splitTextToSize(nick_github,120));
                         doc.text(12,91, "* Pais");
                         doc.text(55,91, ":");
                         doc.text(72,91, doc.splitTextToSize(pais_github,120));
                         doc.text(12,99, "* Biografia");
                         doc.text(55,99, ":");
                         doc.text(72,99, doc.splitTextToSize(biografia_github,120));
                         doc.text(12,110, "* Foto");
                         doc.text(55,110, ":");
                          if(value.img_github!=''){
                           doc.addImage(imggit_new, 72, 110, 50, 40);
                         }else{
                           doc.text(22,110,imggit_new);   
                         }
                        
                         doc.save(nombre_persona+'-'+nombre_persona+'-'+tregistro_persona+'.pdf');
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