# Script to extract .com website names from large text file

with open('websites.txt', 'r') as f:
    lines = f.readlines()

sites = []
for line in lines:
    words = line.split()
    for word in words:
        if word[-4:] == '.com':
            sites.append(word.lower())

with open('test_data.txt', 'w') as f:
    for site in sites:
        f.write(site + '\n')
