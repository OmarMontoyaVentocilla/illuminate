<template>
<div class="container">
      <div class="row">
          <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
         <div class="form-group">
              <label for="persona">ALGERIA</label>
              <select class="form-control input-sm" v-model="combo_algeria" @change="gettrending()" id="combo_algeria">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_algeria" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
         <div class="form-group">
              <label for="persona">ARGENTINA</label>
              <select class="form-control input-sm" v-model="combo_argentina" @change="gettrending()" id="combo_argentina">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_argentina" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
          <div class="form-group">
              <label for="persona">AUSTRALIA</label>
              <select class="form-control input-sm" v-model="combo_australia" @change="gettrending()" id="combo_australia">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_australia" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
         <div class="form-group">
              <label for="persona">AUSTRIA</label>
              <select class="form-control input-sm" v-model="combo_austria" @change="gettrending()" id="combo_austria"> 
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_austria" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
          <div class="form-group">
              <label for="persona">BRAZIL</label>
              <select class="form-control input-sm" v-model="combo_brazil" @change="gettrending()" id="combo_brazil">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_brasil" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
          <div class="form-group">
              <label for="persona">CHILE</label>
              <select class="form-control input-sm" v-model="combo_chile" @change="gettrending()" id="combo_chile">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_chile" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
           <div class="form-group">
              <label for="persona">COLOMBIA</label>
              <select class="form-control input-sm" v-model="combo_colombia" @change="gettrending()" id="combo_colombia">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_colombia" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
          <div class="form-group">
              <label for="persona">ECUADOR</label>
              <select class="form-control input-sm" v-model="combo_ecuador" @change="gettrending()" id="combo_ecuador">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_ecuador" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
          <div class="form-group">
              <label for="persona">MEXICO</label>
              <select class="form-control input-sm" v-model="combo_mexico" @change="gettrending()" id="combo_mexico">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_mexico" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
           <div class="form-group">
              <label for="persona">PERÚ</label>
              <select class="form-control input-sm" v-model="combo_peru" @change="gettrending()" id="combo_peru">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_peru" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
           <div class="form-group">
              <label for="persona">ESPAÑA</label>
              <select class="form-control input-sm" v-model="combo_spain" @change="gettrending()" id="combo_spain"> 
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_spain" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
         
         
          </div>
          <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
             <div class="form-group" v-show="loading">
              <i class="fa fa-spinner fa-spin" style="font-size:48px"></i> Cargando tendencias....
            </div> 
                  <div class="panel-body div1 table-responsive">
            <table class="table table-bordered table-hover table-fixed table-striped" style="background:white;">
                 <thead>
                 <tr>
                     <th>#</th>
                     <th>Trending Topic Global</th>
                 </tr>
                 </thead>
                  <tbody>
                     <template v-if="lista!=''">
                  <tr v-for="(list,index) in lista">
                      <td>{{index+1}}</td>
                      <td>{{list}}</td>
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
</template>
<script>

 export default{
     created(){
       this.gettrending();
     },
     data(){
         return{
            lista:[], 
            loading: false,
            combo_algeria:'',
            combo_argentina:'',
            combo_australia:'',
            combo_austria:'',
            combo_brazil:'',
            combo_chile:'',
            combo_colombia:'',
            combo_ecuador:'',
            combo_mexico:'',
            combo_peru:'',
            combo_spain:'', 
            options_algeria:[
 		     { id: 'algeria', nombre: 'ALGERIA'},
 		     { id: 'algeria/algiers', nombre: 'ALGIERS'}
            ],
           options_argentina:[
             { id: 'argentina', nombre: 'ARGENTINA'},
             { id: 'argentina/buenos-aires', nombre: 'BUENOS AIRES'},
             { id: 'argentina/cordoba', nombre: 'CÓRDOBA'},
             { id: 'argentina/mendoza', nombre: 'MENDOZA'},
             { id: 'argentina/rosario', nombre: 'ROSARIO'}
           ],
           options_australia:[
             { id: 'australia', nombre: 'AUSTRALIA'},
             { id: 'australia/adelaide', nombre: 'ADELAIDE'},
             { id: 'australia/brisbane', nombre: 'BRISBANE'},
             { id: 'australia/canberra', nombre: 'CANBERRA'},
             { id: 'australia/darwin', nombre: 'DARWIN'},
             { id: 'australia/melbourne', nombre: 'MELBOURNE'},
             { id: 'australia/perth', nombre: 'PERTH'},
             { id: 'australia/sydney', nombre: 'SYDNEY'}
           ],
            options_austria:[
             { id: 'austria', nombre: 'AUSTRIA'},
             { id: 'austria/vienna', nombre: 'VIENNA'}, 
           ],
           options_brasil:[
             { id: 'brazil', nombre: 'BRAZIL'},
             { id: 'brazil/belem', nombre: 'BELÉM'}, 
             { id: 'brazil/belo-horizonte', nombre: 'BELO HORIZONTE'},
             { id: 'brazil/brasilia', nombre: 'BRASÍLIA'}, 
             { id: 'brazil/campinas', nombre: 'CAMPINAS'},
             { id: 'brazil/curitiba', nombre: 'CURITIBA'}, 
             { id: 'brazil/fortaleza', nombre: 'FORTALEZA'},
             { id: 'brazil/vienna', nombre: 'PORTO ALEGRE'}, 
             { id: 'brazil/porto-alegre', nombre: 'RECIFE'},
             { id: 'brazil/rio-de-janeiro', nombre: 'RIO DE JANEIRO'}, 
             { id: 'brazil/salvador', nombre: 'SALVADOR'},
             { id: 'brazil/sao-paulo', nombre: 'SAO PAULO'}
           ],
           options_chile:[
             { id: 'chile', nombre: 'CHILE'},
             { id: 'chile/concepcion', nombre: 'CONCEPCIÓN'}, 
             { id: 'chile/santiago', nombre: 'SANTIAGO'},
             { id: 'chile/valparaiso', nombre: 'VALPARAISO'}
           ],
           options_colombia:[
             { id: 'colombia', nombre: 'COLOMBIA'},
             { id: 'colombia/barranquilla', nombre: 'BARRANQUILLA'}, 
             { id: 'colombia/bogota', nombre: 'BOGOTÁ'},
             { id: 'colombia/cali', nombre: 'CALI'},
             { id: 'colombia/medellin', nombre: 'MEDELLÍN'}  
           ],
           options_ecuador:[
             { id: 'ecuador', nombre: 'ECUADOR'},
             { id: 'ecuador/guayaquil', nombre: 'GUAYAQUIL'}, 
             { id: 'ecuador/quito', nombre: 'QUITO'}
           ],
           options_mexico:[
             { id: 'mexico/', nombre: 'MEXICO'},
             { id: 'mexico/acapulco', nombre: 'ACAPULCO'}, 
             { id: 'mexico/aguascalientes', nombre: 'AGUASCALIENTES'},
             { id: 'mexico/chihuahua', nombre: 'CHIHUAHUA'},
             { id: 'mexico/ciudad-juarez', nombre: 'CIUDAD JUAREZ'}, 
             { id: 'mexico/culiacan', nombre: 'CULIACÁN'},
             { id: 'mexico/ecatepec-de-morelos', nombre: 'ECATEPEC DE MORELOS'},
             { id: 'mexico/guadalajara', nombre: 'GUADALAJARA'}, 
             { id: 'mexico/hermosilla', nombre: 'HERMOSILLO'},
             { id: 'mexico/leon', nombre: 'LEON'},
             { id: 'mexico/merida', nombre: 'MERIDA'}, 
             { id: 'mexico/mexicali', nombre: 'MEXICALI'},
             { id: 'mexico/mexico-city', nombre: 'MEXICO CITY'},
             { id: 'mexico/monterrey', nombre: 'MONTERREY'}, 
             { id: 'mexico/morelia', nombre: 'MORELIA'},
             { id: 'mexico/naucalpan-de-juarez', nombre: 'NAUCALPAN DE JUAREZ'},
             { id: 'mexico/nezahualcoyotl', nombre: 'NEZAHUALCOYOTL'}, 
             { id: 'mexico/puebla', nombre: 'PUEBLA'},
             { id: 'mexico/queretaro', nombre: 'QUERETARO'},
             { id: 'mexico/saltillo', nombre: 'SALTILLO'}, 
             { id: 'mexico/san-luis-potosi', nombre: 'SAN LUIS POTOSI'},
             { id: 'mexico/tijuana', nombre: 'TIJUANA'},
             { id: 'mexico/toluca', nombre: 'TOLUCA'}, 
             { id: 'mexico/zapopan', nombre: 'ZAPOPAN'}
           ],
           options_peru:[
             { id: 'peru', nombre: 'PERÚ'},
             { id: 'peru/lima', nombre: 'LIMA'}
           ],
           options_spain:[
             { id: 'spain', nombre: 'ESPAÑA'},
             { id: 'spain/barcelona', nombre: 'BARCELONA'},
             { id: 'spain/madrid', nombre: 'MADRID'},
             { id: 'spain/malaga', nombre: 'MALAGA'},
             { id: 'spain/seville', nombre: 'SEVILLA'},
             { id: 'spain/valencia', nombre: 'VALENCIA'}
           ],
         }
     },
     methods:{
             gettrending(){
              var buscador='';   
               if(this.combo_algeria!=''){
                 $("#combo_argentina").prop('disabled', true);
                 $("#combo_australia").prop('disabled', true);
                 $("#combo_austria").prop('disabled', true);
                 $("#combo_brazil").prop('disabled', true); 
                 $("#combo_chile").prop('disabled', true); 
                 $("#combo_colombia").prop('disabled', true); 
                 $("#combo_ecuador").prop('disabled', true); 
                 $("#combo_mexico").prop('disabled', true); 
                 $("#combo_peru").prop('disabled', true); 
                 $("#combo_spain").prop('disabled', true);         
                 var buscador=this.combo_algeria;
               }else if(this.combo_argentina!=''){
                 $("#combo_algeria").prop('disabled', true);
                 $("#combo_australia").prop('disabled', true);
                 $("#combo_austria").prop('disabled', true);
                 $("#combo_brazil").prop('disabled', true); 
                 $("#combo_chile").prop('disabled', true); 
                 $("#combo_colombia").prop('disabled', true); 
                 $("#combo_ecuador").prop('disabled', true); 
                 $("#combo_mexico").prop('disabled', true); 
                 $("#combo_peru").prop('disabled', true); 
                 $("#combo_spain").prop('disabled', true); 
                 var buscador=this.combo_argentina;
               }else if(this.combo_australia!=''){
                 $("#combo_algeria").prop('disabled', true);
                 $("#combo_argentina").prop('disabled', true);
                 $("#combo_austria").prop('disabled', true);
                 $("#combo_brazil").prop('disabled', true); 
                 $("#combo_chile").prop('disabled', true); 
                 $("#combo_colombia").prop('disabled', true); 
                 $("#combo_ecuador").prop('disabled', true); 
                 $("#combo_mexico").prop('disabled', true); 
                 $("#combo_peru").prop('disabled', true); 
                 $("#combo_spain").prop('disabled', true); 
                  var buscador=this.combo_australia;
               }else if(this.combo_austria!=''){
                 $("#combo_algeria").prop('disabled', true);
                 $("#combo_argentina").prop('disabled', true);
                 $("#combo_australia").prop('disabled', true);
                 $("#combo_brazil").prop('disabled', true); 
                 $("#combo_chile").prop('disabled', true); 
                 $("#combo_colombia").prop('disabled', true); 
                 $("#combo_ecuador").prop('disabled', true); 
                 $("#combo_mexico").prop('disabled', true); 
                 $("#combo_peru").prop('disabled', true); 
                 $("#combo_spain").prop('disabled', true); 
                  var buscador=this.combo_austria;
               }else if(this.combo_brazil!=''){
                 $("#combo_argentina").prop('disabled', true);
                 $("#combo_australia").prop('disabled', true);
                 $("#combo_austria").prop('disabled', true);
                 $("#combo_algeria").prop('disabled', true); 
                 $("#combo_chile").prop('disabled', true); 
                 $("#combo_colombia").prop('disabled', true); 
                 $("#combo_ecuador").prop('disabled', true); 
                 $("#combo_mexico").prop('disabled', true); 
                 $("#combo_peru").prop('disabled', true); 
                 $("#combo_spain").prop('disabled', true); 
                   var buscador=this.combo_brazil;        
               }else if(this.combo_chile!=''){
                 $("#combo_argentina").prop('disabled', true);
                 $("#combo_australia").prop('disabled', true);
                 $("#combo_austria").prop('disabled', true);
                 $("#combo_brazil").prop('disabled', true); 
                 $("#combo_algeria").prop('disabled', true); 
                 $("#combo_colombia").prop('disabled', true); 
                 $("#combo_ecuador").prop('disabled', true); 
                 $("#combo_mexico").prop('disabled', true); 
                 $("#combo_peru").prop('disabled', true); 
                 $("#combo_spain").prop('disabled', true); 
                  var buscador=this.combo_chile;   
               }else if(this.combo_colombia!=''){
                 $("#combo_argentina").prop('disabled', true);
                 $("#combo_australia").prop('disabled', true);
                 $("#combo_austria").prop('disabled', true);
                 $("#combo_brazil").prop('disabled', true); 
                 $("#combo_algeria").prop('disabled', true); 
                 $("#combo_chile").prop('disabled', true); 
                 $("#combo_ecuador").prop('disabled', true); 
                 $("#combo_mexico").prop('disabled', true); 
                 $("#combo_peru").prop('disabled', true); 
                 $("#combo_spain").prop('disabled', true);
                 var buscador=this.combo_colombia;    
               }else if(this.combo_ecuador!=''){
                 $("#combo_argentina").prop('disabled', true);
                 $("#combo_australia").prop('disabled', true);
                 $("#combo_austria").prop('disabled', true);
                 $("#combo_brazil").prop('disabled', true); 
                 $("#combo_algeria").prop('disabled', true); 
                 $("#combo_chile").prop('disabled', true); 
                 $("#combo_colombia").prop('disabled', true); 
                 $("#combo_mexico").prop('disabled', true); 
                 $("#combo_peru").prop('disabled', true); 
                 $("#combo_spain").prop('disabled', true);
                 var buscador=this.combo_ecuador;     
               }else if(this.combo_mexico!=''){
                 $("#combo_argentina").prop('disabled', true);
                 $("#combo_australia").prop('disabled', true);
                 $("#combo_austria").prop('disabled', true);
                 $("#combo_brazil").prop('disabled', true); 
                 $("#combo_algeria").prop('disabled', true); 
                 $("#combo_chile").prop('disabled', true); 
                 $("#combo_colombia").prop('disabled', true); 
                 $("#combo_ecuador").prop('disabled', true); 
                 $("#combo_peru").prop('disabled', true); 
                 $("#combo_spain").prop('disabled', true); 
                  var buscador=this.combo_ecuador;    
               }else if(this.combo_peru!=''){
                 $("#combo_argentina").prop('disabled', true);
                 $("#combo_australia").prop('disabled', true);
                 $("#combo_austria").prop('disabled', true);
                 $("#combo_brazil").prop('disabled', true); 
                 $("#combo_algeria").prop('disabled', true); 
                 $("#combo_chile").prop('disabled', true); 
                 $("#combo_colombia").prop('disabled', true); 
                 $("#combo_ecuador").prop('disabled', true); 
                 $("#combo_mexico").prop('disabled', true); 
                 $("#combo_spain").prop('disabled', true); 
                  var buscador=this.combo_peru; 
               }else if(this.combo_spain!=''){
                 $("#combo_argentina").prop('disabled', true);
                 $("#combo_australia").prop('disabled', true);
                 $("#combo_austria").prop('disabled', true);
                 $("#combo_brazil").prop('disabled', true); 
                 $("#combo_algeria").prop('disabled', true); 
                 $("#combo_chile").prop('disabled', true); 
                 $("#combo_colombia").prop('disabled', true); 
                 $("#combo_ecuador").prop('disabled', true); 
                 $("#combo_mexico").prop('disabled', true); 
                 $("#combo_peru").prop('disabled', true); 
                 var buscador=this.combo_spain; 
               }else{
                 $("#combo_argentina").prop('disabled', false);
                 $("#combo_australia").prop('disabled', false);
                 $("#combo_austria").prop('disabled', false);
                 $("#combo_brazil").prop('disabled', false); 
                 $("#combo_algeria").prop('disabled', false); 
                 $("#combo_chile").prop('disabled', false); 
                 $("#combo_colombia").prop('disabled', false); 
                 $("#combo_ecuador").prop('disabled', false); 
                 $("#combo_mexico").prop('disabled', false); 
                 $("#combo_peru").prop('disabled', false); 
                 $("#combo_spain").prop('disabled', false); 
                  var buscador=''; 
               }

              this.loading = true;
                     axios.get('http://127.0.0.1:8000/search/gettrending',{ 
                            params: { 
                                     buscador: buscador.trim()
                                    }
                        })
                        .then(response=>{ 
                            this.lista=response.data.info_trending;
                            this.loading = false;       
                        })
                        .catch(error=>{
                          console.log(error);
                        })       
           }
     }   
 }
</script>
<style>
.panel-body.div1.table-responsive{
     border: 1px solid #2a3f54;
    -webkit-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
    -moz-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
     box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
} 
</style>