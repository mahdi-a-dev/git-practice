class Email:
    def __init__(self, sender: str, receiver: str, subject: str, body: str) -> None:
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body

    def send(self) -> None:
        print(f"From: {self.sender}")
        print(f"To: {self.receiver}")
        print(f"Subject: {self.subject}")
        print(f"Body: {self.body}")
        print(f"\t\tEmail send successfully")

def main():
    email = Email("ali@email.com", "reza@email.com", "Hello", "How are you?")
    email.send()


if __name__ == "__main__":
    main()