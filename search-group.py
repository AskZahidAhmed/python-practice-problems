import re

search_text = 'srctxt:This is website from id:19987,18675,1678 domainName: xyz.com'

# Extracting text after 'srctxt:'
match = re.search(r'srctxt:(.*)', search_text)
if match:
    text = match.group(1)
else:
    text = ''

# Extracting 'id' value
id_match = re.search(r'id:([\d,]+)', search_text)
if id_match:
    ids = id_match.group(1).split(',')
else:
    ids = []

# Extracting 'domainName' value
domain_match = re.search(r'domainName:\s*([\w.-]+)', search_text)
if domain_match:
    domain_name = domain_match.group(1)
else:
    domain_name = ''

print('Text:', text)
print('ID:', ids)
print('Domain Name:', domain_name)

