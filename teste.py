string = '$680,000.00'
partialstr = string.replace(',','')
newstr = partialstr.replace('$','')
newstr2 = newstr.replace('.00','')
print(newstr2)