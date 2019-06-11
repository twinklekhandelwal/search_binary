
binary_search=[3,4,8,23,56,78,90]
start=0
end=len(binary_search)-1
mid=start+end/2
user_input=int(raw_input("enter no."))
while(start<end):
    

    mid=start+end/2
    if(user_input==binary_search[mid]):
        print mid
    
    elif(user_input<binary_search[mid]):
        start=mid-1
        
    
    
    elif(user_input>binary_search[mid]):
        end=mid+1
    start=start+1 
print start  
