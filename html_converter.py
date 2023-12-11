import os
import sys
import markdown

def main(arg):
    command = arg[1]
    inputfile = arg[2]
    outputfile = arg[3]

    if command != "markdown":
        sys.stdout.buffer.write(b"Command not found...\n")
    elif not os.path.exists(inputfile):
        sys.stdout.buffer.write(b"Inputfile not found...\n")
    elif len(arg) != 4:
        sys.stdout.buffer.write(b"Incorrect input!")
    else:
        converter(inputfile, outputfile)

def converter(inputfile, outputfile):
    html = ""

    with open(inputfile, "r", encoding='utf-8') as i:
       html = markdown.markdown(i.read())
    
    with open(outputfile, "w", encoding='utf-8') as o:
        o.write(html)
    

if __name__ == "__main__":
    main(sys.argv)
