
from os import listdir
from os.path import isfile, join


grades = ["Assignment", "Homework", "Exam", "Midterm", "Reading", "Lab", "Project", "Quiz", "Final"]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
keywords = ['weight', 'evalu', 'deadline', 'due']

# takes in a line as string and squeezes out the assignment type and due date, to return in a list
# in YEAR-DAY-MONTH???
def format_due_date(line):
    line = line.split()
    ret = []

    gradefound = False
    day = 0
    monthidx = 0

    for index, value in enumerate(line):
        if value.capitalize() in grades and not gradefound:
            if value.capitalize() == "Final":
                ret.append("Exam")
            else: ret.append(value.capitalize())

            gradefound = True
            if line[index+1].isdigit():
                ret.append(line[index+1])

        for month in months:
            if month in value:
                # assuming date is formatted like "Friday, September 30th"
                monthidx = months.index(month) + 1
                day = line[index+1]

                end = 0
                for end in range(len(day)):
                    if not day[end].isdigit():
                        day = day[:end]
                        break                
                break

    if not ret:
        return []

    ret.append("2022-" + day + "-" + str(monthidx))
    return ret



def parsesyllabi():
    fn = [f for f in listdir('syllabitxt') if isfile(join('syllabitxt', f))]

    assinfo = {}

    for ofilename in fn:
    # filename = "syllabitxt/241syllabus.pdf.txt"
        filename = "syllabitxt/" + ofilename

        f = open(filename, 'r', encoding="utf-8")

        f = f.read()

        text = f.split("\n")

        weightings = {}

        info = []

        found = False

        for index, line in enumerate(text):
            # DO NOT START LOOKING UNTIL A KEYWORD IS FOUND!!!
            if not found:
                for word in line.split():
                    for key in keywords:
                        if key in word.lower():
                            # print("FOUND KEY WORD:", line)
                            # print()
                            found = True
                            break

            if not found: continue

            for month in months:
                if month in line:
                    # print("DUE DATE:", line)
                    res = format_due_date(line)
                    if res: 
                        duplicate = False
                        for inf in info:
                            if inf[0] == res[0] and inf[1] == res[1]:
                                # print("FOUND COPY:", inf)
                                duplicate= True
                                break
                        if not duplicate:
                            info.append(res)
                        
                        # print(info[-1])

            if "%" in line:
                temp = line.split()
                weight = -1
                asgt = ""
                for word in temp:
                    if "%" in word:
                        weight = int(word.strip(",.:()%"))

                    else:
                        for grade in grades:
                            if grade in word.capitalize():
                                asgt = grade

                if asgt == "":
                    for word in text[index-1].split():
                        for grade in grades:
                            if grade in word.capitalize():
                                asgt = grade
                                break

                if asgt in weightings:
                    if "each" in line or "each" in text[index-1]:
                        weightings[asgt][0] = min(weightings[asgt][0], weight)
                    else:
                        weightings[asgt].append(weight)
                else:
                    weightings[asgt] = [weight]

                # print("WEIGHTINGS:", weightings)
                # print(line)
                # print()

        # print("=================================================================")
        # print(weightings)
        # print(info)
        # print("=================================================================")

        final_info = []

        for weight in weightings:
            found = False
            for inf in info:
                if inf[0] == weight:
                    if inf[0] == "Final":
                        inf.append("Exam")
                    else:
                        inf.append(weightings[inf[0]][0])
                    if len(weightings[inf[0]]) > 1:
                        weightings[inf[0]].pop(0)
                    found = True

            if not found:
                for x in range(len(weightings[weight])):
                    if weight == "Final":
                        info.append(["Exam", weightings[weight][x]])
                    else:
                        info.append([weight, weightings[weight][x]])

        print("FINAL INFO FOR", ofilename.split(".")[0] + ":", info)
        print()

        #put in dict to send to front end :D
        assinfo[ofilename.split(".")[0]] = info


    print()
    print(assinfo)
    return(assinfo)
        


if __name__ == "__main__":
    parsesyllabi()