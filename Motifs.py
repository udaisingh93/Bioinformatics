def Count(Motifs):
    count = {} # initializing the count dictionary
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    profile=Count(Motifs)
    for i in "ACGT":
        for j in range(k):
            profile[i][j]=profile[i][j]/t   
    return profile
def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus
# Output: The score of these k-mers.
def Score(Motifs):
    score=[]
    k = len(Motifs[0])
    t = len(Motifs)
    consensus=Consensus(Motifs)
    print(consensus)
    for i in range(k):
        score.append(0)
        for j in range(t):
            if (Motifs[j][i]!=consensus[i]):
                score[i]+=1
    return sum(score)
# Input:  String Text and profile matrix Profile

# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    p=1
    for i in range(len(Text)):
        p*=Profile[Text[i]][i]
    return p
