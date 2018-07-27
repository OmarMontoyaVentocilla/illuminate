<template>
   <div class="container">
    <div class="row">
        <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
           <form v-on:submit.prevent="getaddasig()"> 
            <div class="form-group">
                 <label for="exampleInputEmail1">Persona</label>
                 <v-select label="nombre" :options="options" v-model="idpersona"></v-select>
            </div>
             <div class="form-group">
                 <label for="exampleInputEmail1">Datos guardados de Facebook</label>
                 <v-select label="nombres" :options="optionsfb" v-model="idfb"></v-select>
            </div>
             <div class="form-group">
                 <label for="exampleInputEmail1">Datos guardados de Twitter</label>
                 <v-select label="nombre_cuenta_tw" :options="optionstw" v-model="idtw"></v-select>    
            </div>
            <div class="form-group">
                 <label for="exampleInputEmail1">Datos guardados de Google</label>
                 <v-select label="nombre_google" :options="optionsgogle" v-model="idgoogle"></v-select>    
            </div>
            <div class="form-group">
             <button type="submit" id="envioasig" class="btn btn-primary">Guardar</button>
            </div>
            </form> 
        </div> 
    </div>
    <div class="row">
      <div class="col-lg-4 col-md-4 col-sm-4 col-xs-4">
         <template v-if="idfb.id!=''">
                 <img :src="idfb.foto" width="100" height="100">
          </template>
          <template v-else>
                <img src="/static/img/facebook-perfil.jpg" width="100" height="100"> 
          </template>
      </div>
       <div class="col-lg-4 col-md-4 col-sm-4 col-xs-4">
             <template v-if="idtw.id!=''">
                 <img :src="idtw.img_tw" width="100" height="100">
          </template>
           <template v-else>
                <img src="/static/img/twitter-perfil.jpg" width="100" height="100"> 
           </template>
      </div>
      <div class="col-lg-4 col-md-4 col-sm-4 col-xs-4">
             <template v-if="idgoogle.id!=''">
                 <img :src="idgoogle.img_google" width="100" height="100">
          </template>
           <template v-else>
                <img src="/static/img/google-perfil.jpg" width="100" height="100"> 
           </template>
      </div>
    </div>
   </div>        
</template>    
<script>
import swal from 'sweetalert';
import vSelect from 'vue-select';
var tokenx = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
var config = {
     headers: {'X-CSRFToken': tokenx}
};
export default{
    created(){
     this.getPersonaAs();
     this.getFacebookAs();
     this.getTwitterAs();
     this.getGoogleAs();
     
    },
     components: {
         'vSelect':vSelect
        },
     mounted(){
       

     },
    data(){
       return{
           options: [],
           optionsfb:[],
           optionsgogle:[],
           optionstw:[],
           idpersona:{id:"", nombre:"Seleccione"},
           idfb:{id: "", nombres: "Seleccione"},
           idtw:{id: "", nombre_cuenta_tw: "Seleccione"},
           idgoogle:{id: "", nombre_google: "Seleccione"}  
      }
    },
    methods:{
         disabl(valor){
               $("#envioasig").prop('disabled', valor);
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
        getPersonaAs(){
            axios.get('http://127.0.0.1:8000/api/persona/',{})
                        .then(response=>{ 
                                this.options=response.data;                              
                        })
                        .catch(error=>{
                                console.log(error);
                        }) 
        },
         getGoogleAs(){
            axios.get('http://127.0.0.1:8000/api/google/',{})
                        .then(response=>{ 
                                this.optionsgogle=response.data;
       
                        })
                        .catch(error=>{
                                console.log(error);
                        }) 
        },
        getFacebookAs(){
            axios.get('http://127.0.0.1:8000/api/facebook/',{})
                        .then(response=>{ 
                                this.optionsfb=response.data;
       
                        })
                        .catch(error=>{
                                console.log(error);
                        }) 
        },
        getTwitterAs(){
            axios.get('http://127.0.0.1:8000/api/twitter/',{})
                        .then(response=>{ 
                                this.optionstw=response.data;                        
                        })
                        .catch(error=>{
                                console.log(error);
                        }) 
        },
        getaddasig(){
              var data={
                    idfb_id:this.idfb.id,
                    idgoogle_id:this.idgoogle.id,
                    idpersona_id:this.idpersona.id,
                    idtw_id:this.idtw.id
                     };
            var sel_thi=this;
            sel_thi.disabl(true);
            setTimeout(function(){sel_thi.disabl(false); }, 2000);
              
            if(this.idfb.id!='' && this.idpersona.id!='' &&  this.idtw.id!=''){ 
            axios.post('http://127.0.0.1:8000/search/addasignacion',data,config)
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
            }else{
                this.mensaje('Llene los campos','','error'); 
            }
        }
    },
    computed:{
         descripcionColor(){
            if(this.idtw.img_tw!=''){
                return ['imgtwprofile'];
            }
         }
    }  
}
</script>

