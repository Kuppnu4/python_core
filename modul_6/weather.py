import sys


def base():
    if len(sys.argv) != 2:
        print(f"Usage {sys.argv[0]} country")
        sys.exit(1)

    country = sys.argv[1]
    if country == "Ukraine":
        print("Sun")
    elif country == "Germany":
        print("Cloudy")
    else:
        print("I do not know")
        sys.exit(1)
    
    print(sys.argv)
    


if __name__ == "__main__":
    base()

    
