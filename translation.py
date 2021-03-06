##############################################
## Name: translation.py			    ##
## Author: Aditya Sakhuja		    ##
## Date: Monday, 20 June 2016		    ##
## Description: Takes as input a character  ##
## and outputs its corresponding 6-bit code ##
##############################################

## Lookup table containing ASCII characters and
## their corresponding 6-bit braille code

ASCIItoBraille = { 'A' : '100000', 'a' : '100000',
		   'B' : '101000', 'b' : '101000',
		   'C' : '110000', 'c' : '110000',
		   'D' : '110100', 'd' : '110100',
		   'E' : '100100', 'e' : '100100',
		   'F' : '111000', 'f' : '111000',
		   'G' : '111100', 'g' : '111100',
		   'H' : '101100', 'h' : '101100',
		   'I' : '011000', 'i' : '011000',
		   'J' : '011100', 'j' : '011100',
		   'K' : '100010', 'k' : '100010',
		   'L' : '101010', 'l' : '101010',
		   'M' : '110010', 'm' : '110010',
		   'N' : '110110', 'n' : '110110',
		   'O' : '100110', 'o' : '100110',
		   'P' : '111010', 'p' : '111010',
		   'Q' : '111110', 'q' : '111110',
		   'R' : '101110', 'r' : '101110',
		   'S' : '011010', 's' : '011010',
		   'T' : '011110', 't' : '011110',
		   'U' : '100011', 'u' : '100011',
		   'V' : '101011', 'v' : '101011',
		   'W' : '011101', 'w' : '011101',
		   'X' : '110011', 'x' : '110011',
		   'Y' : '110111', 'y' : '110111',
		   'Z' : '100111', 'z' : '100111',
		   '1' : '001000', '2' : '001010',
		   '3' : '001100', '4' : '001101',
		   '5' : '001001', '6' : '001110',
		   '7' : '001111', '8' : '001011',
		   '9' : '000110', '0' : '000111',
		   '&' : '111011', '=' : '111111',
		   '(' : '101111', ')' : '011111',
		   '!' : '011011', '*' : '100001',
		   '<' : '101001', '%' : '110001',
		   '?' : '110101', ':' : '100101',
		   '$' : '111001', ']' : '111101',
		   '_' : '010101', '[' : '011001',
		   '/' : '010010', '+' : '010011',
		   '#' : '010111', '>' : '010110',
		   '-' : '000011', '@' : '010000', 
		   '^' : '010100', '.' : '010001', 
		   ';' : '000101', ',' : '000001', 
		   ' ' : '000000', '\n': '000000' }

## Cannot recognise characters:
## '\' : '101101', ''' : '000010', '"' : '000100'

## Function used to translate characters in the main function
def translate(char):
	return ASCIItoBraille[char]
 
