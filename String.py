class String():
    def __init__(self,string):
        self.string=string
    def __str__(self):
        return self.string
    def search(self,word):
        s=self.string
        CONST = 26
        wordhash = 0
        thash = 0 
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
        return -1
                        
    def replace(self,word,rep):
        s=self.string
        CONST = 26
        wordhash = 0
        thash = 0 
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
                    replacements = {word:rep}
                    words=s.split(" ")
                    self.string=(' '.join(map(lambda w: replacements.get(w, w), words)))
                    return True
        return False
if __name__ == '__main__':
    string=String("Just a text String and no more")
    print(string)
    print("Index of String:",string.search("String"))
    print("Index of r:",string.search("r"))
    print("Index of no:",string.search("no"))
    print("Index of Next:",string.search("Next"))

    string.replace("text","replace")
    print(string)
    print("Index of string:",string.search("replace"))
