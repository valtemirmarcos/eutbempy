  function carregaAjax(urlApi, callback){
    $.ajax({
            url: urlApi,
            type: 'get',
            dataType: "json",
            contentType: "application/json; charset=iso-8859-1",
            success: function (result) {
                if(result.status!='success'){
                    alert('falha ao carregar os dados');
                }
                callback(result.data);
            },
                error: function (error) {
                console.log(JSON.stringify(error));
                callback(false);
            }

    });
}
function carregaAjaxPost(urlApi,json, callback){
    $.ajax({
            url: urlApi,
            type: 'post',
            dataType: "json",
            data:JSON.stringify(json),
            contentType: "application/json; charset=iso-8859-1",
            success: function (result) {
                if(result.status!='success'){
                    console.log(result);
                    // alert('falha ao enviar os dados');
                    $("#voyager-loader").css('display','none');
                    callback(result);
                }
                callback(result);
            },
            error: function (error) {
                // console.log(JSON.stringify(error));
                // callback(error);
            }

    });
}

function dataGravacao(data) {
    var ardata = data.split("/");

    return ardata[2] + "-" + ardata[1] + "-" + ardata[0];
}

function dataExibicao(data) {
    if(data!=null){
        var ardata = data.split("-");

        return ardata[2] + "/" + ardata[1] + "/" + ardata[0];
    }else{
        return null;
    }

}
function dataFormatada() {
    var data = new Date(),
        dia = data.getDate(),
        mes = data.getMonth() + 1,
        ano = data.getFullYear(),
        hora = data.getHours(),
        minutos = data.getMinutes(),
        segundos = data.getSeconds();
    return [ano, mes, dia].join('-') + ' ' + [hora, minutos, segundos].join(':');
}
function retornaVazio(valor){
    if(valor==null){
        valor='';
    }
    return valor;
}
function formataMoeda(valor, moeda, casasDecimais) {
    valor = valor==null ? 0:valor;
        return parseFloat(valor).toLocaleString(moeda, { maximumFractionDigits: casasDecimais, minimumFractionDigits: casasDecimais });
}


