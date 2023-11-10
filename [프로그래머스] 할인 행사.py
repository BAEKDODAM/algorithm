def solution(want, number, discount):
    product_dict = {}
    for i in range(len(want)):
        product_dict[want[i]] = number[i]

    copy_dict = product_dict.copy()
    
    n=0
    cnt = 10
    for i in discount:
        print(cnt)
        if cnt == 0:
            answer = n-10;
            break;

        n+=1
        
        if i not in want or copy_dict[i] <= 0 :
            if len(discount)-n < 10:
                return 0;
            copy_dict = product_dict.copy()
        else:
            copy_dict[i] -= 1
            cnt-=1
        print(copy_dict)
    return answer
want = ["banana", "apple", "rice", "pork", "pot"]
number =  [3, 2, 2, 2, 1]
discount =["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))
