import re
alternative1 = "Bus Rapid Transit"
alternative2 = "Freeway Tunnel"
alternative3 = "Light Rail Transit"
alternative4 = "No Build"
alternative5 = "ransportation Systems Management/Transportation Demand Management"


inputFile = '/home/liyang/workspace/pydev_test/Tweet710refined.txt'
al1=[]
al2=[]
al3=[]
al4=[]
al5=[]
def generate_5_alternatives(inputFile, outputFile1):
    with open(inputFile,'r') as inputF, open(outputFile, 'w') as outputF:
        for line in inputF.readlines():
            patterns=re.compile(r'\btext Bus\b|\bText Rapid\b')  
              
            if patterns.search(line, re.IGNORECASE): # remove the advertisements
                alt1.append(line)
            else:
                continue
    
         
    print (alt1)     
       
              
    
 