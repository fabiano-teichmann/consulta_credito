# Consulta crédito paciente
Esse projeto vem armazenar e dar acesso a consulta de dividas de clientes.

## Estrutura do serviço

O serviço tem três bases de dados sendo uma base da dados sensíveis, que é armazenado
no mongodb com cpf e nome do cliente criptografado garantido segurança.
A segunda base de dados também é no mongodb sendo os conteúdos indexados para uma maior perfomace do da api se utilizará 
mencached.
A terceira base de dados será construído usando o Redis com mencached para uma grande disponibilidade de dados


