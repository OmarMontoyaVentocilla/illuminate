<template>
<div class="container">
      <div class="row">
         <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
              <div class="form-group" >  
                <label for="buscador" class="bmd-label-floating">Metabuscador</label>
                <input type="text" class="form-control" name="buscador" id="buscador" v-model="buscador"  autocomplete="off">
             </div>
              <div class="form-group">
                <button class="btn btn-raised btn-primary" type="button" v-on:click.prevent="gethas()"><i class="fa fa-search"></i> Buscar</button>
            </div> 
         </div>
       </div>
       <div class="row">
           <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
              <div v-html="saludo"></div>
           </div>            
       </div>
        <div class="row">
           <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
              <div v-html="saludo2"></div>
           </div>            
       </div>
</div>
</template>
<script>
 export default{
     created(){
        this.gethas();
     },
     data(){
         return{
           'saludo':'',
           'saludo2':'',
           'buscador':''
         }
     },
     methods:{
      gethas(){
          var buscador=this.buscador;
          if(buscador!=''){
              
          //var src="https://duckduckgo.com/?q="+buscador+"&t=h_&ia=web";
          var src="https://yippy.com/search/?v%3Aproject=clusty-new&query="+buscador+"&xtoken=17154132715bc7682277771";

          var src2="http://www.webcrawler.com/serp?q="+buscador+"&sc=yfOGxTff5dsaZIB8n5GmPeDAGlkcvoWSz5Sx59OcDrmZCR9cxp8Fb6-cw7EJXR8G2NVhHi3szXBRLiCWEU9GchPT9vSh3N12Am2b9-YcJusTxkxDIY2JUq93WQX0MZzCHt8rdnhnwYgsbKFOnJNdl5hk5XEzdATwAyaBiMaWRLDMvFLKVzQ5ZRm_9Bb2Fv_TSUyNscesDg7lirijew0HmjXtFpumAC_DazzysImMici20MggdUV-RUISWIvkxgw2GOo-aCn4hYCrD4cEaI5v8bzcVnj0mpMKbX4fixzfZ-liFaLH6OjHXNchRmJVSeeceC2hgvF2CeRPuXH_cQbNwzuGkh6iHQ-GElSrhoMdxU84rvIh3-2UrW1DtmyxjoZ1-0yrnoIEwUvoz56EMG1sH7EikXIZ_akE6tesEOj0bo8tyhI-jk8ZN4zjiV1tHaNxBws2_k4LTDr-YTWweCl6OTGV41Y7ap9KgX4M0rRugKFmP0VYg4IXnLES2RrqzvRsI-QZETMh7oK7twNuKIAvVbSssn5RWCugIdewGMs2Fz2t-xYvUP9jcQobsoOsavpXR-hTR5MlMK9tIJjjoqb_kn9r2Bbk5u6bCJhBSUitKXGfC2rbMK0ZKdUXmQONFnhXdC_580My6Jib8Hu7pXPOdkiaxInulKtMv02lOThKNvpcQcg4QJLGcQFnVy_KUzSYW6WXf47CISqBzDJMOVjYLSPogr2ZHus73fR0JvwqVn3sKdGwZxm8H0A23Hi8wpgDRzUSdA3zmzzA4kXcbxhRwW_-Z0YCEjcz2ofptvKrx3ylZkzTQ4wqg_rmB1v0JYJBlllIMmdj8km4797HVfHjaqJmkh5AYKPpZnGAF41znvszpyANVSlvMThggI4nT-gfkc_7KtoONgm8UgNbXejY88T4_vuk3Htb-rMtObQzrPWB-4ug-zUy-tLzBs1xTsDMC_h-HTdHLUlRlG0IGnpQNi2tuE-3Ykr3VFtw0EikiPNNTdv4CJ5ytg60Bzs47sz3QppggaN3g4EpqR6F4xqB4wihNZHBpXJh9R9s4uNwLjMjfEwd8l1GTrBGuUv28ZKCGVz1gV2kYhlj_8yBk78C-e8kqfQpcZZPcB29XRycTkCJOa4yWN4tbPabT2JSy8H-TxMEDwbNPURL3ClHhh2bPuTazPzRxjrZAfQM5xtbyxFKeDrHH6gCGg72tRH2rg8l-PNSaQlEyC3aeolj5lZvDQyg1WpMGSSAiSQfDfTN3ixuBUDOmU484hqhTfmkH6NbImfXH8RGeAayIqdg5-FfSvJvLTYY56OJqGWqPk1V_nzB4jEN5my_rlirULSit_lQyfuYVXgVoEzRZ_DXRfq2akGsZyXGdUM5b2t8r_HdZeyy3Xvr_KpBECf3JAavEe0wEp9t8oaS-M0nkDlgZjD-yNVdFaBHpWBcM3AKQvXi3bu0MIHMB-uJMSWk645zdFc95PR1aKMHaIsY4mq6PKuz8USTXhoEpHK0VbGFzeGrecWCumSgh0JJR-opnYNTOJH74O15v64YwKermc2tWwYWLsd0dp4G0ru2mKC9FMU9mtKozRXJFgpqP7ourW98soUU-2QdoZe1Rr9Bpj4aexJzagOw3Th2RtW_-j6uBRHdFg"
          //var url_as=window.open(src);
          var url_as='<iframe src="'+src+'" width="100%" height="1200"></iframe>';

          var url_as2='<iframe src="'+src2+'" width="100%" height="1200"></iframe>';
          this.saludo=url_as;
          this.saludo2=url_as2;
          }else{
           this.saludo=''; 
           this.saludo2='';  
          }
          var arrreglo=[this.saludo,this.salud2];
          return arrreglo;  
      }
     }
     
 }
</script>
<style>
.popupWrap>p>a>img{
    display:none;
}
</style>