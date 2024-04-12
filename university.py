import logging
logging.basicConfig(filename="university.log",level=logging.INFO,encoding="utf-8")
class University:
    def __init__(self,name,location):
        self.__name=name
        self.__location=location
        self.__departments=[]
    def set_departments(self,department):
        self.__departments.append(department)
    def get_info(self):
        return (self.__name,self.__location)
    def display_info(self):
        logging.info("---University Info---")
        logging.info(f"Name:{self.__name}")
        logging.info(f"Location:{self.__location}")
        logging.info("The departments in university are:")
        for i in self.__departments:
            logging.info(f"Department:{i.name}")            
class Departments(University):
    def __init__(self,universityName,location,departmantName,courses:list):
        super().__init__(universityName,location)
        self.name=departmantName
        self.location=location
        self.courses=[]
        try:
            for i in courses:
                self.courses.append(i)
        except Exception as e:
            logging.error(f"Invalid format of list")
    def add_course(self,course):
        self.courses.append(course)
    def display_info(self):
        universityName,location=super().get_info()
        logging.info("---Department info---")
        logging.info(f"University:{universityName}")
        logging.info(f"Locaion:{location}")
        logging.info(f"Department Name:{self.name}")
        logging.info("The courses of the deaprtment are:")
        for i in self.courses:
            logging.info(f"{i}")
               
engineering=Departments("MIT","Massachusetts","Engineering",["Computer","Mechanical"])
engineering.add_course("Eectronics")
appliedScience=Departments("MIT","Massachusetts","Applied Science",["Pysics","Chemistry"])
university=University("MIT","Massachusetts")
university.set_departments(engineering)
university.set_departments(appliedScience)
university.display_info()
engineering.display_info()
    