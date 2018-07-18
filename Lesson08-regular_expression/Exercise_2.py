import re

text1 = " and cookie"
text2 = "CakeCakeCake and cookie"

# Define pattern
plus_pattern = "(Cake)+ and cookie"

# search pattern in texts # 
plus_match1 = re.search(plus_pattern, text1)
plus_match2 = re.search(plus_pattern, text2)

# check
print(plus_match1)
print(plus_match2.group())

# text which re applies to
name1 = raw_input("Enter name1:")
name2 = raw_input("Enter name2:")
name3 = raw_input("Enter name3:")

# specify pattern
pattern =r'(?P<first_name>\w\w\w) (?P<last_name>\w{4})'

# search pattern
match1 = re.search(pattern, name1)
match2 = re.search(pattern, name2)
match3 = re.search(pattern, name3)

# Check
print "Tom Tsai:",match1.groupdict()
print "Amy Wang:",match2.groupdict()
print "Time Chen:",match3.groupdict()


#print "Tom Tsai:",match1.groupdict()
#print "Amy Wang:",match2.groupdict()
#print "Time Chen:",match3.groupdict()




