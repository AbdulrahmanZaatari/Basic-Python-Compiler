def readFromFile(file_name):
    List=[]
    file = open (file_name, 'r')
    for line in file:
        List.append(line)
    file.close()
    return List

def storeVariables(L):
  new_list=[]
  for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if N[0]=="for":
      new_list.append(N[1])
    elif len(N)==3 or len(N)==5:
      if N[0]!="print" and N[0]!="for" and N[0]!="while":
        new_list.append(N[0])
    elif N[0]=="for":
      new_list.append(N[1])
  return new_list

def oneEqual(L,EL):
   variable_list = storeVariables(L)
   for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if N[0]!="if" and N[0]!="elif" and N[0]!="print":
      if N[0] in variable_list:
        for j in range(len(N)):
          if N[j]=="==":
            EL.append(1)
            print("line", i+1 , ":" , x,)
            print(" \t {You need only one =}")

def floatError(L,EL):
  for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if len(N)==3:
      error=list(N[2])
      if len(error)>=3 and "," in error:
        EL.append(1)
        print("line", i+1 , ":" , x,)
        print("\t {Error, should be replaced by .}")

def multiplicationError(L,EL):
  for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if len(N)==5:
      if N[3]=="x":
        EL.append(1)
        print("line", i+1 , ":" , x,)
        print("\t {you should use * for multiplication}")
        

def equalError(L,EL):
  for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if len(N)==5 or len(N)==3:
      if N[0]!="if" and N[0]!="elif" and N[0]!="print" and N[0]!="for":
        if N[1]!="=":
          EL.append(1)
          print("line", i+1 , ":" , x,)
          print("\t {We should have equal sign}")

def printChecker(L,EL):
  for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if N[0]=="Print":
      EL.append(1)
      print("line", i+1 , ":" , x,)
      print("\t {p should be lowercase}")

      
def variableChecker(L,EL):
  variable_list = storeVariables(L)
  for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if N[0]=="print" and N[2]!="“" and N[2]!='"':
      if N[2] not in variable_list:
        EL.append(1)
        print("line", i+1 , ":" , x,)
        print("\t {variable is not defined}")
    elif len(N)==3:
        if N[0] not in variable_list:
          EL.append(1)
          print("line", i+1 , ":" , x,)
          print("\t {variable is not defined}")
    elif len(N)==5:
      if N[0] in variable_list:
        if N[2] not in variable_list or N[4] not in variable_list:
          EL.append(1)
          print("line", i+1 , ":" , x,)
          print("\t {variable is not defined}")

def ifCondition (L,EL): 
    for i in range (len(L)):
      x=L[i].strip()
      N=x.split(" ")
      if N[0]=="if":
        if N[-1]!=":":
          EL.append(1)
          print("line", i+1 , ":" , x,)
          print("\t {Missing ':'}")
        
def elseCondition (L,EL):
  for i in range (len(L)):
      x=L[i].strip()
      N=x.split(" ")
      if N[0]=="else":
        if N[1]!=":":
          EL.append(1)
          print("line", i+1 , ":" , x,)
          print("\t {else should be replaced by elif}")
        
def elseColon (L,EL):
  for i in range (len(L)):
      x=L[i].strip()
      N=x.split(" ")
      if N[0]=="else":
        if N[-1]!=":":
          EL.append(1)
          print("line", i+1 , ":" , x,)
          print("\t {Missing ':'} ")

def elifCondition (L,EL): 
   for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if N[0]=="elif":
      if N[-1]!=":":
        EL.append(1)
        print("line", i+1 , ":" , x,)  
        print("\t {Missing ':'} ")
      
def fctCheck (L,EL): 
    for i in range (len(L)):
      x=L[i].strip()
      N=x.split(" ")
      if N[0]=="def":
        if N[-1]==":":
          EL.append(1)
          print("line", i+1 , ":" , x,)
          print("\t {Missing ':'} ")
        
def forLoop(L,EL):
  for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if N[0]=="for":
      if N[-1]!=":":
        EL.append(1)
        print("line", i+1 , ":" , x,)
        print("\t {Missing ':'} ")
       

        
def whileLoop(L,EL):
   for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if N[0]=="while":
      if N[-1]!=":":
        EL.append(1)
        print("line", i+1 , ":" , x,)
        print("\t {Missing ':'} ")
        
      
def indentationError(L,EL):
  for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if N[0]=="for" or N[0]=="def" or N[0]=="if" or N[0]=="elif" or N[0]=="else" or N[0]=="while":
      if i!=len(L)-1:
        z=L[i+1].strip("\n")
        M=list(z)
        if M[0]!=" " and M[1]!=" ":
          EL.append(1)
          print("line", i+1 , ":" , x,)
          print("line", i+2, ":" , z)
          print("\t {indentation error}")
  
def typingRange(L,EL):
  for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if N[0]=="for":
      if len(N)>5:
        if N[3]!="range":
          EL.append(1)
          print("line", i+1 , ":" , x,)
          print("\t {syntax error, should be range}")
        
        
