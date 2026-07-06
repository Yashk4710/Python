#WAP to check if a list contains palindrome of element 
List = [1, 2, 3, 4, 3, 2, 1]

copy_List = List.copy()
copy_List.reverse()

if(copy_List == List):
    print("Palindrome")

else:
    print("NOT Palindrome")