def main():
    x = input("Greeting:").lower()
    y= value(x)
    print(y)


def value(greeting):
    greeting= greeting.lower()
    if "hello" in greeting:
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
