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

"Minha base de dados está gigante. O que eu faço?" - Apague a base de dados db.sqlite3. Note que ao fazer isso você vai perder todos os dados gravados. Além disso, você vai ter que reviver a base de dados. Não se preocupe, basta rodar o arquivo "revive_database.bat" que ele deve te salvar.

"Encontrei o erro *'OperationalError at /usuarios/ no such table: app_cad_usuarios_usuario'*. O que eu faço?" - Você deve ter deletado a base de dados e não a reviveu. Rode o arquivo "revive_database.bat" que deve solucionar o problema. 

"Encontrei o erro IntegrityError at /usuarios/ NOT NULL constraint failed: app_cad_usuarios_usuario.nome. O que eu faço?" - Não existe usuário algum na sua base de dados e você tentou acessar o http://127.0.0.1:8000/usuarios/ mesmo assim, né? Esse problema irá desaparecer assim que você cadastrar a primeira pessoa. 

# Changelog:

06/09/2023 - Versão alpha 0001 publicada. É uma cópia do trabalho do Jhonatan de Souza, com alguns arquivos meus pra melhorar a quality of life dos usuários (run.bat e o revive_database.bat). É a versão base para o início do nosso trabalho de extensão.
