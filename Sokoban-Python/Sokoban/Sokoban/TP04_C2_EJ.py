from tkinter import Tk
from tkinter import ttk
from tkinter import IntVar
from tkinter import messagebox
from tkinter import PhotoImage
from functools import partial

def crear_matriz_num():
    #0 - camino
    #1 - pared
    #2 - caja móvil
    #3 - destino
    #4 - caja fija
    
    m_num = [[1,1,1,1,1,1,1,1,1,1],
             [1,3,0,0,0,0,0,0,0,1],
             [1,0,0,0,3,1,0,4,0,1],
             [1,0,4,0,1,1,0,0,0,1],
             [1,0,0,0,0,0,0,2,0,1],
             [1,0,2,0,4,0,0,1,1,1],
             [1,0,0,0,0,2,0,0,0,1],
             [1,0,1,1,0,1,0,0,0,1],
             [1,0,0,0,0,0,0,3,0,1],
             [1,1,1,1,1,1,1,1,1,1]]

    return m_num

def crear_matriz_img(fi, co):
    m_img = [None] * fi
    for i in range(fi):
        m_img[i] = [None] * co

    return m_img

def crear_vector_img():
    v_img = []
    str_nom = "soko-"
    str_ext = ".png"

    for i in range(6):
        v_img.append(PhotoImage(file=str_nom+str(i)+str_ext))

    return v_img


def crear_tablero_img(f, c, mat_img, mat_num, vec_img):
    for i in range(f):
        for j in range(c):
            mat_img[i][j] = ttk.Label(image = vec_img[mat_num[i][j]])
            mat_img[i][j].place(x=(32*j)+100, y=(32*i)+100, width=32, height=32)

            

