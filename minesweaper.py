import random 

grid = []
complete_grid = []
show = []
stop = False
booms_len = 0       
size = 9

def create_grid(size):	
    local_grid = [[0 for x in range(0,size)] for i in range(0,size)]
    local_grid= create_booms(local_grid,size)
    local_grid = add_numbers(local_grid)
    return local_grid
        

def create_booms(grid,size):
    global booms_len
    rnd = random.randint(6,8)
    booms = [[random.randint(0,size-1),random.randint(0,size-1)] for x in range(1,rnd) ]
   # grid = [grid[i[0]][i[1]] 4 for i in booms 4]
    booms_len = rnd
    for i in booms:
        grid[i[0]][i[1]] = 4
        #print(i[0]," "i[1])
    	
    return grid
        

def add_numbers(grid):
    global complete_grid
    for x,g in enumerate(grid):
        for y,f in enumerate(g):
       	    #if value is a boom	
            if f == 4 :
                num = 0
                #get above cell
                    #check if its not last row
                if x != size-1:
                    if grid[x+1][y]  == 0 :
                        num = num+1
			#check if its not the last row
                    if x != size-2:
                        if grid[x+2][y] == 4:
                           num = num+1
                           pass
                    if y != size-1:				
                       if grid[x+1][y+1] == 4:
                           num = num+1
                       if y != 0:						
                          if grid[x+1][y-1] == 4:
                              pass
                             #num = num+1
                    if grid[x+1][y] < 4:
                       grid[x+1][y] = grid[x+1][y]+num
                #get below cell
                num = 0
                #dont check the first row
                if x != 0:
                    if grid[x-1][y] == 0:
                        num = num +1
                    #check if its not the last row
                    if x-2 < 0:
                        if grid[x-2][y] == 4:
                            num = num +1
                    if y != size-1:
                        if grid[x-1][y+1] == 4:
                            num = num +1
                    if y != 0:
                        if grid[x-1][y-1] == 4:
                            pass
                            #num = num +1
                    if grid[x-1][y] < 4:
                       grid[x-1][y] = grid[x-1][y]+num
           
                #get left cell
                num = 0     
                if y != size-1:
                    if grid[x][y+1] != 4:
                        num = num+1
                    if y != size-2:    
                        if grid[x][y+2] == 4:
                            num = num+1
                    if x != size-1:        
                        if grid[x+1][y+1] == 4:
                            num = num +1
                        if x != 0:
                            if grid[x+1][y-1] == 4:
                               pass
                               #num = num +1
                    if grid[x][y+1] < 4:
                       grid[x][y+1] = grid[x][y+1]+num 

                #get right cell
                num = 0
                if y != size-1:
                    if grid[x][y-1] != 4:
                        num = num+1
                    if y != size-2:    
                        if grid[x][y-2] == 4:
                            num = num+1
                    if x != size-1:        
                        if grid[x-1][y-1] == 4:
                            num = num +1
                        if x != 0:
                            if grid[x-1][y+1] == 4:
                                pass
                                #num = num +1
                    if grid[x][y-1] < 4:
                       grid[x][y-1] = grid[x][y-1]+num   
             #fix the number after adding them to the gird
                 
                if y != size-1 :
                    if grid[x][y-1] == 4:
                       pass
                       #grid[x][y-1] = 2
                    elif grid[x][y-1] > 4:
                       grid[x][y-1] = 3
                    elif grid[x][y+1] == 4:
                       pass
                       #grid[x][y+1] =2
                    elif grid[x][y+1] > 4:
                       grid[x][y+1] = 3
                if x != size-1:
                    if grid[x+1][y] == 4:
                       pass
                       #grid[x+1][y] = 2
                    elif grid[x+1][y] > 4:
                       grid[x+1][y] = 3
                    elif grid[x-1][y] == 4:
                       pass
                       #grid[x-1][y] = 2
                    elif grid[x-1][y] > 4:
                       grid[x-1][y] = 3 
    complete_grid = grid 
    return grid                 

