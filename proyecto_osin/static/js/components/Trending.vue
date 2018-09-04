<template>
<div class="container">
      <div class="row">
          <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
         <div class="form-group">
              <label for="persona">ALGERIA</label>
              <select class="form-control input-sm">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_algeria" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
         <div class="form-group">
              <label for="persona">ARGENTINA</label>
              <select class="form-control input-sm">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_argentina" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
          <div class="form-group">
              <label for="persona">AUSTRALIA</label>
              <select class="form-control input-sm">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_australia" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
         <div class="form-group">
              <label for="persona">AUSTRIA</label>
              <select class="form-control input-sm">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_austria" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
          <div class="form-group">
              <label for="persona">BRAZIL</label>
              <select class="form-control input-sm">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_brasil" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
          <div class="form-group">
              <label for="persona">CHILE</label>
              <select class="form-control input-sm">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_chile" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
           <div class="form-group">
              <label for="persona">COLOMBIA</label>
              <select class="form-control input-sm">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_colombia" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
          <div class="form-group">
              <label for="persona">ECUADOR</label>
              <select class="form-control input-sm">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_ecuador" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
          <div class="form-group">
              <label for="persona">MEXICO</label>
              <select class="form-control input-sm">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_mexico" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
           <div class="form-group">
              <label for="persona">PERÚ</label>
              <select class="form-control input-sm">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_peru" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
           <div class="form-group">
              <label for="persona">ESPAÑA</label>
              <select class="form-control input-sm">
                 <option value="">Seleccione</option>
                 <option v-for="sel in options_spain" :value="sel.id">{{sel.nombre}}</option>
               </select>         
         </div>
         
         
          </div>
          <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
                  
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
          'options_algeria':[
 		     { id: 'algeria', nombre: 'ALGERIA'},
 		     { id: 'algeria/algiers', nombre: 'ALGIERS'}
            ],
           'options_argentina':[
             { id: 'argentina', nombre: 'ARGENTINA'},
             { id: 'argentina/buenos-aires', nombre: 'BUENOS AIRES'},
             { id: 'argentina/cordoba', nombre: 'CÓRDOBA'},
             { id: 'argentina/mendoza', nombre: 'MENDOZA'},
             { id: 'argentina/rosario', nombre: 'ROSARIO'}
           ],
           'options_australia':[
             { id: 'australia', nombre: 'AUSTRALIA'},
             { id: 'australia/adelaide', nombre: 'ADELAIDE'},
             { id: 'australia/brisbane', nombre: 'BRISBANE'},
             { id: 'australia/canberra', nombre: 'CANBERRA'},
             { id: 'australia/darwin', nombre: 'DARWIN'},
             { id: 'australia/melbourne', nombre: 'MELBOURNE'},
             { id: 'australia/perth', nombre: 'PERTH'},
             { id: 'australia/sydney', nombre: 'SYDNEY'}
           ],
           'options_austria':[
             { id: 'austria', nombre: 'AUSTRIA'},
             { id: 'austria/vienna', nombre: 'VIENNA'}, 
           ],
           'options_brasil':[
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
           'options_chile':[
             { id: 'chile', nombre: 'CHILE'},
             { id: 'chile/concepcion', nombre: 'CONCEPCIÓN'}, 
             { id: 'chile/santiago', nombre: 'SANTIAGO'},
             { id: 'chile/valparaiso', nombre: 'VALPARAISO'}
           ],
           'options_colombia':[
             { id: 'colombia', nombre: 'COLOMBIA'},
             { id: 'colombia/barranquilla', nombre: 'BARRANQUILLA'}, 
             { id: 'colombia/bogota', nombre: 'BOGOTÁ'},
             { id: 'colombia/cali', nombre: 'CALI'},
             { id: 'colombia/medellin', nombre: 'MEDELLÍN'}  
           ],
           'options_ecuador':[
             { id: 'ecuador', nombre: 'ECUADOR'},
             { id: 'ecuador/guayaquil', nombre: 'GUAYAQUIL'}, 
             { id: 'ecuador/quito', nombre: 'QUITO'}
           ],
           'options_mexico':[
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
           'options_peru':[
             { id: 'peru', nombre: 'PERÚ'},
             { id: 'peru/lima', nombre: 'LIMA'}
           ],
           'options_spain':[
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
     
     }
     
 }
</script>
<style>

</style>