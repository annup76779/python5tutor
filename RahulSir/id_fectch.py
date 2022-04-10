import re

text = "//compute.googleapis.com/projects/iac-admin-001/global/firewalls/1177579804082165529"
exp = re.compile(r"(projects\/)([\d\D]+)(\/global)")

match = re.search(exp, text)

print(match.group(2))