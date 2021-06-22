from collections import namedtuple

STRING_CONSULTA_CREDNET = "p=1234567845678901        B49C      " \
                          "000012345678901FC     FI                   " \
                          "S99SINIAN                               N          "\
                          "                                                   "\
                          "                                                   "\
                          "                                                   "\
                          "                                                   "\
                          "                                                   "\
                          "                                         P002RSPU  "\
                          "                                                   "\
                          "                                                   "\
                          "   I00100RS SRSCP              S                   "\
                          "                                                   "\
                          "                T999 "

retorno_crednet_obj = namedtuple('Retorno_Crednet', 'text')

STRING_RETORNO_CREDNET = retorno_crednet_obj(text="""B49C      000000000000353FC     FI0000200            S99SFIMAN                            SS N                                                                         000000000               00  2014073111041200000016    0017                                                                        0000                    3#
P002RSPU
I00100R
I10501EXISTEM 4 VARIACOES DE GRAFIAS PARA O DOCUMENTO CONSULTADO
I10502JOAO DO TESTE TESTANDO
I10503PAULO RIBEIRO
I10504PTUA TESTE
I10505TESTE FLAG ROUBO
I220002014032520140325000000001000000000015611VSERASA
I110002012060420130401000000003000000002500000SAO PAULO
I2200120140325OO 000000000015611                                    S141156                    0034388471V
I2200200000020140402104955VOUTRAS OPER
I22003              SERASA                                                                                VP
I11001201304010001   000000002500000SPO SPSAO PAULO                              000000201407101708080005624566
I11001201304010001   000000002500000SPO SPSAO PAULO                              000000201407101709170005624567
I11001201206040001   000000000000520SPO SPSAO PAULO                              000000201206041037420005486494
T999000PROCESSO ENCERRADO NORMALMENTE

""")
