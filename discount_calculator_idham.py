import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

# ---------- Warna & ukuran ----------
BG = "#F3F4F6"        # latar jendela
CARD = "#FFFFFF"      # latar kartu
TEXT = "#111827"
MUTED = "#6B7280"
ACCENT = "#2563EB"
ACCENT_DARK = "#1D4ED8"
DANGER = "#DC2626"
SUCCESS = "#059669"
BORDER = "#E5E7EB"


# ---------- Logika ----------
def calculate_final_total(price: float, discount_rate: float, quantity: int):
    subtotal = price * quantity
    discount_amount = subtotal * (discount_rate / 100)
    return subtotal, discount_amount, subtotal - discount_amount


def parse_float(value: str, field: str) -> float:
    try:
        number = float(value.replace(",", "."))
    except ValueError:
        raise ValueError(f"{field} harus berupa angka.")
    if number < 0:
        raise ValueError(f"{field} tidak boleh negatif.")
    return number


def parse_int(value: str, field: str) -> int:
    try:
        number = int(value)
    except ValueError:
        raise ValueError(f"{field} harus berupa bilangan bulat.")
    if number <= 0:
        raise ValueError(f"{field} harus lebih dari 0.")
    return number


def format_rupiah(value: float) -> str:
    """1234567.5 -> 'Rp 1.234.567,50' ; 360000 -> 'Rp 360.000'"""
    value = round(value, 2)
    if value.is_integer():
        text = f"{int(value):,}".replace(",", ".")
    else:
        text = f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"Rp {text}"


