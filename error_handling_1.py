def division(num1,num2):
    try:
        result=num1/num2
        return result
    except ZeroDivisionError:
        print("Second number cannot be zero")
        
result=division(1,3)
print(result)
result=division(2,0)
print(result)        