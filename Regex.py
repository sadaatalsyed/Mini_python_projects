import re
# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# r=agentNamesRegex.sub(r'\1****', '''Agent Alice told Agent Carol that Agent
# Eve knew Agent Bob was a double agent.''')
# mo=agentNamesRegex.search('''Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.''')
# print(r)
# print(mo.group())
#---------------------------#
phoneRegex=re.compile(r'''(
(\d{3}|\(\d{3}\))?   # area code xxx or (xxx)
(\s|-|\.)?           # seperator i.e space, dash, or period optional
\d{3}                # first 3 digits
(\s|-|\.)            # seperator
\d{4}                # last four digits
(\s*(ext|ext.|x)\s*\d{2,5})? # extension
)''',re.VERBOSE)

print(phoneRegex.search('122-3452  ext 1222').group())
