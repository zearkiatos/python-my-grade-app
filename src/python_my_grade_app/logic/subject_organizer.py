class subject_organizer():
    def __init__(self):
        self.subjects_list = []
        self.subjects_list.append({"name": "Introducción a la programación",
                                  "semestry": "2019-1", "professor": "Antonio Andrade", "grade": 4.5})
        self.subjects_list.append({"name": "Estructuras de datos",
                                  "semestry": "2019-2", "professor": "Hamid Abdallah", "grade": 3.5})
        self.subjects_list.append({"name": "Desarrollo de software",
                                  "semestry": "2020-1", "professor": "Rubby Casallas", "grade": 2.0})
        self.subjects_list.append({"name": "Arquitectura de software",
                                  "semestry": "2020-2", "professor": "Xiao Lihua", "grade": 4.0})
        self.current = 0

    def get_current_subject(self):
        return self.subjects_list[self.current]

    def advance(self):
        self.current += 1
        self.current = self.current % len(self.subjects_list)

    def back(self):
        self.current -= 1
        self.current = self.current % len(self.subjects_list)
