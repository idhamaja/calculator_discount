# Import the tkinter library (used to create windows and graphical apps)
# "as tk" gives it a shorter name, so we can write tk instead of tkinter
import tkinter as tk



# FUNCTION: runs when the "Hitung" (Calculate) button is clicked
def hitung():

    # try = "attempt to run this code"
    # If an error occurs (for example, the user types letters), jump to except
    try:
        # .get() retrieves the text the user typed into the input box
        # float() converts the text into a decimal number
        harga = float(entry_harga.get())

        # "or 0" means: if the box is empty, use the number 0 instead
        diskon = float(entry_diskon.get() or 0)

        # int() converts the text into a whole number (no decimals)
        jumlah = int(entry_jumlah.get())

    # except = "if an error of type ValueError occurs, run this block"
    # ValueError occurs when text cannot be converted into a number
    except ValueError:
        # .config() changes the appearance of a label
        # fg="red" makes the text red (fg = foreground color)
        label_hasil.config(text="Input harus berupa angka!", fg="red")

        # return = stop the function here and skip the calculation below
        return

    # ----- Calculation -----
    subtotal = harga * jumlah            # total price before the discount
    potongan = subtotal * diskon / 100   # the amount of money deducted
    total = subtotal - potongan          # the final amount to pay

    # Display the result in the label
    # {subtotal:,.0f} means: add thousands separators, show no decimal places
    # \n means: start a new line
    label_hasil.config(
        text=f"Subtotal : Rp {subtotal:,.0f}\n"
             f"Potongan : Rp {potongan:,.0f}\n"
             f"Total    : Rp {total:,.0f}",
        fg="green",   # the text is displayed in green
    )


# BUILDING THE INTERFACE (GUI)

# Create the main window (conventionally named "root")
root = tk.Tk()

# Set the title shown at the top of the window
root.title("Kalkulator Diskon")

# Set the window size: "width x height" in pixels
root.geometry("450x520")

# ----- Fonts (defined once so they are easy to change) -----
FONT_LABEL = ("Arial", 13)        # font for the labels
FONT_ENTRY = ("Arial", 14)        # font for the input boxes
FONT_BUTTON = ("Arial", 13, "bold")  # font for the button
FONT_HASIL = ("Courier", 14)      # monospaced font for the result

# ----- Price input -----
# Label = plain text. .pack() = place it in the window (stacked top to bottom)
# pady=(20, 5) means: 20 pixels of space above, 5 pixels below
tk.Label(root, text="Harga per barang (Rp)", font=FONT_LABEL).pack(pady=(20, 5))

# Entry = a box for typing. width=25 makes the box wider
entry_harga = tk.Entry(root, font=FONT_ENTRY, width=25)
entry_harga.pack()

# ----- Discount input -----
tk.Label(root, text="Diskon (%)", font=FONT_LABEL).pack(pady=(15, 5))
entry_diskon = tk.Entry(root, font=FONT_ENTRY, width=25)
entry_diskon.pack()

# ----- Quantity input -----
tk.Label(root, text="Jumlah barang", font=FONT_LABEL).pack(pady=(15, 5))
entry_jumlah = tk.Entry(root, font=FONT_ENTRY, width=25)
entry_jumlah.pack()

# ----- Button -----
# command=hitung means: when clicked, run the hitung function
# IMPORTANT: write "hitung" without parentheses ()
# padx/pady inside the button (ipadx/ipady) make the button itself bigger
tk.Button(root, text="Hitung", font=FONT_BUTTON, command=hitung).pack(
    pady=20, ipadx=20, ipady=5
)

# ----- Label for displaying the result -----
# It starts empty (text=""); the hitung() function fills it in later
# justify="left" aligns the text to the left
label_hasil = tk.Label(root, text="", font=FONT_HASIL, justify="left")
label_hasil.pack(padx=20, pady=10)


# RUNNING THE PROGRAM
# mainloop() keeps the window open and waits for the user's actions
# Without this line, the window would appear briefly and then disappear
root.mainloop()