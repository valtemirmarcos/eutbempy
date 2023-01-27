
    $(function(){
        console.log(segmento);
        console.log(carta);
        carregaAjax(urlGeral+'/listarParcelas/'+segmento+'/'+carta,function(resposta){
            listarParcelas(resposta);
            console.log(resposta);
        })
    });

    $(document).on('click','.form-check-label',function(evt){
       
        $("#btnContinuar").removeClass('disabled');
    });

    function listarParcelas(json){
        var tab = '';
            $.each(json, function(index, dado){
                tab +='<div class="form-check mod-custom">';
                tab +='     <input class="form-check-input" type="radio" name="plano1" id="15mil2">';
                tab +='         <label class="form-check-label" for="15mil2">';
                tab +='             35 parcelas de <span>R$ 428,57</span>';
                tab +='         </label>';
                tab +='</div>';
            });
            $("#listarParcelas").html(tab);
    }