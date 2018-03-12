def getContinue():
	finalizar = False
	while not finalizar:
		ans = input('¿Quiere continuar? (s/n) ')
		if ans == s or ans == n:
			finalizar = True
getContinue()