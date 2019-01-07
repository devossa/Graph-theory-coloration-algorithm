from json import loads

def getDegree(D):
    degree = {}
    sorted_degree = {}
    for k in Sommets(D):
        if k in D.keys(): degree[k] = len(D[k])
        else: degree[k] = 0
    for key in sorted(degree, key=lambda x: -degree[x]):
        sorted_degree[key] = degree[key]
    return sorted_degree

def Sommets(D):
    s=[]
    for k in D:
        if k not in s: s.append(k)
        for i in D[k]:
            if i not in s: s.append(i)
    return s
   
def FullGraph(G):
	fg = {}
	for sommet in G:
		fg[sommet] = G[sommet]
		for succ in G[sommet]:
			if succ not in fg:
				if succ not in G:
					fg[succ] = []
				else:
					fg[succ] = G[succ]
	return fg

def ordre_pgsg_complet(D):
    graphes_complets = []
    for sommet in getDegree(D):
        sommets = [sommet]
        updated = True
        for pt in D:
            if sommet in D[pt]: sommets.append(pt)
        while len(sommets) > 2 and updated:
            for s in sommets:
                updated = False
                for j in sommets[:sommets.index(s)]+sommets[sommets.index(s)+1:]:
                    if s not in D[j]:
                        sommets.remove(s)
                        updated = True
                        break
        graphes_complets.append(sommets)
    pgsg = max(graphes_complets, key=lambda x:len(x))
    return len(pgsg) if len(pgsg) > 2 else False
    

def Coloration(D):
    deg = getDegree(D)
    s = Sommets(D)
    Colors = {}
    current_color = 1
    for sommet in deg:
        if sommet not in Colors: Colors[sommet] = "C"+str(current_color)
        for sommet2 in s:
            if sommet in D and sommet2 not in D[sommet] and sommet2 not in Colors:
                Colors[sommet2] = "C"+str(current_color)
        if "C"+str(current_color) in Colors.values(): current_color +=1         
    return Colors


def nbre_chromatique(D):
    col = len(set(Coloration(D).values()))
    max_len_graphe_complet = ordre_pgsg_complet(FullGraph(D))
    if col == max_len_graphe_complet or max_len_graphe_complet == False: return "le nombre chromatique est: " + str(col)
    else: return "La coloration realiser n'est pas optimale"

# imput like this: {"a": ["c"], "b": ["c","d"], "c": ["a", "b", "d"], "d": ["c", "b", "e"], "e": ["d"]}
x=input('Entrer un graph')
G = loads(x.replace("'", '"'))
print('Coloration trouvée:',Coloration(G))
print(nbre_chromatique(G))
