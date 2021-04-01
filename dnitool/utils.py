from .config import *
import socket


class WHOISClient:
    '''Documentation'''
    def __init__(self):
        pass

    def __repr__(self):
        '''Return a printable string describing the object.'''
        information = "TBD"
        return information

    def whois(self, domain, host=HOST_IANA):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, PORT))
        s.send((domain + '\r\n').encode())

        response = b""
        while True:
            received = s.recv(2048)
            response += received
            if not received:
                break

        s.close()
        return response.decode()


class CustomException(Exception):
    '''
    Raise an exception with a custom message:
        raise CustomException("Exception message")
    '''
    pass


def cleanup_domain_name(domain):
    '''Clean up the domain name format'''

    domain.replace('http://', '')
    domain.replace('https://', '')
    domain.replace('www.', '')

    # Get only top-level URL.
    n = domain.count('.')
    domain = domain.split('.', n-1)[-1]

    return domain


def _unpack_iana(response):
    '''Get the metadata values from the initial iana WHOIS response.'''
    info = {}
    for line in response.split('\n'):
        if line and line[0] != '%':
            values = line.split(':', 1)
            info[values[0].strip().lower()] = values[-1].strip().lower()
    return info


def _unpack_verisign(response):
    info = {}
    for line in response.split('\n'):
        if line and line[0]==' ':
            values = line.split(':', 1)
            info[values[0].strip().lower()] = values[-1].strip().lower()
    return info


def unpack(response, host=HOST_IANA):
    if host == HOST_IANA:
        return _unpack_iana(response)
    elif host == HOST_VERISIGN:
        return _unpack_verisign(response)
    else:
        return CustomException('Unsupported host.')
