
while __name__ == "__main__":

    text = input("enter text to encode/decode:").lower()
    i = 0
    p_end = 0
    ########## processing text ##############
    def process():
        global text
        global p_end
        for j in range(0,len(text),2):
            if j < len(text) - 1:
                p_end += 1
                if text[j] == text[j+1]:
                    text = text[:j+1] + 'x' + text[j+1:]
                    break

    while p_end < len(text):
        process()
        
    if len(text) % 2 == 1:
        text += 'x'

    ptext = [text[i:i+2] for i in range(0,len(text),2)]

    ######grid generation############
    tkey = input("input key:")
    key = ''
    for i in tkey:
        if i not in key:
            key += i
        
    grid = 'abcdefghijklmnoprstuvwxyz'
    ngrid = ''
    for i in grid:
        if i not in key:
            ngrid += i
    ngrid = key + ngrid
    ngrid = [ngrid[i:i+6] for i in range(0,25,5)]

    processed_text = ''
    c_1 = 0
    r_1 = 0
    r_2 = 0
    c_2 = 0

    for p in ptext:
        for i in range(5):
            for j in range(5):
                if ngrid[i][j] == p[0]:
                    c_1, r_1 = j, i
                if ngrid[i][j] == p[1]:
                    c_2, r_2 = j, i
        processed_text += ngrid[r_1][c_2] + ngrid[r_2][c_1]
                    
                
                
    print("encoded/decoded text:" + processed_text)

    







