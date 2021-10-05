def student(name, grades_list, passing_score, min_score):

    summa = sum(grades_list) / len(grades_list)
        


    if all(i > min_score for i in grades_list) and summa > passing_score:
        print('True')
        return True
    else: 
        print('False')
        return False

student(name='Adnrew', grades_list=[69, 70, 71], passing_score=60, min_score=60)