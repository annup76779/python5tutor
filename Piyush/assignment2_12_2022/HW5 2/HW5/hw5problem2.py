def create_dictionary (idfilename, hwfilename, qzfilename, examfilename):
    sdict = dict()
    with open(idfilename, 'r') as f:
        for id_ in f.readlines():
            sdict[id_.strip()] = {
                "hw": [],
                "quiz": [],
                "exam": [],
            }

    with open(hwfilename, 'r') as f:
        for id_, hwscore in (map(lambda x: x.strip(), line.split()) for line in f.readlines()):
            sdict[id_]["hw"].append(round(float(hwscore), 2))

    with open(qzfilename, 'r') as f:
        for id_, quizscore in (map(lambda x: x.strip(), line.split()) for line in f.readlines()):
            sdict[id_]["quiz"].append(round(float(quizscore), 2))

    with open(examfilename, 'r') as f:
        for id_, examscore in (map(lambda x: x.strip(), line.split()) for line in f.readlines()):
            sdict[id_]["exam"].append(round(float(examscore), 2))
    return sdict


def create_graderoster(sdata_dict, outfilename):
    with open(outfilename, "w") as f:
        f.write(
            "RUID".ljust(14)+"HW(30)".rjust(10)+"QUIZ(30)".rjust(10)+"EXAM(40)".rjust(10)+"TOTAL(100)".rjust(12)+"GRADE".rjust(10)+"\n"
        )
        f.write(str("-"*66) + "\n")
        max_hw = max_quiz = max_exam= max_total = sum_hw = sum_exam=sum_quiz=sum_total = 0
        min_hw = min_quiz = min_exam = min_total = 100
        for id_, val in sdata_dict.items():
            if len(val["hw"]) < 4:
                min_hwscore = 0
            else:
                min_hwscore = min(val["hw"])

            while min_hwscore in val["hw"]:
                val["hw"].remove(min_hwscore)

            if len(val["quiz"]) < 8:
                min_quizscore = 0
            else:
                min_quizscore = min(val["quiz"])

            max_quizscore = max(val["quiz"])
            
            # min amd max are dropped
            if max_quizscore in val["quiz"]:
                val["quiz"].remove(max_quizscore)
            
            if min_quizscore in val["quiz"]:
                val["quiz"].remove(min_quizscore)
            
            hw_30 = round(((sum(val["hw"])/300)* 100) * 0.3, 2)
            if hw_30 < min_hw: 
                min_hw = hw_30
            if hw_30 > max_hw:
                max_hw = hw_30
            quiz_30 = round(((sum(val["quiz"])/ 300)* 100) * 0.3, 2)
            if quiz_30 < min_quiz: 
                min_quiz = quiz_30
            if quiz_30 > max_quiz:
                max_quiz = quiz_30
            exam_40 = round(((sum(val["exam"])/ 400)* 100) * 0.4, 2)
            if exam_40 < min_exam: 
                min_exam = exam_40
            if exam_40 > max_hw:
                max_exam = exam_40

            final_score = round(hw_30 + quiz_30 + exam_40,2)
            if final_score < min_total: 
                min_total = final_score
            if final_score > max_total:
                max_total = final_score

            sum_hw +=hw_30
            sum_quiz +=quiz_30
            sum_exam += exam_40
            sum_total += final_score

            
            grade = ""
            if final_score >= 90.0:
                grade = "A"
            elif final_score >= 85.0:
                grade = "B+"
            elif final_score >= 80.5:
                grade = "B"
            elif final_score >= 75.0:
                grade = "C+"
            elif final_score >= 70.0:
                grade = "C"
            elif final_score >= 60.0:
                grade = "D"

            else:
                grade = "F"

            f.write(
                f"{id_.ljust(14)}{f'{hw_30:.2f}'.rjust(10)}{f'{quiz_30:.2f}'.rjust(10)}{f'{exam_40:.2f}'.rjust(10)}{f'{final_score:.2f}'.rjust(12)}{grade.rjust(10)}\n"
            )
        div = len(sdata_dict.keys())
        f.write("\n")
        f.write(
                f"{'Maximum'.ljust(14)}{f'{max_hw:.2f}'.rjust(10)}{f'{max_quiz:.2f}'.rjust(10)}{f'{max_exam:.2f}'.rjust(10)}{f'{max_total:.2f}'.rjust(12)}\n"
            )

        f.write(
                f"{'Minimum'.ljust(14)}{f'{min_hw:.2f}'.rjust(10)}{f'{min_quiz:.2f}'.rjust(10)}{f'{min_exam:.2f}'.rjust(10)}{f'{min_total:.2f}'.rjust(12)}\n"
            )

        f.write(
                f"{'Average'.ljust(14)}{f'{sum_hw/div:.2f}'.rjust(10)}{f'{sum_quiz / div:.2f}'.rjust(10)}{f'{sum_exam / div:.2f}'.rjust(10)}{f'{sum_total / div:.2f}'.rjust(12)}\n"
            )
