import tkinter as tk
import customtkinter as ctk
import math as mt


LARGE_FONT_STYLE = ("Nunito", 24, "bold")
SMALL_FONT_STYLE = ("Nunito", 14)
DIGITS_FONT_STYLE = ("Nunito", 24, "bold")
DEFAULT_FONT_STYLE = ("Nunito", 18, "bold")

PURE_DARK = "#000000"
LITE_DARK = "#212121"
MEDIUM_DARK = "#515151"
LABEL_COLOR = "#FFFFFF"
CBUTTON_COLOR = "#FF0000"
DISPLAY_COLOR = "#000000"
EQUAL_BUTTON_COLOR = "#0057CD"
TRIG_BUTTON = "#0E8849"

ctk.set_appearance_mode("dark")

π = mt.pi
e = mt.e

class Calculator:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("300x450")
        self.window.resizable(False, False)
        self.window.title("AppStaticsX\u2122-Calculator")
        self.window.iconbitmap(r'cal_icon.ico')

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (2, 1), 8: (2, 2), 9: (2, 3),
            4: (3, 1), 5: (3, 2), 6: (3, 3),
            1: (4, 1), 2: (4, 2), 3: (4, 3),
            0: (5, 1), '.': (5, 2)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.trig_functions = {"sin": "sin", "cos": "cos", "tan": "tan"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 6):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_trig_button()
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
        self.create_square_button()
        self.create_sqrt_button()
        self.create_pi_button()
        self.create_e_button()
        self.create_log_button()
        self.create_ln_button()
        self.create_toggle_button()
        self.create_factorial_button()
        self.create_tenpower_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=DISPLAY_COLOR,
                               fg=LABEL_COLOR, padx=10, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=DISPLAY_COLOR,
                         fg=LABEL_COLOR, padx=10, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=PURE_DARK)
        frame.pack(expand=False, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=LITE_DARK, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.total_expression = self.total_expression.replace(self.total_expression, str(f"{""}"))
        self.update_total_label()
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=PURE_DARK, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="DEL", bg=CBUTTON_COLOR, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        try:
            self.current_expression = str(eval(f"{self.current_expression}**2"))
            self.total_expression = self.total_expression.replace(self.total_expression, 
                 "(" + str(eval(f"{self.current_expression}**0.5")) + ")\u00b2")
            self.update_total_label()
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=PURE_DARK, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        try:
            self.current_expression = str(eval(f"{self.current_expression}**0.5"))
            self.total_expression = self.total_expression.replace(self.total_expression, 
                    "\u221a(" + str(eval(f"{self.current_expression}**2")) + ")")
            self.update_total_label()
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=PURE_DARK, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.update_total_label()
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Invalid Input"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=EQUAL_BUTTON_COLOR, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=5, column=4, columnspan=2, sticky=tk.NSEW)

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
        self.label.config(text=self.current_expression[:15])

    def create_trig_button(self):
        row = 0
        for func, symbol in self.trig_functions.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=TRIG_BUTTON, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=func: self.apply_trig_function(x))
            button.grid(row=row, column=5, sticky=tk.NSEW)
            row += 1

    def apply_trig_function(self, func):
        try:
            angle = mt.radians(eval(self.current_expression))
            self.total_expression = self.total_expression.replace(self.total_expression, 
                          func + "(" + str(eval(f"{self.current_expression}")) + "\u2070" + ")")
            self.update_total_label()
            if func == "sin":
                 result = mt.sin(angle)
            elif func == "cos":
                 result = mt.cos(angle)
            elif func == "tan":
                if mt.isclose(angle % (mt.pi * 2), 0):
                    result = "0"
                elif mt.isclose(angle % mt.pi, 0):
                    result = "0"
                elif mt.isclose(angle % (mt.pi / 2),0):
                    result = "Infinity"
                else:
                    result = mt.tan(angle)
            else:
                raise ValueError("Unsupported trigonometric function")
            self.current_expression = str(result)
        except Exception as e:
            self.current_expression = "Invalid Input"
        finally:
            self.update_label()

    def create_pi_button(self):
        button = tk.Button(self.buttons_frame, text="π", bg=PURE_DARK, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                              borderwidth=0,  command=lambda: self.insert_pi())
        button.grid(row=3, column=5, sticky=tk.NSEW)

    def insert_pi(self):
        self.current_expression = str("π")
        self.update_label()

    def create_e_button(self):
        button = tk.Button(self.buttons_frame, text="e", bg=PURE_DARK, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                              borderwidth=0,  command=lambda: self.insert_e())
        button.grid(row=4, column=5, sticky=tk.NSEW)

    def insert_e(self):
        self.current_expression = str("e")
        self.update_label()

    def log(self):
        try:
            self.current_expression = str(mt.log10(eval(self.current_expression)))
            self.total_expression = self.total_expression.replace(self.total_expression, 
                          "log\u2081\u2080" "(" + str(eval(f"10**{self.current_expression}")) + ")")
            self.update_total_label()
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_log_button(self):
        button = tk.Button(self.buttons_frame, text="log", bg=PURE_DARK, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.log)
        button.grid(row=4, column=4, sticky=tk.NSEW)


    def ln(self):
        try:
            self.current_expression = str(mt.log(eval(self.current_expression)))
            self.total_expression = self.total_expression.replace(self.total_expression, 
                          "log\u2091" "(" + str(eval(f"mt.e**{self.current_expression}")) + ")")
            self.update_total_label()
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_ln_button(self):
        button = tk.Button(self.buttons_frame, text="ln", bg=PURE_DARK, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.ln)
        button.grid(row=1, column=1, sticky=tk.NSEW)


    def create_toggle_button(self):
        button = tk.Button(self.buttons_frame, text="\u00B1", bg=PURE_DARK, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.toggle)
        button.grid(row=5, column=3, sticky=tk.NSEW)


    def toggle(self):
        try:
            self.total_expression = self.total_expression.replace(self.total_expression, 
                        "Neg." + "(" + str(eval(f"{self.current_expression}")) + ")" )
            self.current_expression = self.current_expression.replace(self.current_expression, 
                          str(eval(f"-1*{self.current_expression}")))
            self.update_total_label()
            self.update_label()
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()


    def factorial(self):
     try:
        # Calculate the factorial of the current expression
        fact_result = mt.factorial(eval(self.current_expression))
        inverse_fact = None
        # Find the inverse factorial
        for i in range(1, fact_result + 1):
            if mt.factorial(i) == fact_result:
                inverse_fact = i
                break
        
        if inverse_fact is not None:
            # If inverse factorial found, update the current expression and total expression
            self.current_expression = str(mt.factorial(eval(self.current_expression)))
            self.total_expression = self.total_expression.replace(self.total_expression, 
                              "Fact." "(" + str(inverse_fact) + ")")
            self.update_total_label()
        else:
            # If inverse factorial not found, set current expression to "Error"
            self.current_expression = "Error"
        
     except Exception as e:
        self.current_expression = "Error"
     finally:
        self.update_label()


    def create_factorial_button(self):
        button = tk.Button(self.buttons_frame, text="n!", bg=PURE_DARK, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.factorial)
        button.grid(row=1, column=2, sticky=tk.NSEW)


    def create_tenpower_button(self):
        button = tk.Button(self.buttons_frame, text="10\u02b8", bg=PURE_DARK, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.tenpower)
        button.grid(row=1, column=3, sticky=tk.NSEW)


    def tenpower(self):
        try:
            self.total_expression = self.total_expression.replace(self.total_expression, 
                        "10^" + "(" + str(eval(f"{self.current_expression}")) + ")" )
            self.current_expression = self.current_expression.replace(self.current_expression, 
                          str(eval(f"10**{self.current_expression}")))
            self.update_total_label()
            self.update_label()
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
