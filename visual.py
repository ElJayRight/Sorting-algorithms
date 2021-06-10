import pygame,time,random
def bubbleSort(arr,self):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
        pygame.draw.rect(self.screen,(255,255,255),(0,30,600,500))
        for a,b in enumerate(self.arr):
            pygame.draw.rect(self.screen,(0,255,0),(300+a*30,500-b*5,30,b*5))
            pygame.draw.rect(self.screen,(0,0,0),(300+a*30,500-b*5,30,b*5),1)

            text_obj = self.font.render(str(b),False,(0,0,0))
            self.screen.blit(text_obj,(300+(a*30)+text_obj.get_width()/2,500-text_obj.get_height()-5))

        pygame.display.update()
        time.sleep(1)
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertionSort(arr,self):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        pygame.draw.rect(self.screen,(255,255,255),(0,30,600,500))
        for a,b in enumerate(self.arr):
            pygame.draw.rect(self.screen,(0,255,0),(300+a*30,500-b*5,30,b*5))
            pygame.draw.rect(self.screen,(0,0,0),(300+a*30,500-b*5,30,b*5),1)

            text_obj = self.font.render(str(b),False,(0,0,0))
            self.screen.blit(text_obj,(300+(a*30)+text_obj.get_width()/2,500-text_obj.get_height()-5))
        pygame.display.update()
        time.sleep(1)
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

def selection(A,self):
    for i in range(len(A)):
        pygame.draw.rect(self.screen,(255,255,255),(0,30,600,500))
        for a,b in enumerate(self.arr):
            pygame.draw.rect(self.screen,(0,255,0),(300+a*30,500-b*5,30,b*5))
            pygame.draw.rect(self.screen,(0,0,0),(300+a*30,500-b*5,30,b*5),1)

            text_obj = self.font.render(str(b),False,(0,0,0))
            self.screen.blit(text_obj,(300+(a*30)+text_obj.get_width()/2,500-text_obj.get_height()-5))
        pygame.display.update()
        time.sleep(1)
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
                
        # Swap the found minimum element with
        # the first element       
        A[i], A[min_idx] = A[min_idx], A[i]

class Window:
    def __init__(self,x,y):
        self.width = x
        self.height = y
        self.arr = [64, 34, 25, 12, 22, 11, 90, 38, 86, 56]
        #creates pygame instance
        pygame.init()

        #fonts
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS',12)
        self.screen = pygame.display.set_mode((x,y))
        self.screen.fill((255,255,255))
        self.active = 1

        #start button
        pygame.draw.rect(self.screen,(0,0,0),(670,540,80,40),1)
        text_obj = self.font.render("Start",False,(0,0,0))
        self.screen.blit(text_obj,(710-text_obj.get_width()//2,560-text_obj.get_height()//2))

        #randomise button
        pygame.draw.rect(self.screen,(0,0,0),(590,540,80,40),1)
        text_obj = self.font.render("Randomise",False,(0,0,0))
        self.screen.blit(text_obj,(630-text_obj.get_width()//2,560-text_obj.get_height()//2))

        self.top_menu()
        self.graph()
        pygame.display.update()
    def top_menu(self):
        pygame.draw.rect(self.screen,(0,0,0),(0,0,800,30))
        text_obj = self.font.render("Sorting methdos:",False,(255,255,255))
        self.screen.blit(text_obj,(5,0+text_obj.get_height()//2))

        for j,i in enumerate(["Bubble sort","Insertion","Selection"]):
            text_obj = self.font.render(i,False,(255,255,255))
            #pygame.draw.rect(self.screen,(0,0,255),(95*(j+1)+40-10,0,60+20,30),2)
            self.screen.blit(text_obj,(95*(j+1)+40,0+text_obj.get_height()//2))

    def graph(self):
        pygame.draw.rect(self.screen,(255,255,255),(0,30,600,500))
        for a,b in enumerate(self.arr):
            pygame.draw.rect(self.screen,(0,255,0),(300+a*30,500-b*5,30,b*5))
            pygame.draw.rect(self.screen,(0,0,0),(300+a*30,500-b*5,30,b*5),1)

            text_obj = self.font.render(str(b),False,(0,0,0))
            self.screen.blit(text_obj,(300+(a*30)+text_obj.get_width()/2,500-text_obj.get_height()-5))
        pygame.display.update()
    def input(self,action):
        x,y = action
        if y<30:
            x-=40
            x//=95
            if x>3 or x<1:
                return
            self.top_menu()
            pygame.draw.rect(self.screen,(255,255,255),(x*95+30,0,100,30))
            pygame.draw.rect(self.screen,(0,0,0),(x*95+30,0,100,30),1)
            self.active = x-1
            text_obj = self.font.render(["Bubble sort","Insertion","Selection"][x-1],False,(0,0,0))
            self.screen.blit(text_obj,(95*(x)+40,0+text_obj.get_height()//2))
            pygame.display.update()
        elif x in range(670,750) and y in range(540,580):
            values = [bubbleSort,insertionSort,selection]
            values[self.active](self.arr,self)
        elif x in range(590,670) and y in range(540,580):
            for i in range(len(self.arr)):
                self.arr[i] = random.randint(20,90)
            self.graph()
        return
    def render(self,object=None):
        pygame.display.update()
def main():
    win = Window(800,600)
    while True:
        for event in pygame.event.get():
            #if the player wants to quit the game.
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            #left click
            if event.type ==pygame.MOUSEBUTTONDOWN and event.button==1:
                win.input(event.pos)
main()