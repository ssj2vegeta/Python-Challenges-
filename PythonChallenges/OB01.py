import csv
import random
masterlist = []
with open("dadjokes.txt", "r") as file:
    reader = csv.DictReader(file, fieldnames=["joke", "answer"])
    for i in reader:
        masterlist.append({"joke": i["joke"], "answer":i["answer"]})
class DadJokes:
    i = random.choice(masterlist)
    def __init__(self, answer = i["joke"], prompt = i["answer"] ):
        self.answer = answer
        self.prompt = prompt

    def PrintRandomJoke(self, d):
        if d == i["answer"]:
            return "Correct!"
        else:
            return i["answer"]



    def Constructor(self):
        print(self.answer)
        k = input("what is your answer to this prompt")
        self.answer = k
        return self.answer

d = DadJokes()
print(d.PrintRandomJoke(d.Constructor()))
