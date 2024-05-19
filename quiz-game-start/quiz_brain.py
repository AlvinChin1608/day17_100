# TODO: asking the question
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz

# question_number = 0
# question_list

# next_question()

class QuizBrain:
    def __init__(self, q_list):
        """
              Initializes the QuizBrain with a list of questions.

              Args:
                  q_list (list): List of Question objects.
        """
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def next_question(self):
        """
                Prompts the user with the next question and checks the answer.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False): ")
            if user_answer.lower() in ["true", "false"]:
                break
            else:
                print("Invalid input. Please enter 'True' or 'False' ")
        self.check_answer(user_answer, current_question.answer)


    def still_has_question(self):
        """
               Checks if there are more questions left in the quiz.

               Returns:
                   bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """
                Checks if the user's answer is correct and updates the score.

                Args:
                    user_answer (str): The answer provided by the user.
                    correct_answer (str): The correct answer to the question.
        """

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n\n")


