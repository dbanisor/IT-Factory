def read(filename):
    f = open(filename, "r")
    try:
        return f.readlines()
    except:
        print("Error reading file.")
    finally:
        f.close()


# --------------------------------------------- sau mai usor -------------------------------------------

# ---------------- Reading data  ----------------

def read_safe(filename):
    with open(filename, "r") as f:
        return f.readlines()


print(read("data.txt"))
print(read_safe("data.txt"))

# ---------------- Writing data  ----------------

def write(filename, data):
    with open(filename, "w") as f:
        f.writelines(data)


write("data2.txt", ["abc\n", "123\n", "per\n"])

# ---------------- Adding data  ----------------

def append(filename, data):
    with open(filename, "a") as f:
        f.writelines(data)


append("data2.txt", ["12345"])

