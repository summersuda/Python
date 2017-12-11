from pygal import Bar

from die import Die

def show_one_die_bar(numbers, num_sides=6):
    """投掷骰子numbers次，看每个面出现的次数，用直方图显示结果"""
    die = Die(num_sides)
    results = []
    title_num_sides = "D" + str(num_sides)

    # 投掷骰子，把结果保存在results中
    for number in range(numbers):
        results.append(die.roll())

    # 分析结果
    frequencies = []
    for value in range(1, die.num_sides+1):
        frequencies.append(results.count(value))

    # 显示结果在Console窗口
    #print(results)
    #print(frequencies)

    # 对结果可视化
    hist = Bar()
    
    hist.title = "Results of rolling one " + title_num_sides + " " + str(numbers) + " times"
    hist.x_labels = [str(num) for num in range(1,num_sides + 1)]
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add(title_num_sides, frequencies)
    hist.render_to_file("die_visual_" + title_num_sides + "_"
                        + str(numbers) + ".svg")

show_one_die_bar(1000)
show_one_die_bar(10000, 8)
    
def show_two_die_bar(numbers, num_sides1=6, num_sides2=6):
    """投掷骰子numbers次，看每个面出现的次数，用直方图显示结果"""
    die1 = Die(num_sides1)
    title_num_sides1 = "D" + str(num_sides1)

    die2 = Die(num_sides2)
    title_num_sides2 = "D" + str(num_sides2)

    results = []
    # 投掷两个骰子，把相加结果保存在results中
    for number in range(numbers):
        results.append(die1.roll() + die2.roll())

    # 分析结果
    max_result = num_sides1 + num_sides2
    min_result = 2

    frequencies = []
    for value in range(min_result, max_result+1):
        frequencies.append(results.count(value))

    # 显示结果在Console窗口
    #print(results)
    #print(frequencies)

    # 对结果可视化
    hist = Bar()
    
    if title_num_sides1 == title_num_sides2:
        hist.title = ("Results of rolling two " + title_num_sides1 
                      + " " + str(numbers) + " times")
    else:
        hist.title = ("Results of rolling one " + title_num_sides1
                     + " and one " + title_num_sides2 + " " + str(numbers) + " times")
        
    hist.x_labels = [str(num) for num in range(min_result, max_result+1)]
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"

    hist.add(title_num_sides1 + " + " + title_num_sides2, frequencies)
    hist.render_to_file("die_visual_" + title_num_sides1 + "_" 
                        + title_num_sides2 + "_" + str(numbers) + ".svg")

show_two_die_bar(1000, 6, 6)
show_two_die_bar(100000, 5, 8)
show_two_die_bar(100000, 9, 10)