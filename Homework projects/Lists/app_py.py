import tkinter as tk

# Define the main app class
class EraserApp:
    def __init__(self, root, grid_size=20, cell_size=30):
        self.root = root
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.canvas = tk.Canvas(root, width=grid_size * cell_size, height=grid_size * cell_size)
        self.canvas.pack()
        
        self.cells = {}
        self.eraser_size = 2  # Eraser size (2x2 cells)
        
        self.create_grid()
        self.create_eraser()
        
        self.canvas.bind("<B1-Motion>", self.move_eraser)  # Bind mouse drag event
    
    def create_grid(self):
        # Draw grid of blue cells
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                self.cells[cell] = (row, col)
    
    def create_eraser(self):
        # Draw the eraser as a white rectangle
        self.eraser = self.canvas.create_rectangle(0, 0, self.eraser_size * self.cell_size, self.eraser_size * self.cell_size, fill="white", outline="black")
    
    def move_eraser(self, event):
        # Get the mouse position and move the eraser accordingly
        x, y = event.x, event.y
        row = y // self.cell_size
        col = x // self.cell_size
        
        # Adjust eraser position
        x1 = col * self.cell_size
        y1 = row * self.cell_size
        x2 = x1 + self.eraser_size * self.cell_size
        y2 = y1 + self.eraser_size * self.cell_size
        
        # Move the eraser rectangle
        self.canvas.coords(self.eraser, x1, y1, x2, y2)
        
        # Erase the cells that the eraser is touching
        self.erase_cells(x1, y1, x2, y2)
    
    def erase_cells(self, x1, y1, x2, y2):
        # Find all cells that intersect with the eraser
        for cell in self.canvas.find_overlapping(x1, y1, x2, y2):
            self.canvas.itemconfig(cell, fill="white")  # Change color of cell to white

# Create the main window
root = tk.Tk()
root.title("Eraser Tool")

# Create the app instance
app = EraserApp(root)

# Run the application
root.mainloop()
