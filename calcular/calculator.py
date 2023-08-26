import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.create_widgets()

    def create_widgets(self):
        self.result_label = tk.Label(self.root, text="", padx=10, pady=10)
        self.result_label.pack()

        self.entry1 = tk.Entry(self.root)
        self.entry1.pack()

        self.entry2 = tk.Entry(self.root)
        self.entry2.pack()

        self.add_button = tk.Button(self.root, text="Somar", command=self.sum)
        self.add_button.pack()

        self.subtract_button = tk.Button(self.root, text="Subtrair", command=self.subtract)
        self.subtract_button.pack()

        self.multiply_button = tk.Button(self.root, text="Multiplicar", command=self.multiply)
        self.multiply_button.pack()

        self.divide_button = tk.Button(self.root, text="Dividir", command=self.divide)
        self.divide_button.pack()

    def get_inputs(self):
        try:
            n1 = float(self.entry1.get())
            n2 = float(self.entry2.get())
            return n1, n2
        except ValueError:
            messagebox.showerror("Erro", "Digite números válidos.")
            return None, None

    def show_result(self, operation, result):
        self.result_label.config(text=f"Resultado: {operation} = {result}")

    def sum(self):
        n1, n2 = self.get_inputs()
        if n1 is not None and n2 is not None:
            result = n1 + n2
            self.show_result("Soma", result)

    def subtract(self):
        n1, n2 = self.get_inputs()
        if n1 is not None and n2 is not None:
            result = n1 - n2
            self.show_result("Subtração", result)

    def multiply(self):
        n1, n2 = self.get_inputs()
        if n1 is not None and n2 is not None:
            result = n1 * n2
            self.show_result("Multiplicação", result)

    def divide(self):
        n1, n2 = self.get_inputs()
        if n1 is not None and n2 is not None:
            if n2 == 0:
                messagebox.showerror("Erro", "Divisão por zero não é permitida.")
            else:
                result = n1 / n2
                self.show_result("Divisão", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
