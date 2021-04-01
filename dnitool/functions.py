
def whois(domain):
    w = classes.WHOISClient()
    return 'OK'#w.whois(domain)


def expiry(domain):
    return None

'''


    class DomainRegistry():
        def __init__(self, domain=None):
            self.registry = None
            self.expiry = None
            self._domain = domain

            # Could add other attributes, eg, name of
            self.query(domain)

        @property
        def domain(self):
            return self._domain

        @domain.setter
        def domain(self, new_domain):
            self._domain = new_domain



        @classmethod
        def
    w = DomainRegistrar()
    print(w.query('github.com'))
'''
