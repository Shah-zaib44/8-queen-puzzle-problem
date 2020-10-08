from tkinter import *
root=Tk()
photo=PhotoImage(file="E:/crown (1).png")
yellow='yellow'
orange='orange'
N = int(input())
def is_safe(x,y,board,N):
  # try to find the safe position
  # we will be checking Row
  for i in range(N) :
    if board[x][i].cget('image') :
      return 0
  # we will be checking Columns
  for i in range(N) :
    if board[i][y].cget('image') :
      return 0
  # checking diagonals
  for i in range(N) :
    for j in range(N) :
      if (i+j) == (x+y) :
        if board[i][j].cget('image') :
          return 0
      if (i-j) == (x-y) :
        if board[i][j].cget('image') :
          return 0
  return 1
def n_q(board,i,N):
  if i == N :
    return True
  else :
    for j in range(N) :
      if is_safe(i,j,board,N) :
        if i%2==0:
                if j%2==0:
                    board[i][j]=Button(root,bg=yellow,image=photo)
                    board[i][j].grid(row=i,column=j)
                    
                    
                else:
                    board[i][j]=Button(root,bg=orange,image=photo)
                    board[i][j].grid(row=i,column=j)
                    
        else:
                 if j%2==0:
                    board[i][j]=Button(root,bg=orange,image=photo)
                    board[i][j].grid(row=i,column=j)
                   
                 else:
                    board[i][j]=Button(root,bg=yellow,image=photo)
                    board[i][j].grid(row=i,column=j)
                    
       
        if n_q(board,i+1,N) :
          return True
        if i%2==0:
                if j%2==0:
                    board[i][j]=Button(root,height=2,width=5,bg=yellow)
                    board[i][j].grid(row=i,column=j)
                   
                else:
                    board[i][j]=Button(root,height=2,width=5,bg=orange)
                    board[i][j].grid(row=i,column=j)
                   
        else:
                 if j%2==0:
                    board[i][j]=Button(root,height=2,width=5,bg=orange)
                    board[i][j].grid(row=i,column=j)
                    
                 else:
                    board[i][j]=Button(root,height=2,width=5,bg=yellow)
                    board[i][j].grid(row=i,column=j)
                    
    return False 
def make(N):
    board = [[0 for x in range(N)] for y in range(N)]
    for i in range(N):
        for j in range(N):
            if i%2==0:
                if j%2==0:
                    board[i][j]=Button(root,height=2,width=5,bg=yellow)
                    board[i][j].grid(row=i,column=j)
                   
                else:
                    board[i][j]=Button(root,height=2,width=5,bg=orange)
                    board[i][j].grid(row=i,column=j)
                   
            else:
                 if j%2==0:
                    board[i][j]=Button(root,height=2,width=5,bg=orange)
                    board[i][j].grid(row=i,column=j)
                   
                 else:
                    board[i][j]=Button(root,height=2,width=5,bg=yellow)
                    board[i][j].grid(row=i,column=j)
                    
    return board
board = make(N) 
n_q(board,0,N)
            
            
            
    
