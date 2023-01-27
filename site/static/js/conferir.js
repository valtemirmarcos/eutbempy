    $(function(){
        carregaAjax(urlGeral+'/conferirEscolha/'+idPlano,function(resposta){
            lerPlanos(resposta);
        })
    });
    $(document).on('change','#checkTermos',function(evt){
        evt.stopImmediatePropagation();
        evt.preventDefault();
        if (evt.currentTarget.checked) {
            $("#btnContinuar").removeClass('disabled');
            $("#btnContinuar").attr('href','/cadastro?idPlano='+idPlano);
        }else{
            $("#btnContinuar").addClass('disabled')
        }
    });
    function lerPlanos(json){
        $.each(json, function(index, dados){
            console.log(dados);
            $("#valor-credito").html(formataMoeda(dados.credito_valor,'pt-BR',2));
            $("#valor-mensal").html(formataMoeda(dados.installment,'pt-BR',2));
            $("#valor-contemplado").html(formataMoeda(dados.total_pos_contemplacao,'pt-BR',2));
            $("#qtde-parcelas").html(formataMoeda(dados.parcelas_numero,'pt-BR',0));
            $("#taxa-mensal").html(formataMoeda(dados.taxa_mensal,'pt-BR',2));
        });
    }