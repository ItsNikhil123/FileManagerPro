import tkinter as tk
from tkinter import *
import windnd


class DragDropWidget(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Drag and Drop Widget")
        self.geometry("300x150")

        # Set the window always on top
        self.wm_attributes("-topmost", 1)

        # Label to display the dropped file name
        self.label = tk.Label(self, text="Drop a file here!", font=("Arial", 14))
        self.label.pack(pady=50)

        # Register drag and drop functionality
        Tkdnd.dnd_start(CurrentDir,self.drop_target)
        self.drop_target = windnd.DropTarget(self, drop=self.on_drop)

    def on_drop(self, files):
        file_path = files[0]  # Get the first dropped file
        self.label.config(text=f"File dropped:\n{file_path}")

def main():
    app = tk.Tk()
    app.title("Main App")

    def open_drag_drop_widget():
        drag_drop_widget = DragDropWidget(app)
        drag_drop_widget.mainloop()

    open_button = tk.Button(app, text="Open Drag and Drop Widget", command=open_drag_drop_widget)
    open_button.pack(pady=20)

    app.mainloop()

if __name__ == "__main__":
    main()
