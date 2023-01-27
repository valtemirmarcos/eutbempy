    $(function(){
        $("#btnContinuar").removeClass('disabled');
        $("#idPlano").val(idPlano);
    });

    $(document).on('click','#btnContinuar',function(evt){
       var users = gerarJson("cadastroUsuario");
       var clientes = gerarJson("cadastroCliente");
       var endereco = gerarJson("cadastroEndereco");
        console.log(users);
        console.log(clientes);
        console.log(endereco);
    });
    $(document).on('blur','#email',function(evt){
        validarEmail($(this).val(), '#validaEmail',function(resposta){
            if(resposta){
                console.log('sim');
                $('#email').focus();
            }
        });
    });
    $(document).on('blur','#cpf',function(evt){
        validaCPF($(this).val(),function(resposta){
            if(resposta){
                $("#validaCpf").show().text(resposta);
                $('#cpf').focus();
            }else{
                $("#validaCpf").hide()
            }
        });
    });
    $(document).on('blur','#cep',function(evt){
        buscarCep($(this).val(),function(resposta){
            if(resposta=='cep invalido'){
                $("#validaCep").show().text(resposta);
                $('#cep').focus();
                return ;
            }
            $("#validaCpf").hide();
            $("#endereco").val(resposta.address);
            $("#bairro").val(resposta.district);
            $("#cidade").val(resposta.city);
            $("#uf option[value='"+resposta.state+"']").attr("selected",true);
            console.log(resposta);
        });
    });
    
    