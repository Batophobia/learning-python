from pathlib import Path

def main():
  with open("day24/names.txt") as file:
    names = file.readlines()

  with open("day24/template.txt") as file:
    contents = file.read()

  for name in names:
    customized = contents.replace("[name]", name.strip())
    Path("day24/outputs").mkdir(parents=True, exist_ok=True)
    with open(f"day24/outputs/{name.strip()}.test.ignore", mode="w") as file:
      file.write(customized)

if __name__ == "__main__":
  main()