


def wrapper(f):
    def fun(l):
        f(["+91 " + c [-10:-5] + " " + c [-5:] for c in l])
        return fun
@wrapper

def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
    
'''    
Let's dive into decorators! You are given

mobile numbers. Sort them in ascending order then print them in the standard format shown below:

+91 xxxxx xxxxx

3
07895462130
919875641230
9195969878

Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230
'''
