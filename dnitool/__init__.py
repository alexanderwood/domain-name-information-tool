from .utils import *
import sys
from datetime import datetime

if sys.version_info < (3, 6):
    CustomException('Please use Python version >= 3.6')


def whois(domain):
    """
    Returns the WHOIS response for the given domain.

    The default WHOIS server is whois.iana.org.
    If IANA returns a more authoritative server for the
    query, then the protocol is run again with the new server.


    Parameters
    ----------
    domain : str
        The domain name. Currently stable only for .com addresses.

    Returns
    -------
    dict
        A dictionary of the key, value pairs returned by the data request.

    """

    # Query IANA.
    w = WHOISClient()
    domain = cleanup_domain_name(domain)
    response = unpack(w.whois(domain))

    # Re-query if IANA refers to a different host
    if 'whois' in response:
        host = response['whois']
        response = w.whois(domain, host=host)
        response = unpack(response, host)

    return response


def expiry(domain):
    """
    Returns the expiration date for the given domain.

    Calls the whois function and parses the response. Returns only the expiry
    date for the given domain name.

    Parameters
    ----------
    domain : str
        The domain name. Currently stable only for .com addresses.

    Returns
    -------
    datetime
        A Python datetime object.

    """
    response = whois(domain)
    for k, v in response.items():
        if any(keyword in k for keyword in KEYWORD_EXPIRE):
            return datetime.strptime(v, '%Y-%m-%dt%H:%M:%Sz')
    return None
