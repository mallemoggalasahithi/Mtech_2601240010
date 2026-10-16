import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

from src.exporters import export_to_csv, export_to_json
from src.filters import (
    filter_by_severity,
    filter_by_user,
    search_events,
)
from src.timeline import build_timeline, get_all_events


# ================= CYBER DARK THEME =================

BG = "#080D18"
PANEL = "#111A2B"
INPUT_BG = "#0B1322"
TABLE_BG = "#0C1424"

CYAN = "#00E5FF"
CYAN_HOVER = "#00BFD6"
BLUE = "#176BFF"
BLUE_HOVER = "#1054CC"

TEXT = "#E6F1FF"
MUTED = "#91A4C0"
BORDER = "#263750"
SELECT_BG = "#164E75"

LOG_FILES = [
    "data/system.log",
    "data/application.log",
    "data/browser.log",
    "data/auth.log",
]

timeline = []


def show_events(events):
    """Display events in the table."""
    for row in table.get_children():
        table.delete(row)

    for event in events:
        table.insert(
            "",
            "end",
            values=(
                event.timestamp,
                event.source,
                event.event_type,
                event.user,
                event.description,
                event.severity,
            ),
                tags=(event.severity,),
        )

    total_label.config(text=f"Total Events: {len(events)}")


def refresh_view():
    """Apply search, filters, and selected sorting order."""
    results = list(timeline)

    severity = severity_combo.get()
    user = user_combo.get()
    keyword = search_entry.get().strip()

    if severity != "ALL":
        results = filter_by_severity(results, severity)

    if user != "ALL":
        results = filter_by_user(results, user)

    if keyword:
        results = search_events(results, keyword)

    if sort_order_combo.get() == "Descending (Newest First)":
        results.reverse()

    show_events(results)

    if keyword:
        status_label.config(
            text=f"Search results for '{keyword}': {len(results)}"
        )
    elif severity != "ALL" and user != "ALL":
        status_label.config(
            text=f"{severity} events for {user}: {len(results)}"
        )
    elif severity != "ALL":
        status_label.config(
            text=f"{severity} events: {len(results)}"
        )
    elif user != "ALL":
        status_label.config(
            text=f"{user} events: {len(results)}"
        )
    else:
        status_label.config(
            text=f"Showing {len(results)} events."
        )


def load_timeline():
    """Load log files and build the chronological timeline."""
    global timeline

    try:
        events = get_all_events(LOG_FILES)
        timeline = build_timeline(events)

        refresh_view()

        status_label.config(
            text=f"Timeline loaded successfully: {len(timeline)} events."
        )

    except Exception as error:
        messagebox.showerror(
            "Error",
            f"Could not load timeline:\n{error}",
        )


def show_search_results():
    refresh_view()


def filter_severity():
    refresh_view()


def filter_user():
    refresh_view()


def change_sort_order(event=None):
    refresh_view()


def clear_filters():
    search_entry.delete(0, tk.END)
    severity_combo.set("ALL")
    user_combo.set("ALL")
    sort_order_combo.set("Ascending (Oldest First)")

    refresh_view()
    status_label.config(
        text="Filters cleared. Showing oldest events first."
    )


def export_csv():
    """Export the complete timeline to CSV."""
    if not timeline:
        messagebox.showwarning(
            "Warning",
            "Load the timeline first.",
        )
        return

    file_path = filedialog.asksaveasfilename(
        title="Save CSV File",
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
    )

    if file_path:
        try:
            export_to_csv(timeline, Path(file_path))
            messagebox.showinfo(
                "Success",
                "Timeline exported to CSV successfully.",
            )
        except Exception as error:
            messagebox.showerror(
                "Export Error",
                f"Could not export CSV:\n{error}",
            )


def export_json():
    """Export the complete timeline to JSON."""
    if not timeline:
        messagebox.showwarning(
            "Warning",
            "Load the timeline first.",
        )
        return

    file_path = filedialog.asksaveasfilename(
        title="Save JSON File",
        defaultextension=".json",
        filetypes=[("JSON files", "*.json")],
    )

    if file_path:
        try:
            export_to_json(timeline, Path(file_path))
            messagebox.showinfo(
                "Success",
                "Timeline exported to JSON successfully.",
            )
        except Exception as error:
            messagebox.showerror(
                "Export Error",
                f"Could not export JSON:\n{error}",
            )


