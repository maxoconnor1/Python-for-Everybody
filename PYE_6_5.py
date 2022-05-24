str = 'X-DSPAM-Confidence:0.8475'
atpos = str.find(":")
finalstr = str[atpos+1:]
fltfinalstr = float(finalstr)
print(fltfinalstr)
