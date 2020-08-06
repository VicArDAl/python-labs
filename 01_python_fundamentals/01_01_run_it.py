'''
1 - Write and execute a script that prints "hello world" to the console.

2 - Using the interpreter, print "hello world!" to the console.

3 - Explore the interpreter.
	a - Execute lines with syntax error and see what the response is.
        * What happens if you leave out a quotation or parentheses?
        * How helpful are the error messages?
	b- Use the help() function to explore what you can do with the interpreter.
        For example execute help('print').
        press q to exit.
	c- Use the interpreter to perform simple math.
	d- Calculate how many seconds are in a year.

'''
#1
print("hello world")

#3.a
# leave out parenthesis
# print(hello world)
# When I run the program, it says that there is a SytaxError
# It's very helpful because it shows in which line is the problem

#3.b
#Shows a description of what the command does.
help(print)

#3.c
5+4
print(5+4)



#3.d
sec = 60
min=60
hour=24
day=365
year=sec*min*hour*365
print(year)
