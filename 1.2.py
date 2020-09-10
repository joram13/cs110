def multiply(a,b):
    d1 = [int(x) for x in str(a)]
    d2 = [int(x) for x in str(b)]
    end = [0]*(len(d1)+len(d2))
    d1.reverse()
    d2.reverse()
    p = len(end)-1
    for i in d2:
        carry = 0
        p2 = 0
        carry2 = 0
        for e in d1:
            rech = (i*e) + carry 
            rech = [int(x) for x in str(rech)]
            if len(rech) == 1:
                end[p-p2] += (rech[0]) +carry2
                
                end2 = [int(x) for x in str(end[p-p2])]
                carry2 = 0
                carry = 0
                if len(end2) == 2:
                    end[p-p2] = end2[1]
                    carry2 = end2[0]

                 
                    
                    
                p2 += 1
            else:
                end[p-p2] += rech[1] + carry2
                
                end2 = [int(x) for x in str(end[p-p2])]
                carry2 = 0
                if len(end2) == 2:
                    end[p-p2] = end2[1]
                    carry2 = end2[0]
            
                carry = rech[0]
            p2 += 1
        
        if p-p2 >= 0:
            end[p-p2] = carry2+ carry
    

        p -= 1
        
    end_2 = [str(digit) for digit in end]
    end_3 = "".join(end_2)
    end_4 = int(end_3)
    return end_4
