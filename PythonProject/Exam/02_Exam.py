def describe(*args,**kwargs):
    sum_tuple=0
    sum_dict=0
    list_key=[]
    for i in args:
        sum_tuple+=1
    for j in kwargs:
        sum_dict+=1
        list_key.append(j)
    print(f'位置参数个数是{sum_tuple}')
    print(f'关键字参数个数是{sum_dict}')
    print("键：",end="")
    for lk in list_key:
        print(lk,end=' ')
describe(1, 'hello', 3.14, name='Alice', age=25, city='Beijing')