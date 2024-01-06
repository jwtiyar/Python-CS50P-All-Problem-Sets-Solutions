import random


def main():
    level = get_level()
    error = 0
    score = 0
    for _ in range(0, 10):


        x = generate_integer(level)
        y = generate_integer(level)
        while True:

            try:
                answer = int(input(f"{x} + {y} = "))
                break
            except ValueError:

                print("EEE")
                error += 1
                break


        if answer != x + y:
            print("EEE")
            error += 1
            while True:
                try:
                    answer = int(input(f"{x} + {y} = "))

                except ValueError:
                    print("EEE")
                    error += 1
                    break


                else:
                    if answer == x + y:
                        score += 1
                        break
                    error += 1
                    print("EEE")
                    if error == 3:
                        print(f"{x} + {y} = {x + y}")
                        error = 0
                        break

        else:
            score += 1

    print("Your score is: ", score)


def get_level():
    while True:
        levels = [1, 2, 3]
        try:
            level = int(input("Level: "))
            if level in levels:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)



# generate_integer()
if __name__ == "__main__":
    main()
