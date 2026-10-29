class ege_point:
    def __init__(self, subject, primary):
        self.subject = subject
        self.primary = primary

    def russki(self):
        print(int(self.primary * 2) if self.primary <= 50 else 100)

    def matematika(self):
        print(int(self.primary * 2.5) if self.primary <= 32 else 100)

    def himia(self):
        print(int(self.primary * 1.78) if self.primary <= 56 else 100)

    def phizika(self):
        print(int(self.primary * 2.22) if self.primary <= 45 else 100)

    def result(self):
        if self.subject == 'russki':
            self.russki()
        elif self.subject == 'matematika':
            self.matematika()
        elif self.subject == 'himia':
            self.himia()
        elif self.subject == 'phizika':
            self.phizika()
        else:
            print("Не знаю такой предмет") 

print("Введите предмет (russki, matematika, himia, phizika)")   
s = input()

print("Введите первичный балл")
point = int(input())

me = ege_point(subject=s, primary=point) 
me.result()
