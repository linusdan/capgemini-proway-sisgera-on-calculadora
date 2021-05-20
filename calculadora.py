#!/usr/bin/env python
#
# SISGERA ON - Sistema de Gerenciamento de Anúncios Online
# Calculadora de alcance de anúncio da agência Divulga Tudo
# Maintainer: Danilo Santos (danilosantos07@protonmail.com)
# versão 20210511 (Codename: Final Countdown)
#
# Algoritmo responsável por calcular a projeção aproximada da quantidade
# máxima de pessoas que visualizarão o mesmo anúncio. 
#
# Ela é definida pelas variáveis:
# 1) alcance_compartilhamento - Váriável onde e definida a multiplicação no qual:
#   1.1) O numero 3 refere-se às pessoas que compartilham nas redes sociais a cada 20 cliques.
#   1.2) 40 é o número de novas visualizações a cada 3 cliques que são gerados a cada compartilhamento nas redes sociais.
#   1.3) 4 é a quantidade máxima de compartilhamentos em sequência a cada 30 visualizações do anúncio original (não compartilhado).
# 2) valor_anuncio - O quanto a agência quer cobrar por anúncio. 
# 3) O preço de anuncio é calculado de acordo com o alcance do anúncio original de 30 pessoas
#    (não compartilhado) a cada R$1 investido, logo R$1 dividido por 30 = R$0.033333333
# 4) valor_investimento - O valor a ser inserido pela pessoa para que a projeção seja feita.
# 5) projecao_anuncio - Mostra o resultado da projeção.

valor_anuncio = 1.00 / 30
alcance_compartilhamento = 3 * 40 * 4

print('''
**************************************************************
** SISGERA ON - Sistema de Gerenciamento de Anúncios Online **
**           Calculadora de alcance de anúncio              **
**************************************************************
    ''')

# Input para entrada do dado do cliente
valor_investimento = float(input("Qual valor a/o cliente deseja investir? (R$) "))

# Fórmula responsável por calcular a projeção do anúncio
projecao_anuncio = valor_investimento * valor_anuncio * alcance_compartilhamento

# Saída de dados da projeção de anúncio
if projecao_anuncio > 1:
    print('A/O cliente terá uma projeção aproximada de', int(projecao_anuncio) ,'pessoas')
else:
    print('A/O cliente terá uma projeção aproximada de', int(projecao_anuncio) ,'pessoa')
