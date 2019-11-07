alphabets = "abcdefghijklmnopqrstuvwxyz" # this is the english letters


def encrypt(p, k):
    c = ""
    kpos = [] # return the index of characters ex: if k='d' then kpos= 3
    for x in k:
        kpos.append(alphabets.find(x))
    i = 0
    for x in p:
      if i == len(kpos):
          i = 0
      pos = alphabets.find(x) + kpos[i]
      print(pos)
      if pos > 25:
          pos = pos-26
      c += alphabets[pos].capitalize()
      i +=1
    return c


def main(args):
       p = input("enter the plain text: ")
       p = p.replace(" ", "")  # this will make sure that there is no space in the message
       k = input("Enter the key: ")
       k = k.strip()  # remove the white spaces from both sides
       c = encrypt(p, k)
       print("The cipher text is: ", c)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))