function gerarJson(tipoTabela){
    var arjson = {};
    $('.form-control').each(function(i){
        if($(this).val()!='' || typeof $(this).attr('required') !== "undefined"){
            if($(this).val()=='' && typeof $(this).attr('required') !== "undefined" && $(this).attr('type')=="number"){
                $(this).val('0');
            }
            if($(this).val()=='' && typeof $(this).attr('required') !== "undefined" && $(this).attr('type')!="number"){
                $(".invalid-feedback").eq(i).show().text();
                return;
            }else{
                $(".invalid-feedback").eq(i).hide();
            }
            if (typeof $(this).attr('leitura') === "undefined") {
                if (typeof $(this).attr(tipoTabela) !== "undefined") {
                    var campo = $(this).attr(tipoTabela);
                    var dado = $(this).val().toString();
                    if (typeof $(this).attr('tipo') !== "undefined") {
                        if($(this).attr('tipo')=='moeda'){
                            dado = dado.replace(',','.');
                        }
                        if($(this).attr('tipo')=='moedaInt'){
                            dado = apenasNumeros(dado.replace(',','.'));
                        }
                        if($(this).attr('tipo')=='moedaInt100'){
                            dado = apenasNumeros(dado.replace(',','.'))/100;
                        }
                        if($(this).attr('tipo')=='peso'){
                            dado = dado.replace(',','.');
                        }
                        if($(this).attr('tipo')=='data'){
                            dado = dataGravacao(dado);
                        }
                    }
                    if (typeof $(this).attr('especifico') !== "undefined") {
                        arjson[$(this).attr('especifico')]=dado;
                    }else{
                        arjson[campo]=dado;
                    }
                    
                }
            }
        }
    });
    var json = JSON.stringify(arjson);
    return json;
}
function limparFormulariosDin(tipoTabela){
    console.log(tipoTabela);
    $('.form-control').each(function(i){
        if($(this).val()!=''){
            if (typeof $(this).attr(tipoTabela) !== "undefined") {
                var campo = $(this).attr('id');
                var procuraselect2 = $('#'+campo).hasClass('select2');
                if(procuraselect2){
                    $('#'+campo).val('').select2({
                        placeholder: "Escolha",
                        allowClear: true
                    });
                    $('#'+campo).attr('carregado',0);
                }else{
                    $('#'+campo).val('');
                }
                
            }
 
        }
    });
}
function gerarInputs(tipoTabela, json){
    $('.form-control').each(function(i){
        
            if (typeof $(this).attr(tipoTabela) !== "undefined") {
                var label = $(this).attr('id');
                var campo = $(this).attr(tipoTabela);
                if($(this).attr('tipo')=='moeda'){
                    $("#"+label).val(formataMoedab(json[campo],'pt-BR', 2));
                }else if($(this).attr('tipo')=='moeda100'){
                    $("#"+label).val(formataMoedab(json[campo]/100,'pt-BR', 2));
                }else if($(this).attr('tipo')=='peso'){
                    $("#"+label).val(formataMoedab(json[campo],'pt-BR', 5));
                }else if($(this).attr('type')=='datetime-local'){
                    $("#"+label).val(exibeDataHoraInput(json[campo]));
                }else if($(this).attr('type')=='date'){
                    $("#"+label).val(exibeDataInput(json[campo]));
                }else if($(this).attr('exibe')=='data'){
                    $("#"+label).val(dataExibicao(exibeDataInput(json[campo])));
                }else{
                    $("#"+label).val(removeNull(json[campo]));
                }
                console.log(label+"->"+campo);
            }
        
    });
}
function removeNull(dado){
    return dado==null?'':dado;
}
function formataMoedab(valor, moeda, casasDecimais) {
    valor = valor==null ? 0:valor;
        return parseFloat(valor).toLocaleString(moeda, { maximumFractionDigits: casasDecimais, minimumFractionDigits: casasDecimais }).replaceAll('.', '');
}
function exibeDataHoraInput(data){
    if(data!=null){
        var ardata = data.slice(0,10);
        var arhora = data.slice(11,25);
        return ardata+"T"+arhora;
    }
}
function exibeDataInput(data){
    if(data!=null){
        var ardata = data.slice(0,10);
        return ardata;
    }
}
function formataMoeda(valor, moeda, casasDecimais) {
    valor = valor==null ? 0:valor;
        return parseFloat(valor).toLocaleString(moeda, { maximumFractionDigits: casasDecimais, minimumFractionDigits: casasDecimais });
}
function travarDestravaCampos(tabelaCampos, tarefa){
    $('.form-control').each(function(i){
        if (typeof $(this).attr(tabelaCampos) !== "undefined") {
            var id = "#"+$(this).attr("id");
            $(id).attr('readonly',tarefa);
        }
    });
}
function carregaAjaxToken(urlApi, token, callback){
    
    $.ajax({
            url: urlApi,
            type: 'get',
            headers: token,
            dataType: "json",
            contentType: "application/json; charset=iso-8859-1",
            success: function (result) {
                callback(result);
            },
            error: function (error) {
                console.log(JSON.stringify(error));
                callback(false);
            }

    });
}
function carregaAjaxPostToken(urlApi,json, token,callback){
    $.ajax({
            url: urlApi,
            type: 'post',
            headers:token,
            dataType: "json",
            data:JSON.stringify(json),
            contentType: "application/json; charset=iso-8859-1",
            success: function (result) {
                if(result.status!='success'){
                    console.log(result);
                    // alert('falha ao enviar os dados');
                    $("#voyager-loader").css('display','none');
                    callback(result);
                }
                callback(result);
            },
            error: function (error) {
                // console.log(JSON.stringify(error));
                // callback(error);
            }

    });
}
function iniciaLoading(status){
    if(status){
        $('.tab-loading').html('');
        $('.tab-loading').append('<div class="lds-ring"><div></div><div></div><div></div><div></div></div>');
    }else{
        $('.tab-loading').html('');
    }
}
function formatacaoCampo(){
    // formataMoedaEntradab("input[tipo=moeda]",'','.');
    $("input[tipo=moeda]").mask('0000000000000000000000000000000000000000000000000000,00', {reverse: true}).attr('placeholder','0,00');
    $("input[tipo=peso]").mask('0000000000000000000000000000000000000000000000000000,00000', {reverse: true}).attr('placeholder','0,00000');
    
}
function formatacaoCampoNovo(){
    // formataMoedaEntradab("input[tipo=moeda]",'','.');
    $("input[tipo=moeda]").maskMoney({allowNegative: true, thousands:'.', decimal:',', affixesStay: false});
    $("input[tipo=peso]").maskMoney({allowNegative: true, thousands:'.', decimal:',', affixesStay: false});
    $("input[tipo=moedaInt]").maskMoney({allowNegative: true, thousands:'.', decimal:',', affixesStay: false}).attr('placeholder','0,00');
    $("input[tipo=moedaInt100]").maskMoney({allowNegative: true, thousands:'.', decimal:',', affixesStay: false}).attr('placeholder','0,00');
}
function apenasNumeros(string) 
{
    var numsStr = string.replace(/[^0-9]/g,'');
    return parseInt(numsStr);
}
function vazioEmZero(valor){
    if(valor.length==0){
        return 0;
    }else{
        return apenasNumeros(valor);
    }
}
var strPad = function(i,l,s) {
    if(i!=null){
        var o = i.toString();
        if (!s) { s = '0'; }
        while (o.length < l) {
            o = s + o;
        }
        return o;
    }else{
       return 0; 
    }

};
function validarEmail(email, campoErro,callback){
    var emailFilter=/^.+@.+\..{2,}$/;
    var illegalChars= /[\(\)\<\>\,\;\:\\\/\"\[\]]/
    // condição
    if(!(emailFilter.test(email))||email.match(illegalChars)){
        $(campoErro).show()
        .text('Por favor, informe um email válido.');
        callback(true);
    }else{
        $(campoErro).hide();
        callback(false);
    }

}
function validaCPF(cpf, callback)
{
		cpf = cpf.replace('.','');
		cpf = cpf.replace('.','');
		cpf = cpf.replace('-','');
        var status='';
		erro = new String;
		if (cpf.length < 11) erro += "Sao necessarios 11 digitos para verificacao do CPF! \n\n";
		var nonNumbers = /\D/;
		if (nonNumbers.test(cpf)) erro += "A verificacao de CPF suporta apenas numeros! \n\n";
		if (cpf == "00000000000" || cpf == "11111111111" ||
		    cpf == "22222222222" || cpf == "33333333333" || cpf == "44444444444" ||
            cpf == "55555555555" || cpf == "66666666666" || cpf == "77777777777" ||
            cpf == "88888888888" || cpf == "99999999999"){
			  erro += "Numero de CPF invalido!"
		}
		var a = [];
		var b = new Number;
		var c = 11;
		for (i=0; i<11; i++){
			a[i] = cpf.charAt(i);
			if (i <  9) b += (a[i] *  --c);
		}
		if ((x = b % 11) < 2) { a[9] = 0 } else { a[9] = 11-x }
		b = 0;
		c = 11;
		for (y=0; y<10; y++) b += (a[y] *  c--);
		if ((x = b % 11) < 2) { a[10] = 0; } else { a[10] = 11-x; }
		status = a[9] + ""+ a[10]
		if ((cpf.charAt(9) != a[9]) || (cpf.charAt(10) != a[10])){
			erro +="Digito verificador com problema!";
		}
		if (erro.length > 0){
            callback(erro);
			return false;
		}
        callback(false);
		return true;
}
function buscarCep(cep, callback){
    var erro="";
    cep = cep.replace("-","");
    if(cep.length != 8){
        erro = 'cep invalido';
        console.log(erro);
        callback(erro);
    }else{
        var parte1 = cep.substring(0,5);
        var parte2 = cep.substring(5,8);
        var unificado = parte1+"-"+parte2;
        console.log(parte1);
        console.log(parte2);
        carregaAjax(urlGeral+'/listarEnderecos/'+unificado, function(resposta){
            callback(resposta);
        });
    }
    // 
    
}