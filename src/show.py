import tkinter as tk


class Show(tk.Tk):
    def __init__(self, scale:int=10):
        super().__init__()

        self.scale = scale

        self.canvas = tk.Canvas(self, background="white")
        self.canvas.pack(fill="both", expand=True)

        self.table_iids = set()
        self.coords_iids = set()

    def show_table(self, table:list[list], colormap:dict):
        for i, line in enumerate(table):
            for j, char in enumerate(line):
                if char not in colormap:
                    continue
                iid = self.canvas.create_rectangle(
                    j * self.scale,
                    i * self.scale,
                    (j + 1) * self.scale,
                    (i + 1) * self.scale,
                    fill = colormap[char],
                    outline="",
                )
                self.table_iids.add(iid)

    def show_coords(self, coords:list, color:str):
        for index in coords:
            i, j = index.ij
            iid = self.canvas.create_rectangle(
                j * self.scale,
                i * self.scale,
                (j + 1) * self.scale,
                (i + 1) * self.scale,
                fill=color,
                outline="",
            )
            self.coords_iids.add(iid)



if __name__ == '__main__':
    app = Show()
    app.mainloop()
