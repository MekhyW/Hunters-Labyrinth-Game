import random

def printlabirinto(labirinto, altura, largura):
	for i in range(0, altura):
		for j in range(0, largura):
			if (labirinto[i][j] == 'u'):
				print('\033[0m' + str(labirinto[i][j]), end=" ")
			elif (labirinto[i][j] == 'c'):
				print('\033[92m' + str(labirinto[i][j]), end=" ")
			else:
				print('\033[91m' + str(labirinto[i][j]), end=" ")
		print('\n')

def VaziosEmVolta(rand_parede, labirinto):
	s_vazios = 0
	if (labirinto[rand_parede[0]-1][rand_parede[1]] == 'c'):
		s_vazios += 1
	if (labirinto[rand_parede[0]+1][rand_parede[1]] == 'c'):
		s_vazios += 1
	if (labirinto[rand_parede[0]][rand_parede[1]-1] == 'c'):
		s_vazios +=1
	if (labirinto[rand_parede[0]][rand_parede[1]+1] == 'c'):
		s_vazios += 1
	return s_vazios

def GerarLabirinto(altura, largura, labirinto=[], parede='w', vazio='c', unvisited='u'):
    for i in range(0, altura):
        line = []
        for j in range(0, largura):
            line.append(unvisited)
        labirinto.append(line)

    starting_altura = int(random.random()*altura)
    starting_largura = int(random.random()*largura)
    if (starting_altura == 0):
        starting_altura += 1
    if (starting_altura == altura-1):
        starting_altura -= 1
    if (starting_largura == 0):
        starting_largura += 1
    if (starting_largura == largura-1):
        starting_largura -= 1

    labirinto[starting_altura][starting_largura] = vazio
    paredes = []
    paredes.append([starting_altura - 1, starting_largura])
    paredes.append([starting_altura, starting_largura - 1])
    paredes.append([starting_altura, starting_largura + 1])
    paredes.append([starting_altura + 1, starting_largura])

    labirinto[starting_altura-1][starting_largura] = 'w'
    labirinto[starting_altura][starting_largura - 1] = 'w'
    labirinto[starting_altura][starting_largura + 1] = 'w'
    labirinto[starting_altura + 1][starting_largura] = 'w'

    while (paredes):
        rand_parede = paredes[int(random.random()*len(paredes))-1]
        if (rand_parede[1] != 0):
            if (labirinto[rand_parede[0]][rand_parede[1]-1] == 'u' and labirinto[rand_parede[0]][rand_parede[1]+1] == 'c'):
                s_vazios = VaziosEmVolta(rand_parede, labirinto)
                if (s_vazios < 2):
                    labirinto[rand_parede[0]][rand_parede[1]] = 'c'
                    if (rand_parede[0] != 0):
                        if (labirinto[rand_parede[0]-1][rand_parede[1]] != 'c'):
                            labirinto[rand_parede[0]-1][rand_parede[1]] = 'w'
                        if ([rand_parede[0]-1, rand_parede[1]] not in paredes):
                            paredes.append([rand_parede[0]-1, rand_parede[1]])
                    if (rand_parede[0] != altura-1):
                        if (labirinto[rand_parede[0]+1][rand_parede[1]] != 'c'):
                            labirinto[rand_parede[0]+1][rand_parede[1]] = 'w'
                        if ([rand_parede[0]+1, rand_parede[1]] not in paredes):
                            paredes.append([rand_parede[0]+1, rand_parede[1]])
                    if (rand_parede[1] != 0):	
                        if (labirinto[rand_parede[0]][rand_parede[1]-1] != 'c'):
                            labirinto[rand_parede[0]][rand_parede[1]-1] = 'w'
                        if ([rand_parede[0], rand_parede[1]-1] not in paredes):
                            paredes.append([rand_parede[0], rand_parede[1]-1])
                for parede in paredes:
                    if (parede[0] == rand_parede[0] and parede[1] == rand_parede[1]):
                        paredes.remove(parede)
                continue

        if (rand_parede[0] != 0):
            if (labirinto[rand_parede[0]-1][rand_parede[1]] == 'u' and labirinto[rand_parede[0]+1][rand_parede[1]] == 'c'):
                s_vazios = VaziosEmVolta(rand_parede, labirinto)
                if (s_vazios < 2):
                    labirinto[rand_parede[0]][rand_parede[1]] = 'c'
                    if (rand_parede[0] != 0):
                        if (labirinto[rand_parede[0]-1][rand_parede[1]] != 'c'):
                            labirinto[rand_parede[0]-1][rand_parede[1]] = 'w'
                        if ([rand_parede[0]-1, rand_parede[1]] not in paredes):
                            paredes.append([rand_parede[0]-1, rand_parede[1]])
                    if (rand_parede[1] != 0):
                        if (labirinto[rand_parede[0]][rand_parede[1]-1] != 'c'):
                            labirinto[rand_parede[0]][rand_parede[1]-1] = 'w'
                        if ([rand_parede[0], rand_parede[1]-1] not in paredes):
                            paredes.append([rand_parede[0], rand_parede[1]-1])
                    if (rand_parede[1] != largura-1):
                        if (labirinto[rand_parede[0]][rand_parede[1]+1] != 'c'):
                            labirinto[rand_parede[0]][rand_parede[1]+1] = 'w'
                        if ([rand_parede[0], rand_parede[1]+1] not in paredes):
                            paredes.append([rand_parede[0], rand_parede[1]+1])
                for parede in paredes:
                    if (parede[0] == rand_parede[0] and parede[1] == rand_parede[1]):
                        paredes.remove(parede)
                continue

        if (rand_parede[0] != altura-1):
            if (labirinto[rand_parede[0]+1][rand_parede[1]] == 'u' and labirinto[rand_parede[0]-1][rand_parede[1]] == 'c'):
                s_vazios = VaziosEmVolta(rand_parede, labirinto)
                if (s_vazios < 2):
                    labirinto[rand_parede[0]][rand_parede[1]] = 'c'
                    if (rand_parede[0] != altura-1):
                        if (labirinto[rand_parede[0]+1][rand_parede[1]] != 'c'):
                            labirinto[rand_parede[0]+1][rand_parede[1]] = 'w'
                        if ([rand_parede[0]+1, rand_parede[1]] not in paredes):
                            paredes.append([rand_parede[0]+1, rand_parede[1]])
                    if (rand_parede[1] != 0):
                        if (labirinto[rand_parede[0]][rand_parede[1]-1] != 'c'):
                            labirinto[rand_parede[0]][rand_parede[1]-1] = 'w'
                        if ([rand_parede[0], rand_parede[1]-1] not in paredes):
                            paredes.append([rand_parede[0], rand_parede[1]-1])
                    if (rand_parede[1] != largura-1):
                        if (labirinto[rand_parede[0]][rand_parede[1]+1] != 'c'):
                            labirinto[rand_parede[0]][rand_parede[1]+1] = 'w'
                        if ([rand_parede[0], rand_parede[1]+1] not in paredes):
                            paredes.append([rand_parede[0], rand_parede[1]+1])
                for parede in paredes:
                    if (parede[0] == rand_parede[0] and parede[1] == rand_parede[1]):
                        paredes.remove(parede)
                continue

        if (rand_parede[1] != largura-1):
            if (labirinto[rand_parede[0]][rand_parede[1]+1] == 'u' and labirinto[rand_parede[0]][rand_parede[1]-1] == 'c'):
                s_vazios = VaziosEmVolta(rand_parede, labirinto)
                if (s_vazios < 2):
                    labirinto[rand_parede[0]][rand_parede[1]] = 'c'
                    if (rand_parede[1] != largura-1):
                        if (labirinto[rand_parede[0]][rand_parede[1]+1] != 'c'):
                            labirinto[rand_parede[0]][rand_parede[1]+1] = 'w'
                        if ([rand_parede[0], rand_parede[1]+1] not in paredes):
                            paredes.append([rand_parede[0], rand_parede[1]+1])
                    if (rand_parede[0] != altura-1):
                        if (labirinto[rand_parede[0]+1][rand_parede[1]] != 'c'):
                            labirinto[rand_parede[0]+1][rand_parede[1]] = 'w'
                        if ([rand_parede[0]+1, rand_parede[1]] not in paredes):
                            paredes.append([rand_parede[0]+1, rand_parede[1]])
                    if (rand_parede[0] != 0):	
                        if (labirinto[rand_parede[0]-1][rand_parede[1]] != 'c'):
                            labirinto[rand_parede[0]-1][rand_parede[1]] = 'w'
                        if ([rand_parede[0]-1, rand_parede[1]] not in paredes):
                            paredes.append([rand_parede[0]-1, rand_parede[1]])
                for parede in paredes:
                    if (parede[0] == rand_parede[0] and parede[1] == rand_parede[1]):
                        paredes.remove(parede)
                continue

        for parede in paredes:
            if (parede[0] == rand_parede[0] and parede[1] == rand_parede[1]):
                paredes.remove(parede)
        
    for i in range(0, altura):
        for j in range(0, largura):
            if (labirinto[i][j] == 'u'):
                labirinto[i][j] = 'w'
    for i in range(0, largura):
        if (labirinto[1][i] == 'c'):
            labirinto[0][i] = 'c'
            break
    for i in range(largura-1, 0, -1):
        if (labirinto[altura-2][i] == 'c'):
            labirinto[altura-1][i] = 'c'
            break

    printlabirinto(labirinto, altura, largura)
    return labirinto