# ---------- Tampilan ----------
def build_app() -> tk.Tk:
    root = tk.Tk()
    root.title("Kalkulator Diskon")
    root.configure(bg=BG)
    root.resizable(False, False)

    base = tkfont.nametofont("TkDefaultFont").actual()["family"]
    f_title = (base, 18, "bold")
    f_sub = (base, 10)
    f_label = (base, 10)
    f_entry = (base, 11)
    f_value = (base, 11)
    f_total = (base, 20, "bold")

    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Card.TFrame", background=CARD, relief="solid", borderwidth=1,
                    bordercolor=BORDER)
    style.configure("Bg.TFrame", background=BG)
    style.configure("Card.TLabel", background=CARD, foreground=TEXT, font=f_label)
    style.configure("Muted.TLabel", background=CARD, foreground=MUTED, font=f_label)
    style.configure("TEntry", padding=6, fieldbackground="white", bordercolor=BORDER,
                    lightcolor=BORDER, darkcolor=BORDER)
    style.map("TEntry", bordercolor=[("focus", ACCENT)], lightcolor=[("focus", ACCENT)],
              darkcolor=[("focus", ACCENT)])
    style.configure("Primary.TButton", background=ACCENT, foreground="white",
                    font=(base, 10, "bold"), padding=(10, 9), borderwidth=0)
    style.map("Primary.TButton", background=[("active", ACCENT_DARK)])
    style.configure("Secondary.TButton", background="white", foreground=TEXT,
                    font=(base, 10), padding=(10, 9), bordercolor=BORDER)
    style.map("Secondary.TButton", background=[("active", BG)])

    outer = ttk.Frame(root, style="Bg.TFrame", padding=24)
    outer.pack(fill=tk.BOTH, expand=True)

    # Header
    tk.Label(outer, text="Kalkulator Diskon", font=f_title, bg=BG, fg=TEXT).pack(anchor="w")
    tk.Label(outer, text="Hitung total harga setelah diskon", font=f_sub,
             bg=BG, fg=MUTED).pack(anchor="w", pady=(0, 16))

    # Kartu input
    form = ttk.Frame(outer, style="Card.TFrame", padding=20)
    form.pack(fill=tk.X)
    form.columnconfigure(1, weight=1)

    def add_row(row, label, suffix=None, prefix=None):
        ttk.Label(form, text=label, style="Card.TLabel").grid(
            row=row * 2, column=0, columnspan=3, sticky="w", pady=(0 if row == 0 else 12, 4))
        if prefix:
            ttk.Label(form, text=prefix, style="Muted.TLabel").grid(
                row=row * 2 + 1, column=0, sticky="w", padx=(0, 8))
        entry = ttk.Entry(form, font=f_entry, width=24)
        entry.grid(row=row * 2 + 1, column=1, sticky="ew",
                   columnspan=1 if prefix else 2)
        if suffix:
            ttk.Label(form, text=suffix, style="Muted.TLabel").grid(
                row=row * 2 + 1, column=2, sticky="w", padx=(8, 0))
            entry.grid_configure(columnspan=1)
        return entry

    price_entry = add_row(0, "Harga per barang", prefix="Rp")
    discount_entry = add_row(1, "Diskon", suffix="%")
    quantity_entry = add_row(2, "Jumlah barang", suffix="pcs")

    # Pesan error (tempat tetap agar layout tidak bergeser)
    error_var = tk.StringVar()
    tk.Label(outer, textvariable=error_var, font=(base, 9), bg=BG, fg=DANGER,
             anchor="w", height=1).pack(fill=tk.X, pady=(8, 4))

    # Tombol
    buttons = ttk.Frame(outer, style="Bg.TFrame")
    buttons.pack(fill=tk.X)
    buttons.columnconfigure(0, weight=2)
    buttons.columnconfigure(1, weight=1)

    # Kartu hasil
    result = ttk.Frame(outer, style="Card.TFrame", padding=20)
    result.pack(fill=tk.X, pady=(16, 0))
    result.columnconfigure(1, weight=1)

    subtotal_var = tk.StringVar(value="Rp 0")
    discount_var = tk.StringVar(value="- Rp 0")
    total_var = tk.StringVar(value="Rp 0")

    ttk.Label(result, text="Subtotal", style="Muted.TLabel").grid(row=0, column=0, sticky="w")
    tk.Label(result, textvariable=subtotal_var, font=f_value, bg=CARD, fg=TEXT).grid(
        row=0, column=1, sticky="e")

    ttk.Label(result, text="Potongan diskon", style="Muted.TLabel").grid(
        row=1, column=0, sticky="w", pady=(6, 0))
    tk.Label(result, textvariable=discount_var, font=f_value, bg=CARD, fg=DANGER).grid(
        row=1, column=1, sticky="e", pady=(6, 0))

    ttk.Separator(result, orient="horizontal").grid(
        row=2, column=0, columnspan=2, sticky="ew", pady=12)

    ttk.Label(result, text="Total bayar", style="Card.TLabel").grid(row=3, column=0, sticky="w")
    tk.Label(result, textvariable=total_var, font=f_total, bg=CARD, fg=SUCCESS).grid(
        row=3, column=1, sticky="e")

    # Aksi
    def on_calculate(event=None) -> None:
        try:
            price = parse_float(price_entry.get().strip(), "Harga")
            rate = parse_float(discount_entry.get().strip() or "0", "Diskon")
            if rate > 100:
                raise ValueError("Diskon harus antara 0 dan 100.")
            qty = parse_int(quantity_entry.get().strip(), "Jumlah barang")
        except ValueError as exc:
            error_var.set(f"⚠ {exc}")
            return

        error_var.set("")
        subtotal, discount, total = calculate_final_total(price, rate, qty)
        subtotal_var.set(format_rupiah(subtotal))
        discount_var.set(f"- {format_rupiah(discount)}")
        total_var.set(format_rupiah(total))

    def on_clear() -> None:
        for entry in (price_entry, discount_entry, quantity_entry):
            entry.delete(0, tk.END)
        error_var.set("")
        subtotal_var.set("Rp 0")
        discount_var.set("- Rp 0")
        total_var.set("Rp 0")
        price_entry.focus()

    ttk.Button(buttons, text="Hitung", style="Primary.TButton",
               command=on_calculate).grid(row=0, column=0, sticky="ew", padx=(0, 8))
    ttk.Button(buttons, text="Reset", style="Secondary.TButton",
               command=on_clear).grid(row=0, column=1, sticky="ew")

    root.bind("<Return>", on_calculate)
    price_entry.focus()

    # Tengahkan jendela di layar
    root.update_idletasks()
    w, h = root.winfo_reqwidth(), root.winfo_reqheight()
    x = (root.winfo_screenwidth() - w) // 2
    y = (root.winfo_screenheight() - h) // 2
    root.geometry(f"+{x}+{y}")

    return root


if __name__ == "__main__":
    build_app().mainloop()