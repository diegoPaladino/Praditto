# Sistema de Paragem de Emergência Arduino

## Introdução
Este projeto implementa um sistema de paragem de emergência para uma aplicação Arduino. Utiliza quatro chaves fim de curso e um botão de emergência para pausar a execução do código em qualquer ponto, esperando um comando para continuar ou reiniciar.

## Lista de Materiais Necessários
- Arduino Uno (ou compatível)
- 4 x Chaves fim de curso
- 1 x Botão de emergência
- Cabos de conexão
- Resistor de pull-down, se necessário

## Propósito do Projeto
Este projeto foi criado para oferecer uma camada adicional de segurança em sistemas mecânicos e eletrônicos controlados por Arduino. É ideal para qualquer um que necessite de um método confiável para interromper imediatamente um processo em caso de emergência.

## Prós e Contras
**Prós:**
- Aumenta a segurança do sistema
- Fácil de implementar e modular

**Contras:**
- Dependente da disposição física e da integridade das chaves de fim de curso e botão de emergência

## Orientações Gerais
1. Conecte as chaves fim de curso e o botão de emergência aos pinos especificados no código.
2. Carregue o código para o seu Arduino.
3. Inicie a comunicação serial para enviar comandos de continuação ('A') ou reinício ('B').

## Licença
Este projeto está sob a licença MIT. Sinta-se livre para modificá-lo, distribuí-lo e usá-lo conforme necessário.
