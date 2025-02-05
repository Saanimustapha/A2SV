if __name__ == '__main__':
    n = int(input())
    student_info = []
    for i in range(n):
        name = input()
        grade = float(input())
        student_info += [[name,grade]]
        
    student_info = sorted(student_info,key = lambda x:x[1])
    first_second_lowest, last_second_lowest = None, None
    
    
    for i in range(1,len(student_info)):
        if student_info[i][1] != student_info[i-1][1]:
            first_second_lowest,last_second_lowest = i,i+1
            break
    while last_second_lowest < len(student_info):
        if student_info[last_second_lowest][1] == student_info[last_second_lowest-1][1]:
            last_second_lowest += 1
        else:
            break
            
    lowest_scores = student_info[first_second_lowest:last_second_lowest]
    
    lowest_scores = sorted(lowest_scores,key = lambda x:x[0])
    
    for i in range(len(lowest_scores)):
        print(lowest_scores[i][0]) 
        
