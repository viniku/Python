def main():
    string = input("How do you feel? (1-10) ")
    p = int(string)
    if p >= 1 and p <= 10:
        if p == 1:
            print("A suitable smiley would be :'(")
        elif p == 10:
            print("A suitable smiley would be :-D")
        elif p < 4:
            print("A suitable smiley would be :-(")
        elif p <= 7:
            print("A suitable smiley would be :-|")
        elif p > 6:
            print("A suitable smiley would be :-)")
    else:
            print("Bad input!")
if __name__ == "__main__":
    main()