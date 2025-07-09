try:
    with open('config.txt','r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Config File is misisng")
finally:
    print("Execution Complete")