
<br />
<p align="center">
  <h1 align="center">Domain Name Information Tool</h1>
  <p align="center">
    Accessing the WHOIS service with Python
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
## About The Project

The Domain Name Information (DNI) Tool is a Python tool for utilizing the WHOIS service without using the `whois` command line utility.

The WHOIS service is a public directory containing information on registered domain name registrants that uses TCP port 43. The WHOIS protocol is the generally accepted standard for querying domain information. The eponymously named UNIX command line utility `whois` is often used to make WHOIS queries. This module sidesteps this utility.

The DNI Tool currently supports requests for `.com` domains and can return the entire record for the site or just the date of domain expiry. Future versions may incorporate requests for additional specific information and additional top-level domains.


<!-- GETTING STARTED -->
## Getting Started

To use this tool locally follow these steps.

### Prerequisites

This tool works with Python 3.6+.

### Installation

1. Clone the hydrate-tweets-api-v2
```sh
git clone https://github.com/alexanderwood/domain-name-information-tool.git
```
2. Import the functions as the `dnitool` module.
```py
import dnitool
```
If the module is not in your search path, then you can use [`importlib.util`](https://docs.python.org/3/library/importlib.html#module-importlib.util) (Python 3.5+), or:
```py
import sys
sys.path.append('/foo/bar/dni-tool')
import dnitool
```



<!-- USAGE EXAMPLES -->
## Usage

This tool provides two functions: `whois` and `expiry`. The `whois` function returns a `dict` containing information from the WHOIS registry. The `expiry` function returns the domain's expiration date as a `datetime` object.

```python
from dnitool import whois, expiry

domain = 'mathprofessorquotes.com'
info = whois(domain)
exp_date = expiry(domain)
```

For more examples, see `examples.py`.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Alexander Wood - [@woodalexandern](https://twitter.com/woodalexandern) - [website](https://alexanderwood.github.io)

Project Link: [https://github.com/alexanderwood/hydrate-tweets-api-v2](https://github.com/alexanderwood/domain-name-information-tool)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/alexanderwood/hydrate-tweets-api-v2.svg?style=flat-square
[contributors-url]: https://github.com/alexanderwood/hydrate-tweets-api-v2/graphs/contributors
[license-shield]: https://img.shields.io/github/license/alexanderwood/hydrate-tweets-api-v2.svg?style=flat-square
[license-url]: https://github.com/alexanderwood/hydrate-tweets-api-v2/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/woodalexandern
[product-screenshot]: images/screenshot.png

# Domain Name Tool
