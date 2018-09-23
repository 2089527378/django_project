str4 = ['yetytuw{}dhkkf,]f我是,{jkhejkf,\"谁\"}]']
i = 0
str_out = ''
while i < len(str4[0]):
    if str4[0][i] == ',' and (str4[0][i + 1] != '{' and str4[0][i + 1] != '\"'):
        pass
    else:
        str_out = str_out + str4[0][i]
    i = i + 1
print(str_out)