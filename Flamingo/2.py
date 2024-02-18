import tkinter as tk

# create the main window
window = tk.Tk()
window.title("Drag and Drop Files")

# create a frame for the file list
frame = tk.Frame(window)

# create a label to display the list
label = tk.Label(frame, anchor="w", width=350)
label.pack(side="left", fill="x")

# create a frame for the listbox
listbox_frame = tk.Frame(window)

# create the listbox
listbox = tk.Listbox(listbox_frame, width=350, selectmode=tk.SINGLE, exportselection=False)
listbox.pack(side="left", fill="both", expand=True)
listbox_frame.pack(side="bottom", fill="both", expand=True)

# create a frame to receive the dropped files
drop_frame = tk.Frame(window, width=350, height=350)
drop_frame.pack(side="top", fill="both", expand=True)

# create a label to display the dropped files
drop_label = tk.Label(drop_frame, anchor="w", width=350, height=350)
drop_label.pack(side="left", fill="both", expand=True)

# create a function to handle the drag and drop event
def handle_drag_and_drop(event):
    filename = event.data
    drop_label.config(text=f"Dropped file: {filename}")

window.drop_target_register(drop_frame)
window.callback_register("drop_target_event", handle_drag_and_drop)

window.mainloop()
