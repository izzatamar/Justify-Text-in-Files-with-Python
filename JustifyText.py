import time

actions = input("Enter 'l' to Left Justify || Enter 'r' to Right Justify :")

with open('Paragraph.txt','r') as f:    #Open text file and assign 'f' as its name

    text = str(f.read())     #read text file into a variable
    fileOutput = open('JustifiedParagraph.txt', 'w')

    if (actions =='l'):      #Left Justify
        print('Action: LEFT JUSTIFY')
        justifiedText = text.ljust(80, '*')     #justify using * as space
        print( text.ljust(80, '*'))
        fileOutput.write(justifiedText)
        time.sleep(1)
        print('Left Justification Completed')
        print('Output filename: JustifiedParagraph.txt')


    elif actions == 'r':    #Right Justify
        justifiedText = text.rjust(80, '*')     #justify using * as space
        fileOutput.write(justifiedText)
        time.sleep(1)
        print('Right Justification Completed')
        print('Output filename: JustifiedParagraph.txt')

f.close()                #close f
fileOutput.close()       #close output file