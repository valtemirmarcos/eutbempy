    $(function(){
        carregaAjax(urlGeral+'/listarSegmentos',function(resposta){
            console.log(resposta);
            listarSegmentos(resposta);
        })
    });
    $(document).on('click','.aba-tipo',function(evt){
        evt.stopImmediatePropagation();
        evt.preventDefault();
        $("#btnContinuar").removeClass('disabled');
        $("#btnContinuar").attr('href','/valorCarta?segmento='+$(this).attr('segmento'));
    });
    function listarSegmentos(json){
        var tab='';
            $.each(json,function(index, dado){
                tab+='<div class="col-12 mt-4">';
                tab+='      <ul class="nav nav-tab aba-tipo" segmento="'+dado.segment_code+'">';
                tab+='          <li style="box-shadow: 7px 4px 4px grey;border-radius: 0.5em">';
                tab+='              <a href="#" >'+dado.tipo+'</a>';
                tab+='          </li>';
                tab+='      </ul>';
                tab+='</div>';
            });
        $("#listaSonhos").html(tab);
    }