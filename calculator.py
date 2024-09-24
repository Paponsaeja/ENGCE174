import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class BaseCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.is_squaring_mode = False
        self.last_result = None
        self.initial_number = None

        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_open_parenthesis_button()
        self.create_close_parenthesis_button()
        self.create_backspace_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        if self.current_expression:
            last_char = self.current_expression[-1]
            if last_char.isdigit() or last_char == ')':
                if value == '(':
                    self.current_expression += '*('
                else:
                    self.current_expression += str(value)
            elif value == ')' and self.current_expression.count('(') > self.current_expression.count(')'):
                self.current_expression += ')'
            else:
                self.current_expression += str(value)
        else:
            self.current_expression += str(value)

        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        if self.current_expression != "":
            self.current_expression += operator
            self.total_expression += self.current_expression
            self.current_expression = ""
            self.update_total_label()
        else:
            if operator in self.operations:
                self.total_expression = self.total_expression.rstrip("+-*/") + operator
                self.update_total_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.last_result = None
        self.is_squaring_mode = False
        self.initial_number = None
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_open_parenthesis_button(self):
        button = tk.Button(self.buttons_frame, text="(", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression('('))
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_close_parenthesis_button(self):
        button = tk.Button(self.buttons_frame, text=")", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression(')'))
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def backspace(self):
        if self.current_expression:
            self.current_expression = self.current_expression[:-1]
            self.update_label()

    def create_backspace_button(self):
        button = tk.Button(self.buttons_frame, text="⌫", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.backspace)
        button.grid(row=0, column=0, sticky=tk.NSEW)

    def evaluate(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()
        
class AdvancedCalculator(BaseCalculator):
    def __init__(self):
        super().__init__()
        self.is_continuing = False  # Flag to track if we're continuing from the last result
        self.last_operator = None  # Track the last operator used
        self.last_operand = None  # Track the last operand for repeated operations

    def evaluate(self):
        # If we're continuing from a result, use the last result for further calculations
        if self.is_continuing and self.last_result is not None and self.last_operator and self.last_operand is not None:
            # Repeat the last operation with the last operand
            expression = f"{self.last_result}{self.last_operator}{self.last_operand}"
        else:
            # First-time evaluation or a fresh input
            expression = self.total_expression + self.current_expression

        # Handle cases like operator at the end of expression
        if expression.endswith(("*", "/", "+", "-")):
            expression = expression[:-1]  # Remove trailing operator

        # Close any open parenthesis
        open_parenthesis_count = expression.count('(')
        close_parenthesis_count = expression.count(')')
        if open_parenthesis_count > close_parenthesis_count:
            expression += ')' * (open_parenthesis_count - close_parenthesis_count)

        # Replace symbols for division and multiplication
        expression = expression.replace("\u00F7", "/").replace("\u00D7", "*")

        try:
            result = eval(expression)
            # Update current expression with the result
            self.current_expression = str(result)
            self.last_result = result

            # Store the last operator and operand for repeated evaluation if not already doing so
            if not self.is_continuing:
                self.last_operator = self.total_expression[-1] if self.total_expression else None
                self.last_operand = self.current_expression

            # Clear total expression for next calculation
            self.total_expression = ""
            self.is_continuing = True

        except Exception:
            self.current_expression = "Error"
            self.last_result = None
            self.last_operator = None
            self.last_operand = None

        self.update_total_label()
        self.update_label()

    def append_operator(self, operator):
        # Allow continuing from the last result when an operator is pressed after `=`
        if self.is_continuing:
            self.total_expression = str(self.last_result)
            self.current_expression = ""
            self.is_continuing = False  # Reset continuation flag

        super().append_operator(operator)

if __name__ == "__main__":
    calc = AdvancedCalculator()
    calc.run()