def twosmallword(N,L):
  outputlist=[]  
  sublist=[]
  finallist=[]
  for item in L:
    if (len(item)==N):
      outputlist.append(item)
    if(len(item)<N):
      sublist.append(item)
  #print(outputlist)
  for i in range (0,len(outputlist)):
    k=0
    while k < N:
      if (outputlist[i][:k] in sublist):
        if (outputlist[i][k:] in sublist):
          s1=outputlist[i][:k]
          s2=outputlist[i][k:]
        #print(s1,s2)
        #print(outputlist[i] +" ("+s1+"+"+s2+")")
          finallist.append(outputlist[i] +" ("+s1+"+"+s2+")")
      k +=1

  print(finallist)
  return finallist

N=6
L=["hot", "bird", "dog", "tailor", "hotdog", "or", "if", "tail"]
twosmallword(N,L)
