import tkinter as tk
from src.breadth_first_search import breadth_first_search
from src.depth_first_search import depth_first_search
from src.gradual_depth_first_search import gradual_depth_first_search
from src.Dijkstra_algorithm import Dijkstra_algorithm
from src.grath_G4 import g4


class MyApp(tk.Frame):
    def __init__(self, grath: dict, master=None):
        super().__init__(master, width=600, height=400)
        self.master = master
        self.grath, self.nodes = self.initGraph(grath)
        self.initUI()

    def initGraph(self, grath: dict = g4):
        nodes = [x for x in grath]
        return grath, nodes

    def initUI(self):
        self.master.title("Интеллектуальные системы (ЛР2) Освоение методов поиска")

        # Изменим позицию окна на экране
        self.master.geometry("600x400+50+50")

        self.pack(fill=tk.BOTH, expand=True)

        # Первый параметр
        label1 = tk.Label(self, text="Initial peak")
        label1.place(x=250, y=20)

        self.var1 = tk.StringVar(self)
        self.var1.set(self.nodes[0])

        self.option1 = tk.OptionMenu(self, self.var1, *self.nodes)
        self.option1.place(x=250, y=40)

        # Второй параметр
        label2 = tk.Label(self, text="Terminal peak")
        label2.place(x=250, y=70)

        self.var2 = tk.StringVar(self)
        self.var2.set(self.nodes[-1])

        self.option2 = tk.OptionMenu(self, self.var2, *self.nodes)
        self.option2.place(x=250, y=90)

        # Третий параметр
        label3 = tk.Label(self, text="Search method")
        label3.place(x=250, y=120)

        self.var3 = tk.StringVar(self)
        self.var3.set("select")

        self.option3 = tk.OptionMenu(self, self.var3, "breadth_first_search", "depth_first_search", "gradual_depth_first_search", "Dijkstra_algorithm")
        self.option3.place(x=250, y=140)

        # Вывод выбранных значений
        self.label_result = tk.Label(self, text="")
        self.label_result.place(x=250, y=230)

        # Кнопка получения значений
        btn = tk.Button(self, text="Result", command=self.show_values)
        btn.place(x=250, y=190)


    def show_values(self):
        list_func = {
            "breadth_first_search": breadth_first_search,
            "depth_first_search": depth_first_search,
            "gradual_depth_first_search": gradual_depth_first_search,
            "Dijkstra_algorithm": Dijkstra_algorithm
        }

        func = list_func[self.var3.get()]
        path, length, num_vertices = func(self.grath, self.var1.get(), self.var2.get())


        self.label_result.configure(
            text=f"""
            Путь: {path}\n
            Длина пути (L): {length}
            Количество посещенных вершин (K): {num_vertices}
            """)


if __name__ == '__main__':
    root = tk.Tk()
    app = MyApp(master=root, grath=g4)
    app.mainloop()