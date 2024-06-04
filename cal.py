import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_button_clicked():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        result_label.config(text=f"Your BMI: {bmi:.2f}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid weight and height.")

def clear_button_clicked():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")

def main():
    global weight_entry, height_entry, result_label
    
    window = tk.Tk()
    window.title("BMI Calculator")

    weight_label = tk.Label(window, text="Weight (kg):")
    weight_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

    weight_entry = tk.Entry(window)
    weight_entry.grid(row=0, column=1, padx=10, pady=5)

    height_label = tk.Label(window, text="Height (m):")
    height_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

    height_entry = tk.Entry(window)
    height_entry.grid(row=1, column=1, padx=10, pady=5)

    calculate_button = tk.Button(window, text="Calculate", command=calculate_button_clicked)
    calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    clear_button = tk.Button(window, text="Clear", command=clear_button_clicked)
    clear_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    result_label = tk.Label(window, text="")
    result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    window.mainloop()

if __name__ == "__main__":
    main()
