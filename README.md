# MUTUM-ERP
Bem-vindo à documentação do Mutum ERP, um sistema de planejamento de recursos empresariais modular construído utilizando o framework Django. Este documento fornece uma visão geral da estrutura do projeto, explicando a organização dos aplicativos e a finalidade de cada componente.

Estrutura do Projeto
O Mutum ERP é dividido em vários aplicativos, cada um focado em uma funcionalidade específica. A estrutura principal do projeto (até o momento) é a seguinte:

mutum:                    //Contém os arquivos principais de configuração do Django, incluindo settings.py, urls.py, e outros.
apps:                     //Pasta raiz para todos os aplicativos do projeto.

  common:                 //Contém aplicativos essenciais para o funcionamento interno do sistema.
    common_accounts:      //Gerencia informações de conta e autenticação do usuário.
    common_logging:       //Lida com lógica relacionada a logs do sistema.
    common_notifications: //Gerencia a lógica de notificações do sistema.
    common_utilities:     //Fornece funções de utilidade geral.
    
  pages:                  //Contém aplicativos relacionados às páginas web que os usuários interagem.
    page_home:            //Página inicial do sistema, apresentando informações sobre o ERP e opções para login e registro.
    page_settings:        //Página de configurações da conta e seleção de ferramentas para a área de trabalho.
    page_workspace:       //Área onde o usuário acessa as ferramentas para gerenciar seu negócio.
    
  tools:                  //Contém aplicativos para diferentes ferramentas disponíveis na área de trabalho.
    tool_inventory:       //App da ferramenta de inventário.
    tool_point_of_sale:   //App da ferramenta de ponto de venda.

# Como Executar
-Tenha em seu sistema o python e django (Recomendado: inicie um ambiente virtual com o django instalado);
-Em seu terminal acesse o diretório do mutum;
-Inicialize o servidor utilizando o comando:
  'python manage.py runserver'
-Acesse o link em seu navegador:
  'http://127.0.0.1:8000/'

