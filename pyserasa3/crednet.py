from .constantes import AMBIENTES


class Crednet:
    def __init__(self, login: str, password: str, ambiente: str ='p'):
        self._login = login
        self._password = password
        self._ambiente = ambiente
        if ambiente not in ('p', 'h'):
            self.errors.append(
                "Os ambientes são 'p' de Produção(Padrão) ou "
                "'h' de Homologação!"
            )
        self.errors = []
        if len(login) != 8 or len(password) != 8:
            self.errors.append("Login e password devem possuir 8 números!")

    def _verificar_url_ambiente(self):
        return AMBIENTES[self._ambiente]

    def _get_request_string(self, num_documento):
        """
        Funcao responsavel por buscar a string de conexao dentro da biblioteca
        pySerasa e fazer a chamada da validacao do ambiente de conexao.
        """
        tipo_pessoa_busca = 'F' if len(num_documento) == 11 else 'J'

        string_dados = f"p={self._login}{self._password}        B49C      {num_documento:0>15}{tipo_pessoa_busca}C     FI                   S99SINIAN                               N                                                                                                                                                                                                                                                                                                                  P002RSPU                                                                                                           I00100RS SRSCP              S                                                                                      T999 "

        return string_dados
