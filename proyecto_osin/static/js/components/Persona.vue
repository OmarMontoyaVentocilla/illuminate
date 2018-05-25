<template>
      <div class="container">
          <div class="row">
              <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
            <form v-on:submit.prevent="createPersona()">
             <div class="form-group" >  
                <label for="nombre" class="bmd-label-floating">Nombre:</label>
                <input type="text" class="form-control" name="nombre" id="nombre" v-model.trim="persona.nombre" autocomplete="off">
            </div>
           <div class="form-group">
              <label for="apodo" class="bmd-label-floating">Apodo:</label>
              <input type="text" class="form-control" name="apodo" id="apodo" v-model.trim="persona.apodo" autocomplete="off">
           </div>
            <div class="form-group">
                <button class="btn btn-raised btn-primary" type="submit" id="envio">Agregar</button>
            </div> 
            </form>
              </div>
          </div>

       <div class="row">
          <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                <div class="panel panel-success panel_estilo_persona">
           <div class="panel-body div1 table-responsive">
            <table class="table table-bordered table-hover table-fixed table-striped" style="background:white;">   
             <thead>
                 <tr>
                     <th>#</th>
                     <th>Nombre</th>
                     <th>Apodo</th>
                     <th>Acción</th>
                 </tr>
            </thead>
            <tbody>
                 <template v-if="lista!=''">
                 <tr v-for="(list,index) in lista">
                    <td>{{index+1}}</td>
                    <td>{{list.nombre}}</td>
                    <td>{{list.apodo}}</td>
                    <td align="center">
                <button type="button" class="btn btn-raised btn-primary">Editar</button>
                <button type="button" class="btn btn-raised btn-danger" v-on:click.prevent="deletepersona(list)">Eliminar</button>
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
      </div>
</template>
<script>

import swal from 'sweetalert';
var crf_tok = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
var config = {
     headers: {'X-CSRFToken': crf_tok}
};
export default{
    created(){
       this.getPersona();
    },
    data(){
        return{
           persona:{
                 nombre:'',
                 apodo:''
           },
           lista:[] 
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
        disabl(valor){
         $("#envio").prop('disabled', valor);
        },
        limpiar(){
          this.persona.nombre='';
          this.persona.apodo='';
        },
        getPersona(){
           axios.get('/api/persona/')
           .then(response=>{
               this.lista=response.data;
           })
           .catch(error=>{
               console.log(error);
           })
        },
        deletepersona(info){
               let url_delete="http://127.0.0.1:8000/persona/deletepersona/"+info.id;
               var selfdel=this;
               swal({
                    title: "Estas seguro?",
                    text: "Eliminara a "+info.nombre,
                    icon: "warning",
                    buttons: true,
                    dangerMode: true,
              })
              .then((willDelete) => {
                    if (willDelete) {
                   axios.delete(url_delete,config).then(response => {
                       selfdel.mensaje('Excelente',response.data.message,'success');
                       selfdel.getPersona();
                        })
                        .catch(error => {
                         console.log(error);
                   });
                    } else {
                    alert("xxxxxxx");
                    }
               });
        },
        createPersona(){
             var crf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
            var data={
                     nombre: this.persona.nombre,
                     apodo: this.persona.apodo
                     };
            var sel_thi=this;
            sel_thi.disabl(true);
            setTimeout(function(){sel_thi.disabl(false); }, 2000);         
            axios.post('http://127.0.0.1:8000/persona/addpersona',data,config)
                .then(response=>{
                          if(response.data.success){
                           this.mensaje(response.data.success,'','success');
                           this.getPersona();
                           this.limpiar(); 
                          }else if(response.data.fail){
                           this.mensaje(response.data.fail,'','error');
                           this.limpiar(); 
                          } 
                     })
                .catch(error=>{
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

.panel.panel-success.panel_estilo_persona {
    border: 1px solid #2a3f54;
    -webkit-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
    -moz-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
     box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
    width: 80%;
    margin: auto;
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