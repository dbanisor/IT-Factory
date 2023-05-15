import csv


class UsersRepo:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename) as f:
            reader = csv.DictReader(f)
            return list(reader)

    def find_one(self, name):
        with open(self.filename) as f:
            reader = csv.DictReader(f)
            for user in reader:
                if user["name"] == name:
                    return user

    def create(self, new_user):
        with open(self.filename, "a") as f:
            writer = csv.writer(f)
            writer.writerow(new_user.values())

    def update(self, name, new_data):
        with open(self.filename, "r") as f:
            reader = csv.DictReader(f)
            users = []
            for user in reader:
                if user["name"] == name:
                    user.update(new_data)
                users.append(user)
        with open(self.filename, "w") as f:
            writer = csv.DictWriter(f, users[0].keys())
            writer.writeheader()
            writer.writerows(users)
            

