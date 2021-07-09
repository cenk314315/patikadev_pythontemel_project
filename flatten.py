input = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
result = []

#tüm elemanları sırayla boş bir listenin içerisine aktaracağız.
#bunun için for döngüsü kullanacağız.
#******************************************************
#we will transfer all the elements in order into an empty list. We will use a for loop for this.

def flatten_list(lists):
    #list tipinde olmayan tüm elemanları boş listeye aktarıyoruz.
    #**************************************************************
    #We transfer all elements that are not of type list to the empty list."""
    for i in lists:
        if type(i) != list:
            result.append(i)
        #liste tipinde olanları için fonksiyonu tekrar çağırıyoruz.
        #************************************************************
        #We call the function again for the list type ones.
        else:
            flatten_list(i)
    return result

print("input: ", input)
print("sonuc: ",flatten_list(input))