def recurse(empty_list):
    global show
    count_zero = 0
    for x in grid:
       for i in x:
           if i == 0:
              count_zero = count_zero+1			   	 
    for x in empty_list:			
       #check the right cell for empty cell
       if x[1]+1 < size:
           bools = [x[0],x[1]+1] in empty_list		
           if grid[x[0]][x[1]+1] == 0 and bools == False and grid[x[0]][x[1]+1] != 4 and\
           [x[0],x[1]+1] not in show: 			
             empty_list.append([x[0],x[1]+1])
       #check the left cell
       if x[1]-1 > 1:
           bools = [x[0],x[1]-1] in empty_list	
           if grid[x[0]][x[1]-1] == 0 and bools == False and grid[x[0]][x[1]-1] != 4 and\
            [x[0],x[1]-1] not in show:		
               empty_list.append([x[0],x[1]-1])
       #check bottom cell
       if x[0]+1 < size:
          bools = [x[0]+1,x[1]] in empty_list 
          if grid[x[0]+1][x[1]] == 0 and bools == False and grid[x[0]][x[1]-1] != 4 and\
          [x[0]+1,x[1]] not in show:  
              empty_list.append([x[0]+1,x[1]])
       #check bottom cell
       if x[0]-1 > 1:
           bools = [x[0]-1,x[1]] in empty_list 
           if grid[x[0]-1][x[1]] == 0 and bools == False and grid[x[0]-1][x[1]] != 4 and\
           [x[0]-1,x[1]] not in show: 
              empty_list.append([x[0]-1,x[1]])	
      #check if list as been apdated
      
      #do recurssion
    return empty_list	
   			
          	 					    	 	
def open_empty(arr):
   global show
   if grid[arr[0]][arr[1]] == 0:
        return recurse([arr])
   else:
        show.append(arr)	   	   	
   return []

def win_game(shows):
    global booms_len
    global size
    size1 = size*size
    game_size = size1-booms_len
    if shows >= game_size :
        return True
    return False    
    
def draw_grid(show):
    global stop
    print("   ",end="")
    for x in range(1,size+1):
        print(x," ",end="")
    counter = 1 
    print("")
    for v,y in enumerate(grid):
        print("")
        print(counter," ",end="")
        for c,a in enumerate(y):
            #print(v," ",c)
            if [v,c] in show :
                if a == 4:
                    print("*"," ",end="")
                else:    
                    print(a," ",end="")
               # check(int(a))
            else:
                print("-"," ",end="")                           
        counter = counter +1
    print("") 


def print_grid():
    print("")
    print("========================")
    print("   ",end="")
    for x in range(1,9):
        print(x," ",end="")
    counter = 1 
    for v,y in enumerate(grid):
        print("")
        print(counter," ",end="")
        for c,a in enumerate(y):
            if a == 4:
                print("*"," ",end="")
            else:    
                print(a," ",end="")                         
        counter = counter +1
    print("") 
    
def check(value):
    global stop

    if grid[value[0]][value[1]] == 4:
        stop = True
    """
    if value == 4:
        stop = True
    """     

def ask():
    global stop
    global show
    global complete_grid
    global grid
    grid = create_grid(size)        
    draw_grid(show)
    while True:
        value = input("Enter X and Y like x,y ")
        values = value.split(",")
        try:
            try: 		
                x = int(values[0])-1
                y = int(values[1])-1
            except IndexError:
                print("Enter the correct format")
                continue
        except ValueError:
            print("You entered invalid input")
            continue
        if x > -1 and x  < size and y > -1 and y < size:
            #print(show) 
            if [x,y] not in show:
            	#show.append([x,y])
            	lists = open_empty([x,y]) 
            	show = show+lists
            	lists = []
            	draw_grid(show)
            	check([x,y])
            	if win_game(len(show)):
                	print("You have completed the game congradulations")
                	print_grid() 
                	print(show)
                	break
            else:
                print("The cell is already open") 
        else:
            print("your number should be between 0 and 8")
        if stop:
           print("********************** Game Over ****************************")
           print_grid() 
           print("")
           print("****************You were boomed Game over********************")
           break

def welcome():
    print("==============================        =========================================")
    print("============================ MINESWEAPER ======================================")
    print("=============================         =========================================")
    print("")
welcome()     
#open_empty() 


ask()
