from collections import OrderedDict
list=[]
def permutations(act_dict,arr,string,n):
    sum=0
    if n>=len(string):
        list.append(''.join(arr)) #could have just printed the string here but output requires count first hence appending
        return 1

    for i in act_dict:
        if act_dict[i]>0:
            arr[n]=i
            act_dict[i]-=1
            sum+=permutations(act_dict,arr,string,n+1)
            arr[n]=None
            act_dict[i] += 1
    return sum
if __name__ == "__main__":
    act_dict=OrderedDict()
    string=input()
    string=sorted(string)
    for i in string:
        if i not in act_dict.keys():
            act_dict[i]=1
        else:
            act_dict[i]+=1
    n = len(string)
    arr=[None]*n
    xyz=permutations(act_dict,arr,string,0)
    print(xyz)
    for i in list:
        print(i)




