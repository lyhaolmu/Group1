import re

    
def delete_lines(inputFile, outputFile):
    count = 0
    with open(inputFile,'r') as inputF, open(outputFile, 'w') as outputF:
        for line in inputF.readlines():
            if count%2 == 0:
                if not re.search('nail', line): # remove the advertisements
                    thisIsAD = False
                    
                    outputF.writelines(line)
                    
                else:
                    thisIsAD = True
                    print line
                    
            else:      
                if thisIsAD:  
                    print line
                    
                else:
                    outputF.writelines(line)  
            count+=1

inputFile = '/home/liyang/workspace/pydev_test/tweet&710'               
delete_lines(inputFile, 'Tweet710refined.txt')  # or you pass any line number

