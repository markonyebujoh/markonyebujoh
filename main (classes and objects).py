class Student:
    # [assignment] Skeleton class. Add your code here
    name = str("Mark")
    age = int(25)
    track = ["French", "Mathematics", "English", "biology", "physics"]
    score = float(97.5)
    
     
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def add_track(self, track):
        self.track = track
        

    def get_score(self):
        return self.score
        
    



Bob = Student(name="Bob", age=26, track=["FE","BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

