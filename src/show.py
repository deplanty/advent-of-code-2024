import tkinter as tk
import typing

if typing.TYPE_CHECKING:
    from .index import Index


class Show(tk.Tk):
    def __init__(self, scale:int=10):
        super().__init__()

        self.scale = scale

        self.canvas = tk.Canvas(self, background="white")
        self.canvas.pack(fill="both", expand=True)

        self.table_iids = set()
        self.coords_iids = set()

        self.geometry("+20+20")

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
                j * self.scale + 1,
                i * self.scale + 1,
                (j + 1) * self.scale - 1,
                (i + 1) * self.scale - 1,
                fill=color,
                outline="",
            )
            self.coords_iids.add(iid)

    def show_path(self, coords: list["Index"], color:str = "black"):
        for i in range(len(coords) - 1):
            a = coords[i]
            b = coords[i + 1]
            iid = self.canvas.create_line(
                a.j * self.scale + self.scale / 2,
                a.i * self.scale + self.scale / 2,
                b.j * self.scale + self.scale / 2,
                b.i * self.scale + self.scale / 2,
                fill=color,
                width=self.scale / 4,
                arrow="last"
            )
            self.coords_iids.add(iid)


if __name__ == '__main__':
    app = Show()
    app.mainloop()