def mueve_jugador(event):

    iv_pas.set(iv_pas.get() + 1)

    if (event.keysym == "Up") and (mat_num[fila.get()-1][columna.get()] != 1) and (mat_num[fila.get()-1][columna.get()] != 4):
         
        if (mat_num[fila.get() - 1][columna.get()] == 2):
        
            if (mat_num[fila.get() - 2][columna.get()] == 0) or (mat_num[fila.get()-2][columna.get()] == 3):
                
                if (mat_num[fila.get()-2][columna.get()] == 3):
                    
                    if (iv_des.get()<3):
                        iv_des.set(iv_des.get()+1)
                    
                    mat_num[fila.get()-2][columna.get()] = 4
                    mat_img[fila.get()-2][columna.get()].configure(image=vec_img[4])
                else:
                    mat_num[fila.get()-2][columna.get()] = 2
                    mat_img[fila.get()-2][columna.get()].configure(image=vec_img[2])
            
                mat_num[fila.get()-1][columna.get()] = 0
                mat_img[fila.get()-1][columna.get()].configure(image=vec_img[0])
                app.update()
                
        l_jugador.place(x = l_jugador.winfo_x(), y = l_jugador.winfo_y() - 32)
        fila.set(fila.get() - 1)
        
    elif (event.keysym == "Down") and (mat_num[fila.get() + 1][columna.get()] != 1) and (mat_num[fila.get() + 1][columna.get()] != 4):
         
        if (mat_num[fila.get() + 1][columna.get()] == 2):
        
            if (mat_num[fila.get() + 2][columna.get()] == 0) or (mat_num[fila.get() + 2][columna.get()] == 3):
                
                if (mat_num[fila.get() + 2][columna.get()] == 3):
                    
                    if (iv_des.get()<3):
                        iv_des.set(iv_des.get()+1)
                    
                    mat_num[fila.get()][columna.get()+2] = 4
                    mat_img[fila.get()][columna.get()+2].configure(image=vec_img[4])
                else:
                    mat_num[fila.get()+2][columna.get()] = 2
                    mat_img[fila.get()+2][columna.get()].configure(image=vec_img[2])
                    
                mat_num[fila.get()+1][columna.get()] = 0
                mat_img[fila.get()+1][columna.get()].configure(image=vec_img[0])
                app.update()
                
        l_jugador.place(x = l_jugador.winfo_x(), y = l_jugador.winfo_y() + 32)
        fila.set(fila.get() + 1)
        
    elif (event.keysym == "Right") and (mat_num[fila.get()][columna.get() + 1] != 1) and (mat_num[fila.get()][columna.get() + 1] != 4):
         
        if (mat_num[fila.get()][columna.get() + 1] == 2):
            
            if (mat_num[fila.get()][columna.get() + 2] == 0) or (mat_num[fila.get()][columna.get() + 2] == 3):
                
                if (mat_num[fila.get()][columna.get() + 2] == 3):
                    
                    if (iv_des.get()<3):
                        iv_des.set(iv_des.get()+1)
                    
                    mat_num[fila.get()][columna.get()+2] = 4
                    mat_img[fila.get()][columna.get()+2].configure(image=vec_img[4])
                else:
                    mat_num[fila.get()][columna.get()+2] = 2
                    mat_img[fila.get()][columna.get()+2].configure(image=vec_img[2])
                    
                mat_num[fila.get()][columna.get()+1] = 0
                mat_img[fila.get()][columna.get()+1].configure(image=vec_img[0])
                app.update()
                
        l_jugador.place(x = l_jugador.winfo_x()+ 32, y = l_jugador.winfo_y())
        columna.set(columna.get() + 1)
        
    elif (event.keysym == "Left") and (mat_num[fila.get()][columna.get() - 1] != 1) and (mat_num[fila.get()][columna.get() - 1] != 4):
         
        if (mat_num[fila.get()][columna.get() - 1] == 2):
        
            if (mat_num[fila.get()][columna.get() - 2] == 0) or (mat_num[fila.get()][columna.get() - 2] == 3):
                
                if (mat_num[fila.get()][columna.get() - 2] == 3):
                    
                    if (iv_des.get()<3):
                        iv_des.set(iv_des.get()+1)
                    
                    mat_num[fila.get()][columna.get()-2] = 4
                    mat_img[fila.get()][columna.get()-2].configure(image=vec_img[4])
                else:
                    mat_num[fila.get()][columna.get()-2] = 2
                    mat_img[fila.get()][columna.get()-2].configure(image=vec_img[2])
                    
                mat_num[fila.get()][columna.get()-1] = 0
                mat_img[fila.get()][columna.get()-1].configure(image=vec_img[0])
                app.update()
                
        l_jugador.place(x = l_jugador.winfo_x() - 32, y = l_jugador.winfo_y())
        columna.set(columna.get() - 1)
        
    if (iv_des.get()==3):
        messagebox.showinfo("Ganador!!", "Se completo el nivel con " + str(iv_pas.get()) + " pasos")

                
def mostrar_mat_num():
    
    for i in range(10):
        for j in range(10):
            print(mat_num[j][i], end=' ')
        print()
          


#-----------------------------------------------------------------------------------------------------------------#
#          PROGRAMA PRINCIPAL
#-----------------------------------------------------------------------------------------------------------------#
app = Tk()
app.geometry("500x500")
app.title("Sokoban ")

fila = IntVar()
columna = IntVar()
iv_pas = IntVar()
iv_des = IntVar()
fila.set(4)
columna.set(4)
iv_pas.set(0)
iv_des.set(0)

mat_num = crear_matriz_num()
mat_img = crear_matriz_img(10, 10)
vec_img = crear_vector_img()
crear_tablero_img(10, 10, mat_img, mat_num, vec_img)
#mostrar_mat_num()



l_jugador = ttk.Label(image=vec_img[5])
l_jugador.place(x=(32*fila.get())+100, y=(32*columna.get())+100, width=32, height=32)

app.bind("<Key>", mueve_jugador)

app.mainloop()

#fin
