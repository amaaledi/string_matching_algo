#input validation function
def inputVal(string, pattern):
    sLen = len(string)
    pLen = len(pattern)
    
    #checking fo the length
    while sLen > 20:
        #Getting the user input as a string then coverting it into a list
        string = list(str(input("Input a string with characters less than 20 : "))) #getiing the input string
        sLen = len(string)
    
    while pLen > 30:
        pattern = list(str(input("Input a pattern with characters less than 30 : "))) #getting the input pattern
        pLen = len(pattern)

    #returning the results    
    return string, pattern

#this function is the string matching algorithm
def stringMatcher(string, pattern):
    #variable declaration
    i = 0 #pattern lists indexing variable
    x = 0 #string lists indexing variable
    matched = 0 #this is used to map the matched count
    cantIgnore = False #This is a flag used to check whether the remianing indexes of pattern list can be ignored or not
    canRem = 0 # can remove variable(used to check whether the rest of the pattern list idexes can be removed to match the string)
    cantRem = 0 #cannot remove variable
    sLen = len(string) #length of the string
    pLen = len(pattern)#length of the pattern
    
    #looping to match both lists
    while True:
        if x == sLen: #if the string list reached the max index, program will enter this section
            if i < pLen: #checking if the current index of the pattern list is less than the last index 
                for s in range(i, pLen): #looping through the rest of the index left
                    if i+1 == pLen: #checking whether the pattern has any more indexes left
                        if pattern[i] == "*":
                            canRem+=1 #this will increment so that we can identify whether the inedx can be ignored or not
                        
                        elif pattern[i] == ".":
                            cantRem+=1
                            
                        else:
                            cantRem+=1
                    
                    elif i+1 != pLen:
                        if pattern[i+1] == "*":
                            canRem+=1
                        
                        else:
                            cantRem+=1
                
                if canRem > 0 and cantRem == 0: #canRem should be more than 0 and cantRem must be equal to 0 
                    cantIgnore = False #if above cond is true, cantIgoner flags sets to false
                    break # will breakk the entire loop
                
                elif cantRem > 0:
                    cantIgnore = True
                    break
                
            else:
                cantIgnore = False
                break
                        
        else: #string section not reached the max index, program enter this section
            #if i == pLen: #If pLen reach the max index, but no
                #x+=1
            
            if i == pLen and pattern[i-1] != "*": 
                break
            
            elif string[x] == pattern[i]: #checking both pattern and string index has the same value
                matched+=1 #if both are equal, increase matched by 1
                i+=1  
            
            else:  #if both indexes are not equal, do the following
                
                #this block will check for the special 2 signs given("." , "*")
                if pattern[i] == ".": #check if the patterns current index is equal to "."
                    matched+=1 #if equal, matched will be increased
                    i+=1
                
                elif pattern[i] == "*":  #check if the patterns current index is equal to "*"
                    last = pattern[i-1] #if equal, store the last index value of pattern to variable "last"
                    if last == string[x]:  #check if the "last" variable equal to current string index
                        matched+=1
                        i+=1
                    
                    elif last == ".": #if variable "last" is equal to ".""
                        if i+1 == pLen: #checking i+1 would increase than pLen or not
                            matched+=1
                            
                        elif i+1 > pLen: #if i+1 is greater than pLen. do the following
                            matched+=1
                            i+=1
                            
                        else:
                            if pattern[i+1] == string[x]: #checking if next patern index is equal to the current string index
                                matched+=1
                                i+=2
                            
                            else:
                                matched+=1
                                i+=1
                    
                    elif i+1 < pLen: 
                        
                        #this block is used to ignore the the values with "*" sign in front of it
                        if pattern[i+1] == "*":
                            if pattern[i+2] == string[x]:
                                matched+=1
                                i+=3
                
                #This block is used to check whether last inex value is "*" sign. so that it can repeate the before last index value if the current pattern index does not match"            
                elif i != 0:
                    if pattern[i-1] == "*":
                        b_Last = pattern[i-2]
                        if b_Last == string[x]:
                            matched+=1
                        
                        elif b_Last == ".":
                            matched+=1
                
                #if the last value of the string list is not matched with the current pattern, ot will check if there is next index available on pattern list,
                #and whether it contains a "*" sign, so it could ignore and shift to the next index of the pattern
                    else:
                        if pattern[i+1] == "*":
                            i+=2
                            x-=1
                        
                        #if nothing matches
                        else:
                            break
                
                else:
                        if pattern[i+1] == "*":
                            i+=2
                            x-=1
                        
                        #if nothing matches
                        else:
                            break
  
        x+=1 #increament of the string list control variable
        
    
    #final check whther both string list and pattern has matched successfully      
    if matched == sLen and cantIgnore == False:
        return True
    
    elif matched == sLen and cantIgnore == True:
        return False
    
    else:
        return False



#Main Program
    
string = list(str(input("Input a string : "))) #getiing the input string
pattern = list(str(input("Input a pattern : "))) #getting the input pattern

string, pattern = inputVal(string,pattern) #calling the inputVal function and assigning the results

print(stringMatcher(string, pattern)) #output results and the function call