def main():
    global table
    global total_label
    global search_entry
    global severity_combo
    global user_combo
    global sort_order_combo
    global status_label

    root = tk.Tk()
    root.title("Digital Forensics Timeline Builder")
    root.geometry("1300x750")
    root.minsize(900, 550)
    root.configure(bg=BG)

    # ================= TTK CYBER STYLING =================

    style = ttk.Style(root)
    style.theme_use("clam")

    style.configure(
        "Cyber.Treeview",
        background=TABLE_BG,
        foreground=TEXT,
        fieldbackground=TABLE_BG,
        rowheight=34,
        font=("Consolas", 10),
        borderwidth=0,
    )

    style.configure(
        "Cyber.Treeview.Heading",
        background=PANEL,
        foreground=CYAN,
        font=("Arial", 10, "bold"),
        padding=(8, 12),
        relief="flat",
    )

    style.map(
        "Cyber.Treeview",
        background=[("selected", SELECT_BG)],
        foreground=[("selected", CYAN)],
    )

    style.map(
        "Cyber.Treeview.Heading",
        background=[("active", SELECT_BG)],
        foreground=[("active", CYAN)],
    )

    style.configure(
        "Cyber.TCombobox",
        fieldbackground=INPUT_BG,
        background=PANEL,
        foreground=TEXT,
        arrowcolor=CYAN,
        bordercolor=BORDER,
        lightcolor=BORDER,
        darkcolor=BORDER,
        padding=6,
    )

    style.map(
        "Cyber.TCombobox",
        fieldbackground=[("readonly", INPUT_BG)],
        foreground=[("readonly", TEXT)],
        selectbackground=[("readonly", INPUT_BG)],
        selectforeground=[("readonly", TEXT)],
    )

    style.configure(
        "Cyber.Vertical.TScrollbar",
        background=PANEL,
        troughcolor=BG,
        arrowcolor=CYAN,
        bordercolor=BG,
    )

    style.configure(
        "Cyber.Horizontal.TScrollbar",
        background=PANEL,
        troughcolor=BG,
        arrowcolor=CYAN,
        bordercolor=BG,
    )

    # ================= HELPER FUNCTIONS =================

    def make_label(parent, text, color=TEXT, size=10, bold=False):
        return tk.Label(
            parent,
            text=text,
            bg=parent.cget("bg"),
            fg=color,
            font=("Arial", size, "bold" if bold else "normal"),
        )

    def make_button(parent, text, command, primary=False):
        normal = BLUE if primary else PANEL
        hover = BLUE_HOVER if primary else SELECT_BG

        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=normal,
            fg=CYAN if not primary else "#FFFFFF",
            activebackground=hover,
            activeforeground="#FFFFFF",
            font=("Arial", 10, "bold"),
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=14,
            pady=7,
            highlightthickness=1,
            highlightbackground=BORDER,
            highlightcolor=CYAN,
        )

    # ================= HEADER =================

    header_frame = tk.Frame(root, bg=BG)
    header_frame.pack(fill="x", pady=(22, 4))

    title = tk.Label(
        header_frame,
        text="DIGITAL FORENSICS TIMELINE BUILDER",
        font=("Arial", 22, "bold"),
        bg=BG,
        fg=CYAN,
    )
    title.pack()

    subtitle = tk.Label(
        header_frame,
        text="// ANALYZE  •  TRACE  •  INVESTIGATE",
        font=("Consolas", 10),
        bg=BG,
        fg=MUTED,
    )
    subtitle.pack(pady=(7, 10))

    tk.Frame(
        root,
        bg=CYAN,
        height=2,
    ).pack(fill="x", padx=35, pady=(0, 12))

    make_button(
        root,
        "▶  LOAD TIMELINE",
        load_timeline,
        primary=True,
    ).pack(pady=7)

    # ================= CONTROL PANEL =================

    controls_frame = tk.Frame(
        root,
        bg=PANEL,
        highlightbackground=BORDER,
        highlightthickness=1,
    )
    controls_frame.pack(
        fill="x",
        padx=25,
        pady=12,
    )

    # Search
    make_label(
        controls_frame, "SEARCH", CYAN, bold=True
    ).pack(side=tk.LEFT, padx=(12, 5), pady=14)

    search_entry = tk.Entry(
        controls_frame,
        width=17,
        font=("Consolas", 10),
        bg=INPUT_BG,
        fg=TEXT,
        insertbackground=CYAN,
        relief="flat",
        highlightthickness=1,
        highlightbackground=BORDER,
        highlightcolor=CYAN,
    )
    search_entry.pack(side=tk.LEFT, padx=5, ipady=7)

    make_button(
        controls_frame, "Search", show_search_results
    ).pack(side=tk.LEFT, padx=4)

    # Severity
    make_label(
        controls_frame, "SEVERITY", CYAN, bold=True
    ).pack(side=tk.LEFT, padx=(10, 4))

    severity_combo = ttk.Combobox(
        controls_frame,
        values=["ALL", "NORMAL", "WARNING", "ERROR"],
        state="readonly",
        width=9,
        style="Cyber.TCombobox",
    )
    severity_combo.set("ALL")
    severity_combo.pack(side=tk.LEFT, padx=4, ipady=2)

    make_button(
        controls_frame, "Filter", filter_severity
    ).pack(side=tk.LEFT, padx=3)

    # User
    make_label(
        controls_frame, "USER", CYAN, bold=True
    ).pack(side=tk.LEFT, padx=(9, 4))

    user_combo = ttk.Combobox(
        controls_frame,
        values=["ALL", "user1", "admin"],
        state="readonly",
        width=9,
        style="Cyber.TCombobox",
    )
    user_combo.set("ALL")
    user_combo.pack(side=tk.LEFT, padx=4, ipady=2)

    make_button(
        controls_frame, "Filter", filter_user
    ).pack(side=tk.LEFT, padx=3)

    # Sorting
    make_label(
        controls_frame, "SORT", CYAN, bold=True
    ).pack(side=tk.LEFT, padx=(9, 4))

    sort_order_combo = ttk.Combobox(
        controls_frame,
        values=[
            "Ascending (Oldest First)",
            "Descending (Newest First)",
        ],
        state="readonly",
        width=23,
        style="Cyber.TCombobox",
    )
    sort_order_combo.set("Ascending (Oldest First)")
    sort_order_combo.pack(side=tk.LEFT, padx=4, ipady=2)
    sort_order_combo.bind(
        "<<ComboboxSelected>>",
        change_sort_order,
    )

    make_button(
        controls_frame, "Clear", clear_filters
    ).pack(side=tk.LEFT, padx=(5, 10))

    # ================= EVENTS TABLE =================

    table_frame = tk.Frame(
        root,
        bg=PANEL,
        highlightbackground=BORDER,
        highlightthickness=1,
    )
    table_frame.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=(3, 10),
    )

    columns = (
        "Timestamp",
        "Source",
        "Event Type",
        "User",
        "Description",
        "Severity",
    )

    table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        style="Cyber.Treeview",
    )

    widths = {
        "Timestamp": 160,
        "Source": 120,
        "Event Type": 140,
        "User": 100,
        "Description": 450,
        "Severity": 100,
    }

    for column in columns:
        table.heading(column, text=column.upper())
        table.column(
            column,
            width=widths[column],
            minwidth=80,
        )

    # Severity colors are visual only
    table.tag_configure("NORMAL", foreground="#65E6A5")
    table.tag_configure("WARNING", foreground="#FFD166")
    table.tag_configure("ERROR", foreground="#FF647C")

    vertical_scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=table.yview,
        style="Cyber.Vertical.TScrollbar",
    )

    horizontal_scrollbar = ttk.Scrollbar(
        table_frame,
        orient="horizontal",
        command=table.xview,
        style="Cyber.Horizontal.TScrollbar",
    )

    table.configure(
        yscrollcommand=vertical_scrollbar.set,
        xscrollcommand=horizontal_scrollbar.set,
    )

    table.grid(row=0, column=0, sticky="nsew")
    vertical_scrollbar.grid(row=0, column=1, sticky="ns")
    horizontal_scrollbar.grid(row=1, column=0, sticky="ew")

    table_frame.rowconfigure(0, weight=1)
    table_frame.columnconfigure(0, weight=1)

    # ================= EXPORT PANEL =================

    export_frame = tk.Frame(root, bg=BG)
    export_frame.pack(pady=5)

    make_button(
        export_frame,
        "⇩  EXPORT CSV",
        export_csv,
    ).pack(side=tk.LEFT, padx=10)

    make_button(
        export_frame,
        "⇩  EXPORT JSON",
        export_json,
    ).pack(side=tk.LEFT, padx=10)

    # ================= STATUS BAR =================

    total_label = tk.Label(
        root,
        text="Total Events: 0",
        font=("Consolas", 11, "bold"),
        bg=BG,
        fg=CYAN,
    )
    total_label.pack(pady=(8, 3))

    status_label = tk.Label(
        root,
        text="Ready. Click 'Load Timeline' to begin.",
        font=("Consolas", 9),
        bg=BG,
        fg=MUTED,
    )
    status_label.pack(pady=(0, 12))

    root.mainloop()


if __name__ == "__main__":
    main()