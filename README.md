# PRASUNET-CS_01-
Project as a part of PRASUNET internship: Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.
# The Caesar cipher is named after Julius Caesar,
who, according to Suetonius, used it with a shift of three (A becoming D when encrypting, and D becoming A when decrypting) to protect messages of military significance. 
# what is ceaser cipher?
 It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

 # The encryption can also be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A → 0, B → 1, ..., Z → 25.[2] Encryption of a letter x by a shift n can be described mathematically as,[3]

𝐸𝑛(𝑥)=(𝑥+𝑛)mod26.
{displaystyle E_{n}(x)=(x+n)\mod {26}.}
# Decryption is performed similarly,

𝐷𝑛(𝑥)=(𝑥−𝑛)mod26.
{displaystyle D_{n}(x)=(x-n)\mod {26}.}

To write the program that perform subsitution we will take a variable named: SHIFT. This shift tells the compiler upto which characters alphabets should be substituted.

# For example
If you are using right SHIFT to 23 the encoding of all the alphabets will be:
Plain	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
Cipher	X	Y	Z	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W


theory resource from- www.wikipedia.org
