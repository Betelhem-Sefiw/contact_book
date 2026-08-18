import json


class ContactBook:

    FILENAME = "note_book.json"

    def __init__(self):
        self.people = {}
        self.load_data()

    def save(self):
        with open(self.FILENAME, "w") as file:
            json.dump(self.people, file, indent=4)

    def load_data(self):
        try:
            with open(self.FILENAME, "r") as f:
                self.people = json.load(f)
        except FileNotFoundError:
            self.people = {}

    def add_contact(self, name, phone, email, address, company, job, birthdate, notes, tags):

        if not name.strip():
            return False, "Please enter a name."

        if phone:
            if not phone.isdigit():
                return False, "Please enter a valid phone number."

            if len(phone) < 10:
                return False, "Phone number must be at least 10 digits."

        if email:
            if not email.endswith("@gmail.com"):
                return False, "Email must end with @gmail.com."

        self.people[name.strip()] = {
            "phone": phone,
            "email": email,
            "address": address,
            "company": company,
            "job": job,
            "birthdate": birthdate,
            "notes": notes,
            "tags": tags
        }

        self.save()
        return True, "Contact added successfully."

    def view(self):
        return [
            (name, info["phone"], info["email"])
            for name, info in self.people.items()
        ]

    def get_contacts(self):
        return self.people

    def search(self, n):

        if not self.people:
            return False, "No contacts yet."

        n = n.strip()

        if not n:
            return False, "Please enter a name to search."

        matches = {}

        for name, info in self.people.items():

            if n.lower() in name.lower():
                matches[name] = info

        if not matches:
            return False, "Contact not found."

        return True, matches

    def update_contact(
        self,
        old_name,
        name,
        phone,
        email,
        address,
        company,
        job,
        birthdate,
        notes,
        tags
    ):

        if not name.strip():
            return False, "Please enter a name."

        if phone:

            if not phone.isdigit():
                return False, "Please enter a valid phone number."

            if len(phone) < 10:
                return False, "Phone number must be at least 10 digits."

        if email:

            if not email.endswith("@gmail.com"):
                return False, "Email must end with @gmail.com."

        new_name = name.strip()

        if old_name != new_name:

            if new_name in self.people:
                return False, "A contact with this name already exists."

            del self.people[old_name]

        self.people[new_name] = {
            "phone": phone,
            "email": email,
            "address": address,
            "company": company,
            "job": job,
            "birthdate": birthdate,
            "notes": notes,
            "tags": tags
        }

        self.save()

        return True, "Contact updated successfully."

    def delete(self, n):

        if not self.people:
            return False, "No contacts."

        n = n.strip()

        if n in self.people:

            del self.people[n]
            self.save()

            return True, "Deleted successfully."

        return False, "Contact not found."