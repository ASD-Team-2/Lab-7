class String():
    def __init__(self,string):
        self.string=string
    def search(self,word):  #lconst is the large constant used to limit the maximum hash value
        s=self.string.lower()
        word = word.lower() 
        CONST = 26 #The constant for base system 26
    
        wordhash = 0    #For the pattern
        thash = 0 #For each substring
        for i in range(len(word)):
            wordhash += ((ord(word[i])-ord('A')+1)*(CONST**(len(word)-i-1)))
            thash += ((ord(s[i])-ord('A')+1)*(CONST**(len(word)-i-1)))
        for index in range(len(s)-len(word)+1):
            if index!=0:
                thash = (CONST*(thash-((ord(s[index-1])-ord('A')+1)*(CONST**(len(word)-1))))+((ord(s[index+len(word)-1])-ord('A')+1)))
  
            if(thash==wordhash):
                i,j = 1,index+1
                while(i<len(word)):
                    if s[j]!=word[i]:
                        break
                    i += 1
                    j += 1
                else:
                    return index

if __name__ == '__main__':
    string=String("Just a text string, no more")
    print("Index of string:",string.search("string"))
    print("Index of string:",string.search("r"))
    print("Index of string:",string.search("no"))
    
    
