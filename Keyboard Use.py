LEFTKEYS=list("~`!1@2#3$4%5^6qQwWeErRtTyYaAsSdDfFgGZzXxCcVvBb")

def assess(text):
    leftCount=0
    totalCount=len(text)
    for i in text:
        for j in LEFTKEYS:
            if i==j:
                leftCount+=1
    stats={'left count:':leftCount, 'right count:':totalCount-leftCount,
    'total count:':totalCount, '% left:': leftCount/totalCount*100, '% right:': (1-leftCount/totalCount)*100}
    return stats


def main():
    print("""
    Welcome to keyboard assessment
    This program will inform you which side of the keyboard is used
    in a text and return key information about your keyboard usage\n""")
    text=input('Type or paste a text here:')
    result=assess(text)
    for i in result:
        print(i+str(result[i]))


if __name__ == "__main__":
    main()