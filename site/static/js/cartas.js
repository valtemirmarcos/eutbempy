    $(function(){
        carregaAjax(urlGeral+'/listarPlanos/'+segmento,function(resposta){
            listarCartas(resposta);
            console.log(resposta);
        })
    });
    $(document).on('click','.carta',function(evt){
        evt.stopImmediatePropagation();
        evt.preventDefault();
        $("#btnContinuar").removeClass('disabled');
        $("#btnContinuar").attr('href','/valorParcela?segmento='+segmento+'&carta='+$(this).attr('valorID'));
    });
    function listarCartas(json){
        var tab='<ul class="nav nav-tab nav-col" id="tabValor">';
            $.each(json, function(index, dado){
                tab += '<li>';
                tab += '    <a href="#" class="carta" valorID="'+dado.values_id+'">'+dado.valor+'</a>';
                tab += '</li>';
            });

            tab += '</ul>';
        $("#listaCartas").html(tab);
                    
    }
