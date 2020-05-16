sachin_Tendulkar  = int(input("Score achived by Sachin Tendulkar in 60 balls: "))
virat_Kohli = int(input("Score achived by Virat Kohli in 60 balls:"))
ms_Dhoni = int(input("Score achived by Mahendra Singh Dhoni in 60 balls:"))
strike_Rate_of_ST =  sachin_Tendulkar * 100 / 60
strike_Rate_of_VK = virat_Kohli * 100 / 60
strike_Rate_of_MD = ms_Dhoni * 100 / 60
print("Strike rate of Sachin Tendulkar", strike_Rate_of_ST)
print("Strike rate of Virat Kohli",strike_Rate_of_VK)
print("Strike rate of Mahendra Singh Dhoni",strike_Rate_of_MD)
print("Score achived by Sachin Tendulkar if they played 60 more balls is", sachin_Tendulkar * 2)
print("Score achived by Virat Kohli if they played 60 more balls is", virat_Kohli * 2)
print("Score achived by Mahendra Singh Dhoni if they played 60 more balls is", ms_Dhoni * 2)
#Number of maximum sixes are calculated on the basis of maximum score achived by the player
print("Maximum number of sixes Sachin Tendulkar could hit =", sachin_Tendulkar // 6)
print("Maximum number of sixes Virat Kohli could hit =", virat_Kohli // 6)
print("Maximum number of sixes Mahendra Singh Dhoni could hit =", ms_Dhoni // 6)