
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
        $("#btnContinuar").attr('href','/conferir?idPlano='+$(this).attr('idParcela'));
        console.log($(this).attr('idParcela'));
    });

    function listarParcelas(json){
        var tab = '';
            $.each(json, function(index, dado){
                tab +='<div class="form-check mod-custom">';
                tab +='     <input class="form-check-input" type="radio" name="plano1" id="'+dado.id+'">';
                tab +='         <label class="form-check-label" idParcela="'+dado.id+'" for="'+dado.id+'">';
                tab +='             '+dado.parcelas_numero+' parcelas de <span>R$ '+formataMoeda(dado.installment,'pt-BR',2)+'</span>';
                tab +='         </label>';
                tab +='</div>';
            });
            $("#listarParcelas").html(tab);
    }