list = ['a', 'b', 'c', 'd', 'e', 'f']

res = [list[i] + list[i+1] + list[i+2] for i in range(len(list) - 2)]
print(res) 

def test_padding(max_len):
    x_train = [[1,23,5,32,55,63,2,21,78,32,23,1],
               [2,32,1,23,1]]
    res1 = [content[:max_len] if len(content) >= max_len 
            else content + [0]*(max_len-len(content)) 
            for content in x_train]

    print(res1) 

test_padding(10) 

