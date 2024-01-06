def convert(cwmle):
    cwmle = cwmle.replace(":)", "🙂")
    cwmle = cwmle.replace(":(", "🙁")
    print(cwmle)

def main():
    cwmle = input("")
    return convert(cwmle)

main()