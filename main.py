import requests
from html import unescape

difficulty_list = ["easy", "medium", "difficult"]

categories_dictionary = {
    "general knowledge": "9",
    "books": "10",
    "film": "11",
    "music": "12",
    "musicals & theatre": "13",
    "television": "14",
    "video games": "15",
    "board games": "16",
    "science and nature": "17",
    "computers": "18",
    "mathematics": "19",
    "mythology": "20",
    "sports": "21",
    "georgraphy": "22",
    "history": "23",
    "politics": "24",
    "art": "25",
    "celebrities": "26",
    "animals": "27",
    "vehicles": "28",
    "comics": "29",
    "gadgets": "30",
    "anime and manga": "31",
    "cartoon and animations": "32"
}

list_of_categories = [category for category in categories_dictionary.keys()]
count = 0

print("The categories are: \n" + "\n".join(list_of_categories))
number_categories = int(input("How many categories would you like?"))

while count < number_categories:

    category_word = input("Which category would you like?").lower()
    if category_word not in list_of_categories:
        print("invalid input")
        continue

    amount_questions = input("How many questions woud you like for this category?")
    if isinstance(amount_questions, int):
        print("invalid input")
        continue

    difficulty_level = input("How difficult would you like these questions to be? Easy, Medium or Difficult?").lower()
    if difficulty_level not in difficulty_list:
        print("invalid input")
        continue

    category_number = categories_dictionary[category_word]
    endpoint = f"https://opentdb.com/api.php?amount={amount_questions}&category={category_number}&difficulty={difficulty_level}"
    response = requests.get(endpoint)
    data = response.json()
    questions = data["results"]
    with open("quiz_questions.txt", "a") as file:
        file.write(f"{category_word.upper()} \n \n")

    for dictionary in questions:
        question = unescape(dictionary["question"])
        answer = dictionary["correct_answer"]
        with open("quiz_questions.txt", "a") as file:
            file.write(f"Question: {question} \n"
                       f"Answer: {answer} \n \n")

    count += 1

print("all done!")
