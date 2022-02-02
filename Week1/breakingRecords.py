#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#
#input [10, 20, 30, 40, 50]
#output [breaking_most_point, breaking_least_point]

def breakingRecords(scores):
    # Write your code here
    break_points = [0, 0] #from constraints minimum values
    prev_max_score, prev_min_score = scores[0], scores[0]
   
    for i in range(1, len(scores)):
        if scores[i] > prev_max_score:
            break_points[0] += 1
            prev_max_score = scores[i]
            
        elif scores[i] < prev_min_score:
            break_points[1] += 1
            prev_min_score = scores[i]
            
        else: continue
        
        print(break_points)
    
    return break_points

if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    
    print(result)