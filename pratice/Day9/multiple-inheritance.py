class centralGovt():
    def exam(self):
        print("Introduced Exams")
class StateGovt():
    def scheme(self):
        print("Proposed many schemes")
class LocalPeople(centralGovt,StateGovt):
    def follow(self):
        print("Follows everything")
l=LocalPeople()
l.scheme()
l.exam()