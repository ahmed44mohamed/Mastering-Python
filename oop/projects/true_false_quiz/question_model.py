class Question:
    """
    This class take two input arguments:
    * q_text --> Question with the answer
    * q_answer --> if it is tru or false
    """
    def __init__(self, q_text = "", q_answer = ""):
        self.text = q_text
        self.answer = q_answer
