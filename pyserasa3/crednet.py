"""
Generates the parser object from the result string from Serasa's webservice
and create this object functionalities.
"""

import requests


from .constantes import AMBIENTES


class Crednet:
    """
    Main class of the Library, this class is responsible for generation the
    python parsing object when receiving the result string from Serasa's
    webservice.
    """
    def __init__(self, login: str, password: str, ambiente: str ='p'):
        self._login = login
        self._password = password
        self._ambiente = ambiente
        self._retorno_original = None
        self.errors = []

        if ambiente not in ('p', 'h'):
            self.errors.append(
                "Os ambientes são 'p' de Produção(Padrão) ou "
                "'h' de Homologação!"
            )

        if len(login) != 8 or len(password) != 8:
            self.errors.append("Login e password devem possuir 8 números!")

    def _verificar_url_ambiente(self):
        """Return the correct URL for the determinate environment"""
        return AMBIENTES[self._ambiente]

    def _get_request_string(self, num_documento):
        """
        Funcao responsavel por buscar a string de conexao dentro da biblioteca
        pySerasa e fazer a chamada da validacao do ambiente de conexao.
        """
        tipo_pessoa_busca = 'F' if len(num_documento) == 11 else 'J'

        string_dados = \
            f"p={self._login}{self._password}        B49C      " \
            f"{num_documento:0>15}{tipo_pessoa_busca}C     FI               " \
            f"    S99SINIAN                               N                 " \
            f"                                                              " \
            f"                                                              " \
            f"                                                              " \
            f"                                                              " \
            f"                                         P002RSPU             " \
            f"                                                              " \
            f"                                I00100RS SRSCP              S " \
            f"                                                              " \
            f"                       T999 "

        return string_dados

    def realizar_busca_serasa(self, num_documento):
        """Request to Serasa's webservice and store inside '_retorno_original"""
        data = self._get_request_string(num_documento)

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        result = requests.post(
            self._verificar_url_ambiente(),
            data=data,
            headers=headers)

        string_dados = result.text

        self._retorno_original = string_dados
