# I adapted this code from https://stackoverflow.com/questions/24551023/replace-certain-words-in-a-text-file
content = []
filename='watson.txt'
with open(filename, 'r') as read_file:
	content = read_file.readlines()

with open(filename, 'w') as write_file:
	for line in content:
		# I don't want to have it change Sherlock to John only to have it change right back, so I'll do it in steps
		line = line.replace('Sherlock','a123')
		line = line.replace('SHERLOCK','JOHN')
		line = line.replace('HOLMES','WATSON')
		line = line.replace('Holmes', 'a124')
		line = line.replace('John', 'a125')
		line = line.replace('Watson', 'a126')
		line = line.replace('a126', 'Holmes')
		line = line.replace('a125', 'Sherlock')
		line = line.replace('a124', 'Watson')
		line = line.replace('a123', 'John')
		write_file.write(line)