def rangeError(L,EL):
  for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if N[0]=="for":
      if len(N)>=9:
        if N[6]!=(','):
          EL.append(1)
          print("line", i+1 , ":" , x,)
          print(" \t {you should put comma in range}")
        
def equalConditionals(L,EL):
    for i in range(len(L)):
       x=L[i].strip()
       N=x.split(" ")
       if N[0]=="if" or N[0]=="elif":
         for i in range(len(N)):
           if N[i]=="=":
             if N[i+1]!="=":
               EL.append(1)
               print("line", i+1 , ":" , x,)
               print ("\t {False, if and elif should have 2 equal signs}")

def notEqualConditionals(L,EL):
    for i in range(len(L)):
       x=L[i].strip()
       N=x.split(" ")
       if N[0]=="if" or N[0]=="elif":
         for i in range(len(N)):
           if N[i]=="!":
             if N[i+1]!="=":
               EL.append(1)
               print("line", i+1 , ":" , x,)
               print ("\t {False, if and elif should have !=}")

def inChecker(L,EL):
  for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if N[-1]==":" and N[0]=="for":
      if N[2]!="in":
        EL.append(1)
        print("line", i+1 , ":" , x,)
        print ("\t {False, in is missing.}")     

def parenthesesChecker(L,EL):
  for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if N[0]=="print":
      if N[-1]!=")" or N[1]!="(":
        EL.append(1)
        print("line", i+1 , ":" , x,)
        print ("\t {Error, be careful about the parentheses!.}")

      
def returnChecker(L,EL):
  for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if N[0]=="Return":
      EL.append(1)
      print("line", i+1 , ":" , x,)
      print ("\t {False, r shouldn't be capitalized.}")

def isPYKW(L,EL):
   for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    if len(N)==3:
      if N[0]=="sum" or N[0]=="pass" or N[0]=="yield" or N[0]=="return" or N[0]=="in":
        EL.append(1)
        print("line", i+1 , ":" , x,)
        print ("\t {You shouldn't a python keyword to a variable.}")

def plusEqual(L,EL):
  for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    for i in range (len(N)):
      if N[i]=="+" and N[i+1]=="=":
        EL.append(1)
        print("line", i+1 , ":" , x,)
        print("\t {no space should be found between + and =}")

def plusEqual2(L,EL):
  for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    for i in range(len(N)):
      if N[i]=="=+":
        EL.append(1)
        print("line", i+1 , ":" , x,)
        print("\t {should be +=}")
        
def missingBrackets(L,EL):
   for i in range (len(L)):
    x=L[i].strip()
    N=x.split(" ")
    for i in range (len(N)):
      if N[i]=="=" and N[i+1]=="[":
        if N[-1]!="]":
          EL.append(1)
          print("line", i+1 , ":" , x,)
          print("\t {missing brackets}")
      elif N[i]=="=" and N[-1]=="]":
        if N[i+1]!="[":
          EL.append(1)
          print("line", i+1 , ":" , x,)
          print("\t {missing brackets}")



def displaySystem():
  print("Please choose 1 of the below options: \n" + "\n" +"1.Display code\n" +"\n"+ "2.Display errors\n" + "\t A.Display error count\n" + "\t B.Return to menu\n" + "\n" + "3.Exit from file\n" + "-----------\n")

def readfile(file):
  
  print("\nEntered file " + file + " succesfully." + "\n")
  List=readFromFile(file)
  
  error_list = []
  
  choice = True
  
  while choice:
    displaySystem()
    option=int(input("Enter an option from the menu:"))
    print()
    
    if option==1:
      for i in List:
       print(i)
    print("-----------\n") 
    if option==2:

      print("Variable list for this file: " , storeVariables(List))
      
      oneEqual(List,error_list)

      floatError(List,error_list)

      multiplicationError(List,error_list)
     
      equalError(List,error_list)
     
      printChecker(List,error_list)

      variableChecker(List,error_list)
     
      ifCondition(List,error_list)
     
      elseCondition(List,error_list)
     
      elseColon(List,error_list)
  
      elifCondition(List,error_list)
  
      fctCheck(List,error_list)

      forLoop(List,error_list)
     
      indentationError(List,error_list)
      
      typingRange(List,error_list)
   
      rangeError(List,error_list)
      
      equalConditionals(List,error_list)

      notEqualConditionals(List,error_list)
      
      inChecker(List,error_list)

      parenthesesChecker(List,error_list)

      returnChecker(List,error_list)

      isPYKW(List,error_list)

      plusEqual(List,error_list)

      plusEqual2(List,error_list)

      print("--------------\n")

      choose=input("Enter A for error count and enter B to return to the menu:")
      print()
      
      if choose=="A":
        print("Error count is:", len(error_list))
        print("--------------\n")
        
      else:
        print("{Dear user, don't run away from your mistakes!}\n" + "\n" + "{Believe in yourself!}\n" + "\n" + "-----------\n")

    if option==3:
      choice=False
      print("we exited file" + file +", see you next time!")
      print("--------------\n")
      

def main():
  
  name=input("Enter your name:")
  print("Hello", name , "!")
  readfile("file1.txt")
  readfile("file2.txt")
  readfile("file3.txt")
  readfile("file4.txt")
main()
 
  

