import sys

def camelCasing(code):
    # Write your code here
    
    if code[0] == 'S':
        if code[1] == 'V':
            #S;V;pictureFrame -> picture frame
            variable = code[2]
            index_of_capitals = [variable.index(letter) for letter in variable if letter.isupper()]
            result = ''
            prev_idx = 0
            for curr_idx in index_of_capitals:
                if curr_idx>0:
                    result += ' ' + variable[prev_idx:curr_idx].lower()
                    prev_idx = curr_idx
                    
                if curr_idx == index_of_capitals[-1]:
                    result += ' ' + variable[curr_idx:].lower()
                
            return result.ltrim()
        
        elif code[1] == 'C':
            #S;C;LargeSoftwareBook -> large software book
            variable = code[2]
            index_of_capitals = [variable.index(letter) for letter in variable if letter.isupper()]
            result = ''
            prev_idx = 0
            for curr_idx in index_of_capitals:
                if curr_idx>0:
                    result += ' ' + variable[prev_idx:curr_idx].lower()
                    prev_idx = curr_idx
                    
                if curr_idx == index_of_capitals[-1]:
                    result += ' ' + variable[curr_idx:].lower()
                
            return result.ltrim()
        
        else: #M
            #S;M;plasticCup() -> plastic cup
            variable = code[2]
            index_of_capitals = [variable.index(letter) for letter in variable if letter.isupper()]
            result = ''
            prev_idx = 0
            for curr_idx in index_of_capitals:
                if curr_idx>0:
                    result += ' ' + variable[prev_idx:curr_idx].lower()
                    prev_idx = curr_idx
                    
                if curr_idx == index_of_capitals[-1]:
                    result += ' ' + variable[curr_idx:].lower()
                
            return result[:-2].ltrim()
            
        
    elif code[0] == 'C':
        if code[1] == 'V':
            #C;V;mobile phone -> mobilePhone
            strings = code[2].split(' ')
            result_str = strings[0]+ ''.join([s.capitalize() for s in strings[1:]])
            return result_str            
        
        elif code[1] == 'C':
            #C;C;coffee machine -> CoffeeMachine
            strings_arr = [s.capitalize() for s in code[2].split(' ')]
            return ''.join(strings_arr)
        
        else: #M
            #C;M;white sheet of paper -> whiteSheetOfPaper()
            strings = code[2].split(' ')
            result_str = strings[0]+ ''.join([s.capitalize() for s in strings[1:]])
                       
            return result_str+'()'
        
    
    return 'Format not supported'

if __name__ == '__main__':
    
    strings = sys.stdin.readlines()
    for code_line in strings:
        code = list(code_line.strip().split(';'))
        #[0] =S|M
        #[1] = V|C|M
        #[2] = variableClassMethod()
        result = camelCasing(code)
        print(result)