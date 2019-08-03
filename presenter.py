import tkinter as tk

class Presenter(tk.Frame):
    
    def __init__(self,slides=None):

        tk.Frame.__init__(self)
        self.slides = slides
        COLOR_BLACK = '#000000'
        COLOR_WHITE = '#ffffff'

        '''
        Aqui estão as configurações de geometria da janela de apresentação
        a geometria usa quatro parâmetros e cada um corresponde a uma 
        variável do objeto instanciado:

        Largura da janela - self.width
        Altura da janela - self.height
        Posição inicial no eixo x - self.pos_x
        Posição inicial no eixo y - self.pos_y

        Como essa é uma janela de apresentação ela já começa em tela cheia
        porém a tecla 'f' alterna entre tela cheia e janela. Esse estado 
        inicial pode ser alterado mudando a variável self.is_fullscreen
        '''

        self.master.configure(bg=COLOR_BLACK)
        self.master.attributes('-fullscreen',True)

        #Titulo da janela
        self.master.title('Apresentação')

        #Bindings de Teclas
        self.master.bind('<Escape>',self.close_window)
        self.master.bind('<q>',self.close_window)
        self.master.bind('<Q>',self.close_window)
        self.master.bind('<Left>',self.previous_slide)
        self.master.bind('<Right>',self.next_slide)

        #Widgets
        canvas_width, canvas_height = self.get_canvas_size()

        self.canvas_frame = tk.Frame(self.master)
        self.canvas_frame.pack()

        self.canvas = tk.Canvas(self.canvas_frame,height=canvas_height,width=canvas_width,bg=COLOR_WHITE)
        self.canvas.pack(side=tk.TOP,fill=tk.Y)

        self.master.mainloop()

    def get_canvas_size(self):
        screen_height = self.master.winfo_screenheight()
        canvas_height = screen_height
        canvas_width = int(screen_height * (4/3))

        return (canvas_width,canvas_height)

    def close_window(self,event):
        self.quit()

    def next_slide(self,event=None):
        print('next')

    def previous_slide(self,event=None):
        print('previous')


Presenter()
