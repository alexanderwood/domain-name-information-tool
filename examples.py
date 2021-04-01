from dnitool import expiry, whois

# Example 1: Print the domain expiraiton date to a file
# for 1,000 example domains.
with open('test/test_data.txt', 'r') as f:
    lines = f.readlines()

with open('data/test_output.txt', 'w') as f:
    for line in lines:
        domain = line.strip()
        exp_date = expiry(domain)
        whitespace = " " * (50 - len(domain))
        f.write("{}{}{}\n".format(domain, whitespace, exp_date))


# Example 2: Print the WHOIS database information for a single
# example.
info = whois('mathprofessorquotes.com')
for k, v in info.items():
    print("{}: {}".format(k, v))
