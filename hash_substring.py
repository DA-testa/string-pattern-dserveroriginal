# python3
# author: 221RDB047

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    mode= input().rstrip().lower() 
    if mode=='i':
        return (input().rstrip(), input().rstrip())
    else:
        with open("tests/06") as file:
            try:
                return (file.readline().rstrip(), file.readline().rstrip())
            except:
                return ('','')
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))
    
def get_hash(pattern: str):
    # this function returns hash of pattern
    
    result=0
    for index in range(len(pattern)):
        result*=13
        result+=ord(pattern[index])
        result%=256
    
    return result

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    
    result=[]
    
    for index in range(len(text)-len(pattern)+1):
        if get_hash(text[index:index+len(pattern)])==get_hash(pattern):
            if text[index:index+len(pattern)]==pattern:
                result.append(index)
    
    if result == []:
        result.append(-1)
    
    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

