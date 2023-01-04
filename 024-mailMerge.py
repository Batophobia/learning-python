import io

def main():
  with open("day24/test.txt") as file:
    contents = file.read()
    print(contents)

  with open("day24/test2.test.ignore", mode="w") as file:
    file.write("This is added with code.\n")

  with open("day24/test2.test.ignore", mode="a") as file:
    file.write("This is appended with code.\n")

if __name__ == "__main__":
  main()