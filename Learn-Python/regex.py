import re
str = '<a href="http://www.ptop.se" target="_blank">http://www.ptop.se</a>'
match = re.search(r'href=[\'"]?([^\'" >]+)', str)
if match:
	print match.group(0)
