#NOTE: String is immutalbe (we cannot change).

#single and double quote

st1="Gutti's laptop"
st2='Gutti"s laptop'
print(st1)
print(st2)

# single and double quote at a time in single string

st3='Akash\'s "laptop"'
print(st3)

#In python "\n" there is special meanig for enter (next line) for value.

print("Akash\nGutti")

#if we use "\\" then it will consider as single "\".

print("Akash\\nGutti")

#if we use "r" before the string it will consider as RAW string.

print(r"Akash\\nGutti")

#if I want to do string concatination (adding).

print("Akash"+"_"+"Gutti")

#array in python

st4="Akash Gutti"

print(st4[2])
print(st4[0:7])
print(st4[4:])
print(st4[:6])
print(st4[:-6])
print(st4[-5:])

#length function in python

st5=len(st4)

print(st5)