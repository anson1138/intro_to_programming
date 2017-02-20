from __future__ import print_function
"""
open(name[, mode[, buffering]])
so this python documentation, the brackets are misleading. It can be looked at as a list type 
but brackets in docs denote option. so mode and buffering are options b/c
they're in square brackets.

But it's not clear what argument the types should be. so the mode needs type string but it's not clear
in the docs. Although later it puts 'r' around it.

"""
client = open('filename.txt', 'r')
writefile = open('tryme.txt', 'w')

stuff = client.read()
print(stuff, sep='branden',end='this', file=writefile)

client.close()
