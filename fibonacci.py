def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))

def fibonacci_seq_call(n):
    results = []
    for i in range(n):
        results.append(fibonacci(i))
    return results     

def fibonacci_seq(n):
    results = []
    index = 0
    if index == 0:
        results.append(0)
        index += 1
    if index == 1:
        results.append(1)
        index += 1
    while index > 1 and index <= n - 1:
        results.append(results[index - 1] + results[index - 2])
        index += 1
    return results
        
print(fibonacci_seq_call(9))

    
    