###########################################################
# INITIAL SETTINGS
n = 7 # 0-depends on first, correct line / any other number
sep = ','
nodata = "NO_DATA"
###########################################################

try:
    f = open('BatNiCd001_old_method.dat', 'r') # 'r' = read
    fc = open('BatNiCd001.dat', 'a')
except Exception as e:
    print(e)
    exit()
    
# goes to the first line with data ("+" at the beggining)
start = 0
sign = f.read(1)
if sign != '+':
    start = 1
    while sign != '+':
        fc.write(sign)
        sign = f.read(1)
        start +=1

f.seek(start)
# how many separators in one line?
if n == 0:
    n = 0
    sign = f.read(1)
    while sign !='\n':
        if sign == ',':
            n += 1
        sign = f.read(1)
#print(n) # variable n stores number of separators in line
f.seek(start)
seps = 0 # number of separators in every line 
pos = 0 # position of the sign of current line we are looking at
# loop that makes correction on corrupted lines

presign = '0'
sign = f.read(1)
while len(sign) > 0:
    while sign != '\n' and len(sign) > 0:
        if sign == ',':
            seps += 1
        pos +=1
        fc.write(sign) # writes sign in proper file
        sign = f.read(1) # goes to the next sign
        # if there is a comma at the end of the line
        if presign == ',' and sign == '\n':
            fc.write(nodata)
        presign = sign # in the next iteration after reading sign, presign will have previous value of sign
        
    if seps == n: # when current line contains correct number of separators
        pos = 0
        seps = 0
        fc.write('\n')
        
    sign = f.read(1)

f.close()
fc.close()

#print(text.read())

# czy plik jest zamknięty (wtedy True)
# print(text.closed)