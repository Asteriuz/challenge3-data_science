# Dicionário de Dados (Dataset fornecido)
| Variável                    | Tipo       | Descrição                                                                                   |
|-----------------------------|------------|---------------------------------------------------------------------------------------------|
| unidade                     | categórica | Nome da unidade de atendimento Dasa (ex: Unidade A, Unidade B, ...)                         |
| mes                         | categórica | Mês/ano da observação (ex: jan/2025)                                                        |
| tipo_exame                  | categórica | Tipo principal de exame realizado (sangue, urina, imagem, genético, covid, hormonal, alergia)|
| pacientes_dia               | numérica   | Número médio de pacientes atendidos por dia                                                  |
| exames_realizados           | numérica   | Número total de exames processados na unidade no mês                                         |
| turno_mais_movimentado      | categórica | Turno com maior movimento (manhã, tarde, noite)                                              |
| temp_medio_exame            | numérica   | Tempo médio para realização do exame, em minutos                                             |
| protocolo_emergencia        | categórica | Indica se houve protocolo de emergência no período (sim/não)                                 |
| direcao_centrifuga          | categórica | Direção em que a centrífuga principal está voltada (leste, oeste, norte, sul)                |
| quantidade_refrigeradores   | numérica   | Quantidade de refrigeradores presentes no laboratório (1 a 4)                                |
| alinhamento_refrigeradores  | categórica | Arranjo dos refrigeradores no espaço (lado_a_lado, em_L, dispersos)                          |
| cor_parede_laboratorio      | categórica | Cor predominante da parede do laboratório (laranja, azul, verde, etc.)                       |
| cor_parede_coleta           | categórica | Cor da parede da sala de coleta (branca, amarela, azul_cobalto, laranja, roxa, verde)        |
