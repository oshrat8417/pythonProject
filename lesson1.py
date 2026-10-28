from msvcrt import putch

s=input(" input sensor data")
processed=s[4:8:1]
# המרה
processed=float(processed)
if processed >30 :
    print("Hot")
else :
    print("ool")
    status=s[11::1]
    print("status"+status)
    String=input("input string")
    new_string_event=String[1::2]
    new_string=String[0::2]
    new=new_string_event+new_string
    print(new)
    # print("new_string_event"+ new_string_event)
    # print("new_string"+ new_string)
    first=""
    i=0
    j=int(len(new)/2)
    while j<int(len(new)):
        first+=new[j]
        first+=new[i]
        i+=1
        j+=1
print("first"+first)

