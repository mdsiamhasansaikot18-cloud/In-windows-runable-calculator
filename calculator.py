"""
Simple GUI Calculator
Run with: python calculator.py
Requires: Python 3 (tkinter is included by default on Windows installs from python.org)
"""

import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.resizable(False, False)
        self.configure(bg="#1e1e1e")

        self.expression = ""
        self.just_evaluated = False

        self._build_display()
        self._build_buttons()
        self._bind_keys()

    def _build_display(self):
        self.display_var = tk.StringVar(value="0")
        display = tk.Entry(
            self,
            textvariable=self.display_var,
            font=("Segoe UI", 28),
            bd=0,
            relief="flat",
            justify="right",
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
            state="readonly",
            readonlybackground="#1e1e1e",
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=(20, 10), ipady=20)

    def _build_buttons(self):
        buttons = [
            ("C", 1, 0, "#a83232", "white"),
            ("←", 1, 1, "#3a3a3a", "white"),
            ("%", 1, 2, "#3a3a3a", "white"),
            ("÷", 1, 3, "#f0a020", "white"),

            ("7", 2, 0, "#2d2d2d", "white"),
            ("8", 2, 1, "#2d2d2d", "white"),
            ("9", 2, 2, "#2d2d2d", "white"),
            ("×", 2, 3, "#f0a020", "white"),

            ("4", 3, 0, "#2d2d2d", "white"),
            ("5", 3, 1, "#2d2d2d", "white"),
            ("6", 3, 2, "#2d2d2d", "white"),
            ("-", 3, 3, "#f0a020", "white"),

            ("1", 4, 0, "#2d2d2d", "white"),
            ("2", 4, 1, "#2d2d2d", "white"),
            ("3", 4, 2, "#2d2d2d", "white"),
            ("+", 4, 3, "#f0a020", "white"),

            ("±", 5, 0, "#2d2d2d", "white"),
            ("0", 5, 1, "#2d2d2d", "white"),
            (".", 5, 2, "#2d2d2d", "white"),
            ("=", 5, 3, "#2f9e44", "white"),
        ]

        for (text, row, col, bg, fg) in buttons:
            btn = tk.Button(
                self,
                text=text,
                font=("Segoe UI", 18),
                bg=bg,
                fg=fg,
                activebackground="#555555",
                bd=0,
                relief="flat",
                width=5,
                height=2,
                command=lambda t=text: self.on_button(t),
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

    def _bind_keys(self):
        self.bind("<Key>", self.on_key)

    def on_key(self, event):
        char = event.char
        if char in "0123456789.+-":
            self.on_button(char)
        elif char == "*":
            self.on_button("×")
        elif char == "/":
            self.on_button("÷")
        elif char in ("\r", "="):
            self.on_button("=")
        elif char == "\x08":  # backspace
            self.on_button("←")
        elif event.keysym == "Escape":
            self.on_button("C")

    def on_button(self, key):
        if key == "C":
            self.expression = ""
            self.display_var.set("0")
            return

        if key == "←":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")
            return

        if key == "±":
            if self.expression and self.expression[0] == "-":
                self.expression = self.expression[1:]
            elif self.expression:
                self.expression = "-" + self.expression
            self.display_var.set(self.expression if self.expression else "0")
            return

        if key == "=":
            self.evaluate()
            return

        if self.just_evaluated and key not in ("+", "-", "×", "÷", "%"):
            self.expression = ""
        self.just_evaluated = False

        mapping = {"×": "*", "÷": "/", "%": "/100*"}
        self.expression += mapping.get(key, key)
        self.display_var.set(self.expression)

    def evaluate(self):
        try:
            safe_expr = self.expression.replace("×", "*").replace("÷", "/")
            allowed = "0123456789.+-*/() "
            if not all(c in allowed for c in safe_expr):
                raise ValueError("Invalid characters")
            result = eval(safe_expr, {"__builtins__": {}}, {})
            if isinstance(result, float):
                result = round(result, 10)
                if result == int(result):
                    result = int(result)
            self.display_var.set(str(result))
            self.expression = str(result)
            self.just_evaluated = True
        except Exception:
            self.display_var.set("Error")
            self.expression = ""
            self.just_evaluated = True


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
