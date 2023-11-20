import time

def animator(i):
    animation = "-/|\\"
    print(f"\r{animation[i % len(animation)]}", end = "hello")


def main():
    i = 0
    while True:
        animator(i)
        i += 1
        time.sleep(0.5)
        if 1 == 60:
            exit(0)
        
if __name__ == "__main__":
     main()
