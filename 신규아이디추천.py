import re

def solution(new_id):
    answer = ''
    answer = new_id.lower()
    
    answer = re.sub('[^a-z0-9\-_.]','',answer)

    while answer.find('..')!= -1 :
        answer = answer.replace('..','.')
    
    answer = answer.strip('.')
    
    answer = 'a' if answer == '' else answer
    
    answer = answer[0:15].strip('.')
    
    answer = answer + answer if len(answer) < 2 else answer 
    answer = answer + answer[1] if len(answer) < 3 else answer 
    return answer
