from sys import argv

script, filename = argv

txt = open(ex15_sample.txt)

print "Here's your file %r:" % filename
print txt.read()

print "ex15_sample.txt":
file_again = raw_input("> ")

txt_again = open(ex15_sample.txt)

print txt_again.read()
