import tkinter as tk
from tkinter import messagebox

from contact import ContactBook


class ContactBookGUI:

    def __init__(self, root):

        self.root = root
        self.book = ContactBook()

        self.detail_window = None
        self.editing_contact = None

        # =========================================================
        # THEME
        # =========================================================

        self.dark_mode = False

        self.themes = {

            # =====================================================
            # LIGHT - REAL NOTEBOOK PAPER
            # =====================================================

            "light": {
                "bg": "#F3EBDD",
                "panel": "#F8F1E2",
                "input": "#FFFDF8",
                "text": "#24364B",
                "muted": "#7C7F82",

                "accent": "#B9473D",
                "hover": "#963B35",

                "button": "#2D3E57",
                "edit": "#40566F",
                "delete": "#B95750",
                "success": "#405F4A",

                "border": "#D8D2C4",
                "line": "#D7DEE6",
                "margin": "#C97972",
                "tag": "#F1DDD0"
            },

            # =====================================================
            # DARK
            # =====================================================

            "dark": {

                "bg": "#1E1E1E",
                "panel": "#252525",
                "input": "#2D2D2D",

                "text": "#F5F5F5",
                "muted": "#B5B5B5",

                "accent": "#FFFFFF",
                "hover": "#CCCCCC",

                "edit": "#BBBBBB",
                "delete": "#D66A6A",
                "success": "#78A982",

                "gray": "#777777",
                "border": "#444444",

                "line": "#3A3A3A",
                "margin": "#654545",

                "button_text": "#111111"
            }
        }

        self.apply_theme_variables()

        # =========================================================
        # WINDOW
        # =========================================================

        self.root.title("CONTACT BOOK")

        self.root.geometry("1000x750")

        self.root.minsize(
            850,
            650
        )

        self.root.configure(
            bg=self.bg
        )

        # =========================================================
        # BUILD GUI
        # =========================================================

        self.build_form()

        self.build_search_area()

        self.build_contact_list()

        self.refresh_list()

    # =============================================================
    # THEME VARIABLES
    # =============================================================

    def apply_theme_variables(self):

        if self.dark_mode:
            theme = self.themes["dark"]
        else:
            theme = self.themes["light"]

        self.bg = theme["bg"]
        self.panel = theme["panel"]
        self.input = theme["input"]

        self.text = theme["text"]
        self.muted = theme["muted"]

        self.accent = theme["accent"]
        self.hover = theme["hover"]

        self.edit_color = theme["edit"]
        self.delete_color = theme["delete"]
        self.success_color = theme["success"]

        # IMPORTANT:
        # Light theme does not have these values,
        # so we provide fallback values.

        self.gray = theme.get(
            "gray",
            "#555555"
        )

        self.button_text = theme.get(
            "button_text",
            "#FFFFFF"
        )

        self.border = theme["border"]

        self.line = theme["line"]
        self.margin = theme["margin"]

    # =============================================================
    # CONTACT DATA HELPER
    # =============================================================

    def get_contacts(self):

        if hasattr(self.book, "get_contacts"):
            return self.book.get_contacts()

        if hasattr(self.book, "people"):
            return self.book.people

        return {}

    # =============================================================
    # CREATE ENTRY
    # =============================================================

    def create_entry(self, parent):

        return tk.Entry(
            parent,
            bg=self.input,
            fg=self.text,
            insertbackground=self.text,
            relief="flat",
            font=("Segoe UI", 10),
            highlightthickness=1,
            highlightbackground=self.line,
            highlightcolor=self.text
        )

    # =============================================================
    # CREATE LABEL
    # =============================================================

    def create_label(self, parent, text):

        return tk.Label(
            parent,
            text=text,
            bg=self.panel,
            fg=self.text,
            font=("Consolas", 9, "bold")
        )

    # =============================================================
    # MAIN FORM
    # =============================================================

    def build_form(self):

        self.form = tk.Frame(
            self.root,
            bg=self.panel
        )

        self.form.pack(
            fill="x",
            padx=25,
            pady=(20, 15)
        )

        # =========================================================
        # TITLE
        # =========================================================

        self.title_label = tk.Label(
            self.form,
            text="CONTACT // BOOK",
            bg=self.panel,
            fg=self.accent,
            font=("Consolas", 26, "bold")
        )

        self.title_label.grid(
            row=0,
            column=0,
            columnspan=4,
            sticky="w",
            padx=20,
            pady=(20, 2)
        )

        self.subtitle_label = tk.Label(
            self.form,
            text="PERSONAL CONTACT MANAGEMENT SYSTEM",
            bg=self.panel,
            fg=self.muted,
            font=("Consolas", 9)
        )

        self.subtitle_label.grid(
            row=1,
            column=0,
            columnspan=4,
            sticky="w",
            padx=20,
            pady=(0, 20)
        )

        # =========================================================
        # NAME
        # =========================================================

        self.create_label(
            self.form,
            "NAME"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=(20, 5),
            pady=5
        )

        self.name_entry = self.create_entry(
            self.form
        )

        self.name_entry.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=5,
            pady=5,
            ipady=6
        )

        # =========================================================
        # PHONE
        # =========================================================

        self.create_label(
            self.form,
            "PHONE"
        ).grid(
            row=2,
            column=2,
            sticky="w",
            padx=5,
            pady=5
        )

        self.phone_entry = self.create_entry(
            self.form
        )

        self.phone_entry.grid(
            row=2,
            column=3,
            sticky="ew",
            padx=(5, 20),
            pady=5,
            ipady=6
        )

        # =========================================================
        # EMAIL
        # =========================================================

        self.create_label(
            self.form,
            "EMAIL"
        ).grid(
            row=3,
            column=0,
            sticky="w",
            padx=(20, 5),
            pady=5
        )

        self.email_entry = self.create_entry(
            self.form
        )

        self.email_entry.grid(
            row=3,
            column=1,
            sticky="ew",
            padx=5,
            pady=5,
            ipady=6
        )

        # =========================================================
        # ADDRESS
        # =========================================================

        self.create_label(
            self.form,
            "ADDRESS"
        ).grid(
            row=3,
            column=2,
            sticky="w",
            padx=5,
            pady=5
        )

        self.address_entry = self.create_entry(
            self.form
        )

        self.address_entry.grid(
            row=3,
            column=3,
            sticky="ew",
            padx=(5, 20),
            pady=5,
            ipady=6
        )

        # =========================================================
        # COMPANY
        # =========================================================

        self.create_label(
            self.form,
            "COMPANY"
        ).grid(
            row=4,
            column=0,
            sticky="w",
            padx=(20, 5),
            pady=5
        )

        self.company_entry = self.create_entry(
            self.form
        )

        self.company_entry.grid(
            row=4,
            column=1,
            sticky="ew",
            padx=5,
            pady=5,
            ipady=6
        )

        # =========================================================
        # JOB
        # =========================================================

        self.create_label(
            self.form,
            "JOB"
        ).grid(
            row=4,
            column=2,
            sticky="w",
            padx=5,
            pady=5
        )

        self.job_entry = self.create_entry(
            self.form
        )

        self.job_entry.grid(
            row=4,
            column=3,
            sticky="ew",
            padx=(5, 20),
            pady=5,
            ipady=6
        )

        # =========================================================
        # BIRTHDATE
        # =========================================================

        self.create_label(
            self.form,
            "BIRTHDATE"
        ).grid(
            row=5,
            column=0,
            sticky="w",
            padx=(20, 5),
            pady=5
        )

        self.birthdate_entry = self.create_entry(
            self.form
        )

        self.birthdate_entry.grid(
            row=5,
            column=1,
            sticky="ew",
            padx=5,
            pady=5,
            ipady=6
        )

        # =========================================================
        # TAGS
        # =========================================================

        self.create_label(
            self.form,
            "TAGS"
        ).grid(
            row=5,
            column=2,
            sticky="w",
            padx=5,
            pady=5
        )

        self.tags_entry = self.create_entry(
            self.form
        )

        self.tags_entry.grid(
            row=5,
            column=3,
            sticky="ew",
            padx=(5, 20),
            pady=5,
            ipady=6
        )

        # =========================================================
        # NOTES
        # =========================================================

        self.create_label(
            self.form,
            "NOTES"
        ).grid(
            row=6,
            column=0,
            sticky="nw",
            padx=(20, 5),
            pady=8
        )

        self.notes_entry = tk.Text(
            self.form,
            height=3,
            bg=self.input,
            fg=self.text,
            insertbackground=self.text,
            relief="flat",
            font=("Segoe UI", 10),
            wrap="word",
            highlightthickness=1,
            highlightbackground=self.line
        )

        self.notes_entry.grid(
            row=6,
            column=1,
            columnspan=3,
            sticky="ew",
            padx=(5, 20),
            pady=8
        )

        # =========================================================
        # ADD BUTTON
        # =========================================================

        self.action_button = tk.Button(
            self.form,
            text="+  ADD CONTACT",
            command=self.on_add,
            bg=self.accent,
            fg=self.button_text,
            activebackground=self.hover,
            activeforeground=self.button_text,
            relief="flat",
            borderwidth=0,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2"
        )

        self.action_button.grid(
            row=7,
            column=0,
            columnspan=4,
            sticky="ew",
            padx=20,
            pady=(10, 20),
            ipady=7
        )

        self.form.columnconfigure(
            1,
            weight=1
        )

        self.form.columnconfigure(
            3,
            weight=1
        )

    # =============================================================
    # SEARCH AREA
    # =============================================================

    def build_search_area(self):

        self.search_frame = tk.Frame(
            self.root,
            bg=self.panel
        )

        self.search_frame.pack(
            fill="x",
            padx=25,
            pady=(0, 15)
        )

        self.search_label = tk.Label(
            self.search_frame,
            text="SEARCH",
            bg=self.panel,
            fg=self.text,
            font=("Consolas", 10, "bold")
        )

        self.search_label.pack(
            side="left",
            padx=(15, 5)
        )

        self.search_entry = tk.Entry(
            self.search_frame,
            bg=self.input,
            fg=self.text,
            insertbackground=self.text,
            relief="flat",
            font=("Segoe UI", 10),
            highlightthickness=1,
            highlightbackground=self.line
        )

        self.search_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=5,
            pady=10,
            ipady=5
        )

        # SEARCH

        self.search_button = self.make_button(
            self.search_frame,
            "SEARCH",
            self.on_search,
            self.accent
        )

        self.search_button.pack(
            side="left",
            padx=3,
            ipadx=8,
            ipady=5
        )

        # VIEW

        self.view_button = self.make_button(
            self.search_frame,
            "VIEW",
            self.on_view,
            "#0284C7"
        )

        self.view_button.pack(
            side="left",
            padx=3,
            ipadx=8,
            ipady=5
        )

        # EDIT

        self.edit_button = self.make_button(
            self.search_frame,
            "EDIT",
            self.on_edit,
            self.edit_color
        )

        self.edit_button.pack(
            side="left",
            padx=3,
            ipadx=8,
            ipady=5
        )

        # DELETE

        self.delete_button = self.make_button(
            self.search_frame,
            "DELETE",
            self.on_delete,
            self.delete_color
        )

        self.delete_button.pack(
            side="left",
            padx=3,
            ipadx=8,
            ipady=5
        )

        # THEME

        self.theme_button = self.make_button(
            self.search_frame,
            "☾ DARK",
            self.toggle_theme,
            self.gray
        )

        self.theme_button.pack(
            side="right",
            padx=(10, 15),
            ipadx=8,
            ipady=5
        )

    # =============================================================
    # BUTTON HELPER
    # =============================================================

    def make_button(
        self,
        parent,
        text,
        command,
        color
    ):

        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg=self.button_text,
            activebackground=self.hover,
            activeforeground=self.button_text,
            relief="flat",
            borderwidth=0,
            font=("Segoe UI", 9, "bold"),
            cursor="hand2"
        )

    # =============================================================
    # CONTACT LIST
    # =============================================================

    def build_contact_list(self):

        self.container = tk.Frame(
            self.root,
            bg=self.bg
        )

        self.container.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(0, 20)
        )

        self.database_label = tk.Label(
            self.container,
            text="▸ CONTACT DATABASE",
            bg=self.bg,
            fg=self.accent,
            font=("Consolas", 11, "bold")
        )

        self.database_label.pack(
            anchor="w",
            pady=(0, 8)
        )

        self.list_frame = tk.Frame(
            self.container,
            bg=self.panel
        )

        self.list_frame.pack(
            fill="both",
            expand=True
        )

        self.listbox = tk.Listbox(
            self.list_frame,
            font=("Consolas", 10),
            bg=self.input,
            fg=self.text,
            selectbackground="#0284C7",
            selectforeground="white",
            activestyle="none",
            relief="flat",
            borderwidth=0
        )

        self.listbox.pack(
            fill="both",
            expand=True,
            side="left",
            padx=8,
            pady=8
        )

        self.scrollbar = tk.Scrollbar(
            self.list_frame,
            orient="vertical",
            command=self.listbox.yview
        )

        self.scrollbar.pack(
            side="right",
            fill="y"
        )

        self.listbox.config(
            yscrollcommand=self.scrollbar.set
        )

    # =============================================================
    # REFRESH LIST
    # =============================================================

    def refresh_list(self):

        self.listbox.delete(
            0,
            tk.END
        )

        contacts = self.get_contacts()

        if not contacts:

            self.listbox.insert(
                tk.END,
                "   [ DATABASE EMPTY ]"
            )

            return

        for name, info in contacts.items():

            phone = info.get(
                "phone",
                ""
            )

            self.listbox.insert(
                tk.END,
                f"  {name:<30} {phone}"
            )

    # =============================================================
    # GET FORM DATA
    # =============================================================

    def get_form_data(self):

        return {
            "name": self.name_entry.get().strip(),
            "phone": self.phone_entry.get().strip(),
            "email": self.email_entry.get().strip(),
            "address": self.address_entry.get().strip(),
            "company": self.company_entry.get().strip(),
            "job": self.job_entry.get().strip(),
            "birthdate": self.birthdate_entry.get().strip(),
            "notes": self.notes_entry.get(
                "1.0",
                tk.END
            ).strip(),
            "tags": self.tags_entry.get().strip()
        }

    # =============================================================
    # ADD CONTACT
    # =============================================================

    def on_add(self):

        data = self.get_form_data()

        ok, message = self.book.add_contact(
            **data
        )

        if not ok:

            messagebox.showerror(
                "ERROR",
                message
            )

            return

        self.clear_form()

        self.refresh_list()

        messagebox.showinfo(
            "SUCCESS",
            message
        )

    # =============================================================
    # SEARCH
    # =============================================================

    def on_search(self):

        query = self.search_entry.get().strip()

        if not query:

            messagebox.showwarning(
                "SEARCH",
                "Enter a name to search."
            )

            return

        ok, results = self.book.search(
            query
        )

        if not ok:

            messagebox.showwarning(
                "SEARCH",
                results
            )

            return

        if len(results) == 1:

            name, info = next(
                iter(results.items())
            )

            self.show_view_page(
                name,
                info
            )

        else:

            names = "\n".join(
                results.keys()
            )

            messagebox.showinfo(
                "SEARCH RESULTS",
                names
            )

    # =============================================================
    # SELECTED CONTACT
    # =============================================================

    def get_selected_contact(self):

        selected = self.listbox.curselection()

        if not selected:

            return None, None

        index = selected[0]

        contacts = list(
            self.get_contacts().items()
        )

        if index >= len(contacts):

            return None, None

        return contacts[index]

    # =============================================================
    # FIND CONTACT BY NAME
    # =============================================================

    def find_contact_by_name(self, name):

        contacts = self.get_contacts()

        for real_name, info in contacts.items():

            if real_name.lower() == name.lower():

                return real_name, info

        return None, None

    # =============================================================
    # VIEW
    # =============================================================

    def on_view(self):

        name = self.search_entry.get().strip()

        if name:

            real_name, info = self.find_contact_by_name(
                name
            )

            if real_name is not None:

                self.show_view_page(
                    real_name,
                    info
                )

                return

        name, info = self.get_selected_contact()

        if name is None:

            messagebox.showwarning(
                "VIEW",
                "Enter a contact name or select a contact from the list."
            )

            return

        self.show_view_page(
            name,
            info
        )

    # =============================================================
    # FULL VIEW PAGE
    # =============================================================

    def show_view_page(
        self,
        name,
        info
    ):

        if self.detail_window is not None:

            try:
                self.detail_window.destroy()

            except tk.TclError:
                pass

        window = tk.Toplevel(
            self.root
        )

        self.detail_window = window

        window.title(
            f"VIEW // {name}"
        )

        window.geometry(
            "1000x750"
        )

        window.minsize(
            800,
            650
        )

        window.configure(
            bg=self.bg
        )

        # =========================================================
        # HEADER
        # =========================================================

        header = tk.Frame(
            window,
            bg=self.panel
        )

        header.pack(
            fill="x",
            padx=25,
            pady=20
        )

        tk.Button(
            header,
            text="← BACK",
            command=lambda: self.close_detail_window(
                window
            ),
            bg=self.panel,
            fg=self.text,
            activebackground=self.input,
            activeforeground=self.text,
            relief="flat",
            borderwidth=0,
            font=("Segoe UI", 11, "bold"),
            cursor="hand2"
        ).pack(
            side="left",
            padx=10
        )

        tk.Label(
            header,
            text="CONTACT INFORMATION",
            bg=self.panel,
            fg=self.accent,
            font=("Consolas", 24, "bold")
        ).pack(
            side="left",
            padx=30
        )

        # =========================================================
        # INFORMATION CARD
        # =========================================================

        card = tk.Frame(
            window,
            bg=self.panel
        )

        card.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=20
        )

        fields = [

            ("NAME", name),

            (
                "PHONE",
                info.get("phone") or "Not provided"
            ),

            (
                "EMAIL",
                info.get("email") or "Not provided"
            ),

            (
                "ADDRESS",
                info.get("address") or "Not provided"
            ),

            (
                "COMPANY",
                info.get("company") or "Not provided"
            ),

            (
                "JOB",
                info.get("job") or "Not provided"
            ),

            (
                "BIRTHDATE",
                info.get("birthdate") or "Not provided"
            ),

            (
                "TAGS",
                info.get("tags") or "None"
            )
        ]

        for i, (label, value) in enumerate(fields):

            row = i // 2
            column = i % 2

            frame = tk.Frame(
                card,
                bg=self.input
            )

            frame.grid(
                row=row,
                column=column,
                sticky="ew",
                padx=12,
                pady=12
            )

            tk.Label(
                frame,
                text=label,
                bg=self.input,
                fg=self.text,
                font=("Consolas", 9, "bold")
            ).pack(
                anchor="w",
                padx=15,
                pady=(12, 2)
            )

            tk.Label(
                frame,
                text=value,
                bg=self.input,
                fg=self.text,
                font=("Segoe UI", 11),
                anchor="w"
            ).pack(
                fill="x",
                padx=15,
                pady=(0, 12)
            )

        card.columnconfigure(
            0,
            weight=1
        )

        card.columnconfigure(
            1,
            weight=1
        )

        # =========================================================
        # NOTES
        # =========================================================

        notes_frame = tk.Frame(
            card,
            bg=self.input
        )

        notes_frame.grid(
            row=4,
            column=0,
            columnspan=2,
            sticky="nsew",
            padx=12,
            pady=12
        )

        tk.Label(
            notes_frame,
            text="NOTES",
            bg=self.input,
            fg=self.text,
            font=("Consolas", 9, "bold")
        ).pack(
            anchor="w",
            padx=15,
            pady=(12, 5)
        )

        tk.Label(
            notes_frame,
            text=info.get("notes") or "No notes",
            bg=self.input,
            fg=self.text,
            font=("Segoe UI", 11),
            justify="left",
            anchor="nw",
            wraplength=800
        ).pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

        card.rowconfigure(
            4,
            weight=1
        )

        window.protocol(
            "WM_DELETE_WINDOW",
            lambda: self.close_detail_window(
                window
            )
        )

    # =============================================================
    # CLOSE VIEW
    # =============================================================

    def close_detail_window(
        self,
        window
    ):

        try:

            window.destroy()

        except tk.TclError:

            pass

        self.detail_window = None

    # =============================================================
    # EDIT
    # =============================================================

    def on_edit(self):

        name = self.search_entry.get().strip()

        if not name:

            messagebox.showwarning(
                "EDIT",
                "Enter the contact name in the SEARCH box first."
            )

            return

        real_name, info = self.find_contact_by_name(
            name
        )

        if real_name is None:

            messagebox.showwarning(
                "EDIT",
                f"Contact '{name}' was not found."
            )

            return

        self.show_edit_page(
            real_name,
            info
        )

    # =============================================================
    # EDIT PAGE
    # =============================================================

    def show_edit_page(
        self,
        old_name,
        info
    ):

        if self.detail_window is not None:

            try:
                self.detail_window.destroy()

            except tk.TclError:
                pass

        self.editing_contact = old_name

        window = tk.Toplevel(
            self.root
        )

        self.detail_window = window

        window.title(
            f"EDIT // {old_name}"
        )

        window.geometry(
            "1000x800"
        )

        window.minsize(
            850,
            700
        )

        window.configure(
            bg=self.bg
        )

        # =========================================================
        # HEADER
        # =========================================================

        header = tk.Frame(
            window,
            bg=self.panel
        )

        header.pack(
            fill="x",
            padx=25,
            pady=(20, 10)
        )

        tk.Button(
            header,
            text="← BACK",
            command=lambda: self.cancel_edit_page(
                window
            ),
            bg=self.panel,
            fg=self.text,
            activebackground=self.input,
            activeforeground=self.text,
            relief="flat",
            borderwidth=0,
            font=("Segoe UI", 11, "bold"),
            cursor="hand2"
        ).pack(
            side="left",
            padx=10
        )

        tk.Label(
            header,
            text="EDIT CONTACT",
            bg=self.panel,
            fg=self.edit_color,
            font=("Consolas", 24, "bold")
        ).pack(
            side="left",
            padx=30
        )

        # =========================================================
        # FORM
        # =========================================================

        content = tk.Frame(
            window,
            bg=self.panel
        )

        content.pack(
            fill="both",
            expand=True,
            padx=70,
            pady=(10, 0)
        )

        entries = {}

        fields = [

            ("NAME", "name"),
            ("PHONE", "phone"),
            ("EMAIL", "email"),
            ("ADDRESS", "address"),
            ("COMPANY", "company"),
            ("JOB", "job"),
            ("BIRTHDATE", "birthdate"),
            ("TAGS", "tags")
        ]

        for i, (label, key) in enumerate(fields):

            row = i // 2
            column = i % 2

            frame = tk.Frame(
                content,
                bg=self.panel
            )

            frame.grid(
                row=row,
                column=column,
                sticky="ew",
                padx=15,
                pady=10
            )

            tk.Label(
                frame,
                text=label,
                bg=self.panel,
                fg=self.text,
                font=("Consolas", 10, "bold")
            ).pack(
                anchor="w",
                pady=(0, 5)
            )

            entry = tk.Entry(
                frame,
                bg=self.input,
                fg=self.text,
                insertbackground=self.text,
                relief="flat",
                font=("Segoe UI", 11),
                highlightthickness=1,
                highlightbackground=self.line,
                highlightcolor=self.text
            )

            entry.pack(
                fill="x",
                ipady=8
            )

            if key == "name":

                value = old_name

            else:

                value = info.get(
                    key,
                    ""
                )

            entry.insert(
                0,
                value
            )

            entries[key] = entry

        content.columnconfigure(
            0,
            weight=1
        )

        content.columnconfigure(
            1,
            weight=1
        )

        # =========================================================
        # NOTES
        # =========================================================

        tk.Label(
            content,
            text="NOTES",
            bg=self.panel,
            fg=self.text,
            font=("Consolas", 10, "bold")
        ).grid(
            row=4,
            column=0,
            columnspan=2,
            sticky="w",
            padx=15,
            pady=(15, 5)
        )

        notes_entry = tk.Text(
            content,
            height=7,
            bg=self.input,
            fg=self.text,
            insertbackground=self.text,
            relief="flat",
            font=("Segoe UI", 11),
            wrap="word",
            highlightthickness=1,
            highlightbackground=self.line
        )

        notes_entry.grid(
            row=5,
            column=0,
            columnspan=2,
            sticky="nsew",
            padx=15,
            pady=5
        )

        notes_entry.insert(
            "1.0",
            info.get(
                "notes",
                ""
            )
        )

        content.rowconfigure(
            5,
            weight=1
        )

        # =========================================================
        # BUTTON BAR
        # =========================================================

        button_bar = tk.Frame(
            window,
            bg=self.bg
        )

        button_bar.pack(
            side="bottom",
            fill="x",
            padx=40,
            pady=25
        )

        # =========================================================
        # SAVE BUTTON
        # =========================================================

        save_button = tk.Button(
            button_bar,
            text="✓  SAVE CHANGES",
            command=lambda: self.save_edit_page(
                window,
                old_name,
                entries,
                notes_entry
            ),
            bg=self.success_color,
            fg="white",
            activebackground="#22C55E",
            activeforeground="white",
            relief="flat",
            borderwidth=0,
            font=("Segoe UI", 12, "bold"),
            cursor="hand2"
        )

        save_button.pack(
            side="left",
            ipadx=40,
            ipady=12,
            padx=(20, 10)
        )

        # =========================================================
        # CANCEL BUTTON
        # =========================================================

        cancel_button = tk.Button(
            button_bar,
            text="✕  CANCEL EDIT",
            command=lambda: self.cancel_edit_page(
                window
            ),
            bg=self.gray,
            fg="white",
            activebackground="#333333",
            activeforeground="white",
            relief="flat",
            borderwidth=0,
            font=("Segoe UI", 12, "bold"),
            cursor="hand2"
        )

        cancel_button.pack(
            side="left",
            ipadx=30,
            ipady=12,
            padx=10
        )

        # =========================================================
        # WINDOW X = CANCEL
        # =========================================================

        window.protocol(
            "WM_DELETE_WINDOW",
            lambda: self.cancel_edit_page(
                window
            )
        )

    # =============================================================
    # SAVE EDIT
    # =============================================================

    def save_edit_page(
        self,
        window,
        old_name,
        entries,
        notes_entry
    ):

        data = {

            "name": entries["name"].get().strip(),

            "phone": entries["phone"].get().strip(),

            "email": entries["email"].get().strip(),

            "address": entries["address"].get().strip(),

            "company": entries["company"].get().strip(),

            "job": entries["job"].get().strip(),

            "birthdate": entries["birthdate"].get().strip(),

            "tags": entries["tags"].get().strip(),

            "notes": notes_entry.get(
                "1.0",
                tk.END
            ).strip()
        }

        ok, message = self.book.update_contact(
            old_name,
            data["name"],
            data["phone"],
            data["email"],
            data["address"],
            data["company"],
            data["job"],
            data["birthdate"],
            data["notes"],
            data["tags"]
        )

        if not ok:

            messagebox.showerror(
                "EDIT ERROR",
                message
            )

            return

        self.editing_contact = None

        try:

            window.destroy()

        except tk.TclError:

            pass

        self.detail_window = None

        self.refresh_list()

        self.search_entry.delete(
            0,
            tk.END
        )

        messagebox.showinfo(
            "SUCCESS",
            message
        )

    # =============================================================
    # CANCEL EDIT
    # =============================================================

    def cancel_edit_page(
        self,
        window
    ):

        self.editing_contact = None

        try:

            window.destroy()

        except tk.TclError:

            pass

        self.detail_window = None

    # =============================================================
    # DELETE
    # =============================================================

    def on_delete(self):

        name = self.search_entry.get().strip()

        if not name:

            messagebox.showwarning(
                "DELETE",
                "Enter the exact contact name in the SEARCH box."
            )

            return

        real_name, info = self.find_contact_by_name(
            name
        )

        if real_name is None:

            messagebox.showwarning(
                "DELETE",
                "Contact not found."
            )

            return

        confirm = messagebox.askyesno(
            "CONFIRM DELETE",
            f"Delete '{real_name}'?"
        )

        if not confirm:

            return

        ok, message = self.book.delete(
            real_name
        )

        if ok:

            self.search_entry.delete(
                0,
                tk.END
            )

            self.refresh_list()

            messagebox.showinfo(
                "DELETED",
                message
            )

        else:

            messagebox.showwarning(
                "DELETE",
                message
            )

    # =============================================================
    # CLEAR FORM
    # =============================================================

    def clear_form(self):

        self.name_entry.delete(
            0,
            tk.END
        )

        self.phone_entry.delete(
            0,
            tk.END
        )

        self.email_entry.delete(
            0,
            tk.END
        )

        self.address_entry.delete(
            0,
            tk.END
        )

        self.company_entry.delete(
            0,
            tk.END
        )

        self.job_entry.delete(
            0,
            tk.END
        )

        self.birthdate_entry.delete(
            0,
            tk.END
        )

        self.tags_entry.delete(
            0,
            tk.END
        )

        self.notes_entry.delete(
            "1.0",
            tk.END
        )

    # =============================================================
    # DARK / LIGHT MODE
    # =============================================================

    def toggle_theme(self):

        self.dark_mode = not self.dark_mode

        self.apply_theme_variables()

        self.apply_theme_to_main_window()

        if self.detail_window is not None:

            try:

                current_title = self.detail_window.title()

            except tk.TclError:

                current_title = ""

            try:

                self.detail_window.destroy()

            except tk.TclError:

                pass

            self.detail_window = None

            if current_title.startswith("VIEW //"):

                contact_name = current_title.replace(
                    "VIEW // ",
                    "",
                    1
                )

                real_name, info = self.find_contact_by_name(
                    contact_name
                )

                if real_name:

                    self.show_view_page(
                        real_name,
                        info
                    )

            elif current_title.startswith("EDIT //"):

                contact_name = current_title.replace(
                    "EDIT // ",
                    "",
                    1
                )

                real_name, info = self.find_contact_by_name(
                    contact_name
                )

                if real_name:

                    self.show_edit_page(
                        real_name,
                        info
                    )

    # =============================================================
    # APPLY THEME TO MAIN WINDOW
    # =============================================================

    def apply_theme_to_main_window(self):

        # ROOT

        self.root.configure(
            bg=self.bg
        )

        # FORM

        self.form.configure(
            bg=self.panel
        )

        self.title_label.configure(
            bg=self.panel,
            fg=self.accent
        )

        self.subtitle_label.configure(
            bg=self.panel,
            fg=self.muted
        )

        # SEARCH

        self.search_frame.configure(
            bg=self.panel
        )

        self.search_label.configure(
            bg=self.panel,
            fg=self.text
        )

        self.search_entry.configure(
            bg=self.input,
            fg=self.text,
            insertbackground=self.text,
            highlightbackground=self.line
        )

        # CONTAINER

        self.container.configure(
            bg=self.bg
        )

        self.database_label.configure(
            bg=self.bg,
            fg=self.accent
        )

        self.list_frame.configure(
            bg=self.panel
        )

        self.listbox.configure(
            bg=self.input,
            fg=self.text,
            selectbackground="#0284C7",
            selectforeground="white"
        )

        # FORM ENTRIES

        entries = [

            self.name_entry,
            self.phone_entry,
            self.email_entry,
            self.address_entry,
            self.company_entry,
            self.job_entry,
            self.birthdate_entry,
            self.tags_entry
        ]

        for entry in entries:

            entry.configure(
                bg=self.input,
                fg=self.text,
                insertbackground=self.text,
                highlightbackground=self.line
            )

        self.notes_entry.configure(
            bg=self.input,
            fg=self.text,
            insertbackground=self.text,
            highlightbackground=self.line
        )

        # ADD BUTTON

        self.action_button.configure(
            bg=self.accent,
            fg=self.button_text,
            activebackground=self.hover,
            activeforeground=self.button_text
        )

        # SEARCH BUTTON

        self.search_button.configure(
            bg=self.accent,
            fg=self.button_text,
            activebackground=self.hover,
            activeforeground=self.button_text
        )

        # VIEW BUTTON

        self.view_button.configure(
            bg="#0284C7",
            fg="white",
            activebackground="#0369A1",
            activeforeground="white"
        )

        # EDIT BUTTON

        self.edit_button.configure(
            bg=self.edit_color,
            fg=self.button_text,
            activebackground=self.hover,
            activeforeground=self.button_text
        )

        # DELETE BUTTON

        self.delete_button.configure(
            bg=self.delete_color,
            fg="white",
            activebackground="#7F1D1D",
            activeforeground="white"
        )

        # THEME BUTTON

        if self.dark_mode:

            self.theme_button.configure(
                text="☀ LIGHT",
                bg="#777777",
                fg="white",
                activebackground="#555555",
                activeforeground="white"
            )

        else:

            self.theme_button.configure(
                text="☾ DARK",
                bg="#555555",
                fg="white",
                activebackground="#333333",
                activeforeground="white"
            )


# ================================================================
# START APPLICATION
# ================================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = ContactBookGUI(
        root
    )

    root.mainloop()