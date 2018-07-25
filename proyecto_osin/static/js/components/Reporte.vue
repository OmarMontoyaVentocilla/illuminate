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
                     <th>Acción</th>
                 </tr>
            </thead>
            <tbody>
                 <template v-if="lista!=''">
                <tr v-for="(list,index) in lista">
                     <td>{{index+1}}</td>
                     <td>{{list.apodo_persona}}</td>
                     <td><img :src="list.foto_fb" width="100" height="100"></td>
                     <td><img :src="list.img_tw" width="100" height="100"></td>
                     <td><button class="btn btn-success" v-on:click.prevent="getexInfo(list)"> <i class="fa fa-file-pdf-o"></i> Exportar</button>
                         <button class="btn btn-danger" v-on:click.prevent="getexDelete(list)"> <i class="fa fa-trash-o"></i> Eliminar</button>
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
        <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
          <iframe id="pdf_preview" type="application/pdf" src="" width="530" height="400"></iframe>
           </div>
      </div>
   
</div>      
</template>

<script>
import swal from 'sweetalert';
import jsPDF from 'jspdf';
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
        combo:''
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
      var apodo_persona=value.apodo_persona;
      var biografia_fb=value.biografia_fb;
      var biografia_tw=value.biografia_tw;
      var cant_tw=value.cant_tw;
      var estudio_fb=value.estudio_fb;
      var foto_fb=value.foto_fb;
      var img_tw=value.img_tw;
      var inicio_tw=value.inicio_tw;
      var likes_tw=value.likes_tw;
      var lugar_fb=value.lugar_fb;
      var nombre_cuenta_tw=value.nombre_cuenta_tw;
      var nombre_persona=value.nombre_persona;
      var nombre_tw=value.nombre_tw;
      var nombres_fb=value.nombres_fb;
      var pagina_web_tw=value.pagina_web_tw;
      var seguidores_tw=value.seguidores_tw;
      var siguiendo_tw=value.siguiendo_tw;
      var trabajo_fb=value.trabajo_fb;
      var tregistro_persona=value.tregistro_persona;
      var tweets_tw=value.tweets_tw;
      var ubicacion_tw=value.ubicacion_tw;
      var url_fb=value.url_fb;
      var url_tw=value.url_tw;


         var doc = new jsPDF({
                // orientation: 'landscape',
                // unit: 'in',
                // format: [4, 2]
        })
        doc.text(20, 20, apodo_persona);
        doc.text(20, 30, 'This is client-side Javascript, pumping out a PDF.');
        doc.addPage();
        doc.text(20, 20, 'Do you like that?');

        // doc.text('Hello world!', 1, 1);
        $("#pdf_preview").attr("src", doc.output('datauristring'));
        //doc.save('two-by-four.pdf')
        //var string = doc.output('datauristring');
        // var iframe = "<iframe width='100%' height='100%' src='" + string + "'></iframe>";
        // var x = window.open();
        // x.document.open();
        // x.document.write(iframe);
        // x.document.close();
        //doc.output('dataurlnewwindow'); 
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
      