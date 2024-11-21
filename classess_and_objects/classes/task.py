class Task:

    is_done = False

    def __init__(self, description):
        self.description = description

    def mark_done(self):
        self.is_done = True

    def get_status(self):
        # if self.is_done == True:
        #     return "Completed"
        # else:
        #     return "Incomplete"
        # Ternary Operator (shorthand if/else statement)
        return "Completed" if self.is_done else "Incomplete"
