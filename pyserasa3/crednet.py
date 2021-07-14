"""
Generates the parser object from the result string from Serasa's webservice
and create this object functionalities.
"""
import requests

from .constantes import ENVIRONMENTS


class Crednet:
    """
    Main class of the Library, this class is responsible for generation the
    python parsing object when receiving the result string from Serasa's
    webservice.
    """
    def __init__(self, login: str, password: str, environment: str ='p'):
        self._login = login
        self._password = password
        self._environment = environment
        self._original = None
        self.errors = []

        if environment not in ('p', 'h'):
            self.errors.append(
                "The environments are 'p' for Production(Default) or "
                "'h' for homologation!"
            )

        if len(login) != 8 or len(password) != 8:
            self.errors.append("Login and password must have 8 numbers!")

    def _check_request_environment_url(self):
        """Return the correct URL for the determinate environment"""
        return ENVIRONMENTS[self._environment]

    def _get_request_string(self, document_num):
        """
        Return the request string with login, password, document number and
        document type and default serasa's configuration.
        """
        document_type = 'F' if len(document_num) == 11 else 'J'

        request_string = \
            f"p={self._login}{self._password}        B49C      " \
            f"{document_num:0>15}{document_type}C     FI               " \
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

        return request_string

    def request_serasa(self, document_num):
        """Request to Serasa's webservice and store inside '_original"""
        data = self._get_request_string(document_num)

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        result = requests.post(
            self._check_request_environment_url(),
            data=data,
            headers=headers)

        result_string = result.text

        self._original = result_string
