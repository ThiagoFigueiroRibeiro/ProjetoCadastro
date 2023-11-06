# Projeto Cadastro (Extensão Estácio)
Repo from our Computer Engineering extension project

A ideia é fazer um site de cadastro usando Django seguindo *exatamente* os mesmos passos do cara do vídeo a seguir: https://www.youtube.com/watch?v=-m5ywU8SW9E e então em cima desse primeiro estudo, montar um segundo site que atenda às necessidades das pessoas do projeto. 

# O que eu preciso pra rodar o código acima?
1 - Python: Baixe e instale no link a seguir: https://www.python.org/downloads/ Depois de instalado, reinicie o pc por garantia.

2 - Django: Pra baixar ele, abra o prompt de comando do Windows (COMO ADMINISTRADOR!) e digite o seguinte código:

    pip install Django
    
Note que você deve fazer isso somente depois de instalar o Python, caso contrário o comando pip não deve funcionar.

3 - Visual Studio Code (Opcional): Eu acredito que seja o editor de código mais adequado pra esse projeto. Baixe e instale aqui: https://code.visualstudio.com/

# Instalei tudo. E aí, como usar o código acima? 
1 - Clique no botão verde lá em cima escrito "Code" e então "Download Zip" pra baixar os arquivos. Extraia eles em algum lugar depois que você baixar eles.

2 - Você vai notar um arquivo chamado "run.bat". Execute ele. Ele vai botar o servidor em execução e vai abrir o seu browser no ip http://127.0.0.1:8000/ lhe mostrando o site. Eu botei pra abrir nesse ip porque é ele que aparece pra mim, mas existe a possibilidade dele abrir em outro ip. Nessa hipótese, copie o ip que aparecer na linha de comando que vocÊ abriu. 

# Problemas que você com certeza vai encontrar

"As cores do site estão esquisitas ou não estão funcionando" - Isso é culpa do CSS. Se você abrir o site em uma janela privativa, esse problema deve ser solucionado.

"Minha base de dados está gigante. O que eu faço?" - Apague a base de dados db.sqlite3. Note que ao fazer isso você vai perder todos os dados gravados. Além disso, você vai ter que reviver a base de dados. Não se preocupe, basta rodar o arquivo "revive_database.bat" que ele deve te salvar.

# Changelog:

19/10/2023 - Versão Beta 0002 publicada. Agora os campos de exibição das fichas está bem bonitinho. Após o cadastro da pessoa, aparece somente o cadastro dela.

16/10/2023 - Versão Beta 0001 publicada. A página de cadastro de nutrição foi ajeitada. Agora ela está mais bonitinha. Foram criadas as páginas de cadastro adulto e infanto juvenil para Psicologia. Falta a de Educação Física e Fisioterapia.

12/10/2023 - Versão Alpha 0007 publicada. Agora a página de nutrição está com os campos de cadastro "prontos", faltando apenas ajeitar o HTML pra o frontend ficar bonitinho. A base de dados está pronta pra receber dados dos campos da nutrição.

05/10/2023 - Versão Alpha 0006 publicada. Todos os cursos já tem as suas próprias páginas e identidades visuais. Essa versão já está pronta pra exibição para os coordenadores dos cursos que vamos nos reunir. 

03/10/2023 - Versão Alpha 0005 publicada. Cada curso terá a sua própria área com suas próprias páginas e identidade visual. Foi feita a atualização da barra de navegação pra mostrar os quartro cursos e foi feito um trabalho inicial para o curso de Fisioterapia. Note que cada curso terá a sua própria pasta pra pegar as informações de html, mas todos os cursos tirarão informações da mesma base de dados.

19/09/2023 - Versão Alpha 0004 publicada. Foi instalado o tema SB Admin, um dashboard padrão do bootstrap. Foi incluído uma página de gráficos que mostra a quantidade de usuários por especialidade. Correção de alguns erros. 

18/09/2023 - Criação de uma página /deletar_usuario/ que você pode deletar um usuário com determinada id da base SQL.

17/09/2023 - Versão alpha 0003 publicada - Agora existe uma página /exibir/ que exibe todos os usuários cadastrados sem a necessidade de adicionar um novo. Existe também uma página /pesquisa/ que você busca um determinado usuário com id_usuario tal e ela exibe os dados somente desse usuário. 

08/09/2023 - Versão alpha 0002 publicada. Foi editado um footer pra o site e correção do espaçamento das informações de cadastro na página principal.

06/09/2023 - Versão alpha 0001 publicada. É uma cópia do trabalho do Jhonatan de Souza, com alguns arquivos meus pra melhorar a quality of life dos usuários (run.bat e o revive_database.bat). É a versão base para o início do nosso trabalho de extensão.

#teste git