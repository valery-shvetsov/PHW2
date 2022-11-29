#Не прибегая к random  можно сгенерировать случайное число,
#  используя встроенную хэш-функцию:

#Диапазон значений от a до b

def rand_generator(seed, N=10**6, a=0, b=10, integer = True):
    rands =[]
    if integer:
        for i in range(N):
            num = int(a+(b-a)*(abs(hash(str(hash(str(seed)+str(i+1)))))%10**13)/10**13)
            rands.append(num)
        return rands
    else:
        for i in range(N):
            num = a+(b-a)*(abs(hash(str(hash(str(seed)+str(i+1)))))%10**13)/10**13
            rands.append(num)
        return rands

# Мало что понятно, но очень интересно