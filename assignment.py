my_input_file =open("sample_input.txt","r")
new_output_file = open("output.txt","w+")
goodies={}
out_list=[]
for f in my_input_file:
    toRead_index_price=f.index(":")
    print(f[toRead_index_price+1:].strip())
    print(f[:toRead_index_price])
    goodies[f[:toRead_index_price]]=f[toRead_index_price+1:].strip()
print(goodies) 
prices=list(goodies.values())

prices=[int(i)for i in prices]

prices.sort(reverse=True)
print(prices)


num_of_employees=int(input("number of employees: "))
length=(len(prices)-num_of_employees)

print(length)

for i in range(length):
    max_price=prices[i]
    min_price=prices[num_of_employees+i]
    if i == 0:
        diff=max_price-min_price
        idx_choosen=i
    elif (max_price-min_price)<diff:
        diff=max_price-min_price
        idx_choosen=i

choosen_prices=prices[idx_choosen:num_of_employees+idx_choosen]

diff=max(choosen_prices)-min(choosen_prices)
print("diff",diff)

cnt=0
for key,value in goodies.items():
    prices[cnt]
    print(value)
    if int(value)in choosen_prices and cnt<num_of_employees:
        str1=key+": "+value
        
        out_list.append(str1)
        cnt+=1
        print(str1)
new_output_file.write("goodies selected for distributing: ")

new_output_file.write("\n")
for i in out_list:
    new_output_file.write(i)
    new_output_file.write("\n")
new_output_file.write("difference: "+str(diff))

my_input_file.close()
new_output_file.close()