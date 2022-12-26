import sys

def main():
    print(lines())

def comments(line):
    return(line.lstrip().startswith('#'))

def docstrings(line):
    if line.lstrip().startswith("'''"):
        return(True)
    else:
        return(False)

def whitespace(line):
    if len(line.lstrip()) == 0:
        return(True)
    else:
        return(False)

def library(line):
    return(line.lstrip().startswith('import'))

def lines():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith('.py'):
            try:
                with open(sys.argv[1], 'r') as file:
                    counter = 0
                    for line in file:
                        if not(comments(line) or docstrings(line) or whitespace(line)):
                            counter += 1
                    return(counter)

            except FileNotFoundError:
                sys.exit('File does not exist')
        else:
            sys.exit('Not a Python file')

    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        sys.exit('Too few command-line arguments')

if __name__ == '__main__':
    main()