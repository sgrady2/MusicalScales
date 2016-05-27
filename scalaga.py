import random, math

LIST =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
f = open('aga5','a')
tmp = 0




def aga():
    for i in range(10000):
        print(i,"-th SCALL")
        #print
        #print
	
	    #first lets decide how many notes we want this scale to have, randomly of course
	    #sol = sizeoflist
        copy = []
        for b in LIST:  copy.append(b)
        #print("LENGTH COPY",len(copy), copy, LIST, len(LIST))
        sol = 12
        rando = random.uniform(0,1)
        num_notes = int(math.floor(rando*8+1)) 
	    #now we have a random number (uniform random at least) of elements to remove from LIST
	
	    #copy the list so we can always work with our true version
        #copy = LIST
	

        for j in range(num_notes):
        
            #print("Remove",j,"th note  !","OUT OF ",num_notes)
	    #generate random number between 0 and 1
            x = random.uniform(0,1)
        
        #fit the number to the list indices
        
            y = int(math.floor(x*sol))
            #print(y," y<- ->lencopy  ", len(copy), "  sol  ",sol)
            del copy[y-1]
            sol-=1
            
        #copy.append(i)    
        print copy
        nl = [i]
        copy = nl + copy    
        print copy    
        #[i] + copy
        f.write(",".join(repr(e) for e in copy)+'\n')
        #print

    #f.write(",".join(repr(e) for e in copy)+'\n') # python will convert \n to os.linesep

aga()


f.close() # you can omit in most cases as the destructor will call it


