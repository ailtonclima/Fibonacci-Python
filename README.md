Explicação do Código:

Função pertence_fibonacci:

Recebe um número como parâmetro.
Inicializa as duas primeiras variáveis da sequência (a e b) com 0 e 1.
Enquanto a variável a for menor ou igual ao número informado:
Se a for igual ao número, retorna True (o número pertence à sequência).
Calcula o próximo número da sequência e atualiza as variáveis a e b.
Se o loop terminar sem encontrar o número, retorna False (o número não pertence à sequência).
Entrada do usuário:

A linha numero = int(input("Digite um número: ")) permite que o usuário digite um número, que é convertido para um inteiro e armazenado na variável numero.
Chamada da função e impressão do resultado:

A função pertence_fibonacci é chamada com o número informado pelo usuário.
O resultado da função é utilizado para imprimir uma mensagem informando se o número pertence ou não à sequência.
Como usar:

Salve o código em um arquivo Python (por exemplo, fibonacci.py).
Execute o arquivo no seu terminal ou ambiente de desenvolvimento Python.
Digite o número que você deseja verificar ao ser solicitado.
O programa irá imprimir a mensagem indicando se o número pertence ou não à sequência de Fibonacci.
Observações:

Eficiência: Este código é eficiente, pois utiliza um loop while para gerar os números da sequência até encontrar o número informado ou ultrapassá-lo.
Flexibilidade: Você pode modificar a função para retornar a sequência completa até um determinado número, ou para encontrar o índice de um número na sequência.
Outras linguagens: O mesmo algoritmo pode ser implementado em outras linguagens de programação, como C++, Java, JavaScript, etc.
