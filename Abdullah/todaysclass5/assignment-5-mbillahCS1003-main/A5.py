import csv
import matplotlib.pyplot as plt
import numpy as np

# Student Name
# Student Number

# Write Your Code Here

G = -9.8
def calFA(normal, acceleration, mass, mu):
    f_net = mass * acceleration

    # force of friction -> f_f
    f_f = normal * mu
    f_ax = f_net - f_f

    f_ay = (-1 * (mass * G)) - normal
    f_a = ((f_ax ** 2) + (f_ay ** 2)) ** 0.5

    return f_a

def main():
    with open(r"/content/Data.csv", 'r') as f:
        reader = csv.reader(f) # reading the csv file
        next(reader) # skipping the first line of the csv file

        csv_data = list(reader)
        f_a_lst = []
        ques_count, counter = 1, 0
        ques = []

        mean_error = {
            "Alf": [], "Benny": [], "Claire": []
        }
        deviation_dict = {
            "Alf": [], "Benny": [], "Claire": []
        }
        guess_sum = []
        guesses_sum = 0
        less_than_10 = []
        greater_than_10 = []
        for line in csv_data:
            normal, acceleration, mass, mu, name, guess = line
            guess = float(guess)
            f_a_lst.append(guess)
            ques.append(ques_count)
            counter += 1
            guesses_sum += guess
            if counter == 3:
                ques_count+= 1
                counter = 0
                guess_sum.append(guesses_sum/3)
                guesses_sum = 0
            
            f_a = calFA(float(normal), float(acceleration), float(mass), float(mu))
            mean_error[name].append(abs(f_a-guess))
            deviation_dict[name].append(guess)
            error_percentage = ((f_a - guess) / f_a) * 100
            if error_percentage <= 10:
                less_than_10.append(error_percentage)
            else:
                greater_than_10.append(error_percentage)

        # finding the devieation 
        alf_deviation_sum = 0
        benny_deviation_sum = 0
        claire_deviation_sum = 0
        alf_lst, benny_lst, claire_lst = list(deviation_dict.values())
        for alf,benny,claire, sum_of_guess in zip(alf_lst, benny_lst, claire_lst, guess_sum):
            alf_deviation_sum += ((alf - sum_of_guess)**2)
            benny_deviation_sum += ((benny - sum_of_guess)**2) 
            claire_deviation_sum += ((claire - sum_of_guess)**2)
        # getting the final_deviation
        alf_deviation = (alf_deviation_sum / 10) ** 0.5
        benny_deviation = (benny_deviation_sum / 10) ** 0.5
        claire_deviation = (claire_deviation_sum / 10) ** 0.5

        for key, val in mean_error.items():
            mean_error[key] = sum(val)/10

        # making the scattered graph
        plt.xlabel("Question Number")
        plt.ylabel("Guesses")
        plt.title("Students Calculations of Physics Questions")
        plt.scatter(ques, f_a_lst)
        plt.show()

        # making the bar graph
        plt.bar(list(mean_error.keys()), list(mean_error.values()), color=["red", "blue", "green"])
        plt.title("Student Error of Calculation of Physics Questions")
        plt.xlabel("Student Name")
        plt.ylabel("Mean Error")

        plt.show()

        # printing the deviation of all the student
        ## alf
        print("Alf's standard deviation of errors was:",alf_deviation)
        ## benny
        print("Benny's standard deviation of errors was:",benny_deviation)
        ## claire
        print("Claire's standard deviation of errors was:",claire_deviation)

        # making the pie chart for the error percentage
        final_pie_data = [abs(sum(greater_than_10)/len(greater_than_10)), abs(sum(less_than_10)/len(less_than_10))]
        plt.pie(final_pie_data, colors=["blue", "orange"], labels = ["Within 10", "Not Within 10"])
        plt.legend()
        plt.show()

main()