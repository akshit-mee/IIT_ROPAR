dest_bed=list()
bed_id={}
calc_path=[[0,0,0]]

####################################################################

class Bed:
    def __init__(self, Wing, Room, Bed):
        self.node=[Wing, Room, Bed]

####################################################################

## For hospitals bed name would be manually maped
## Loop is only for demostration purposes
i=1
for w in range(1,5):
    for r in range (1,7):
        for b in range (1,5):
            Bed1=Bed(w,r,b)
            bed_id['BED_{0}'.format(i,w,r,b)]=Bed1.node
            i=i+1

###############################################################################

def input_beds():
    i=0
    number = input("Enter the number of bed you want:")
    for i in range(int(number)):
        n = input("Enter Bed Number:")
        dest_bed.append(bed_id[n])
    print()
    print('Location of Input Bed:',dest_bed)
    dest_bed.sort()

#################################################################################

def path():
    print('\n'*5)
    print("Listing Node in the respective order")
    Curr_Wing=0
    Curr_Room=0
    Curr_Bed=0
    Curr_Node=0
    bed_count=0
    Curr_Node=[0,0,0]
    
    while bed_count!=len(dest_bed):
        
        Next_Wing=dest_bed[bed_count][0]
        Next_Room=dest_bed[bed_count][1]
        Next_Bed=dest_bed[bed_count][2]
        
        if Next_Wing != Curr_Wing:
            if Curr_Node[0]>Next_Wing:
                Wing_Order=-1
            else:
                Wing_Order=1
            if Curr_Node[1]>0:
                Room_Order=-1
            else:
                Room_Order=1
            if Curr_Node[2]>0:
                Bed_Order=-1
            else:
                Bed_Order=1
            for i in range(Curr_Node[0]-Wing_Order, Next_Wing, Wing_Order):
                Curr_Node[0]=i+Wing_Order
                for j in range(Curr_Node[1]-Room_Order, 0, Room_Order):
                    Curr_Node[1]=j+Room_Order
                    for k in range(Curr_Node[2]-Room_Order, 0, Bed_Order):
                        Curr_Node[2]=k+Bed_Order
                        print(Curr_Node)
                        calc_path.append(Curr_Node[:])
            Curr_Wing=Next_Wing

        ##__________________________________________________________________##

        elif Next_Room != Curr_Room:
            if Curr_Node[1]>Next_Room:
                Room_Order=-1
            else:
                Room_Order=1
            if Curr_Node[2]>0:
                Bed_Order=-1
            else:
                Bed_Order=1
            for j in range(Curr_Node[1]-Room_Order, Next_Room, Room_Order):
                Curr_Node[1]=j+Room_Order
                for k in range(Curr_Node[2]-Bed_Order, 0, Bed_Order):
                    Curr_Node[2]=k+Bed_Order
                    print(Curr_Node)
                    calc_path.append(Curr_Node[:])
            Curr_Room=Next_Room

        ##_______________________________________________________________________________##
            
        else:
            bed_count=bed_count+1
            if Curr_Node[2]>Next_Bed:
                Bed_Order=-1
            else:
                Bed_Order=1
            for k in range(Curr_Node[2]-Bed_Order, Next_Bed, Bed_Order):
                Curr_Node[2]=k+Bed_Order
                print(Curr_Node)
                calc_path.append(Curr_Node[:])
            calc_path.append(['Pause'])
            Curr_Node=[Next_Wing, Next_Room, Next_Bed]
            Curr_Bed=Next_Bed
            
            node='Wing_{0},Room_{1},Bed_{2} Reached!'.format(Next_Wing, Next_Room, Next_Bed)
            print(node)
        ##_____________________________________________________________________________##            

##Return to Start
    Wing_Order=-1
    Room_Order=-1
    Bed_Order=-1
    for i in range(Curr_Node[0]-Wing_Order, 0, Wing_Order):
        Curr_Node[0]=i+Wing_Order
        for j in range(Curr_Node[1]-Room_Order, 0, Room_Order):
            Curr_Node[1]=j+Room_Order
            for k in range(Curr_Node[2]-Room_Order, 0, Bed_Order):
                Curr_Node[2]=k+Bed_Order
                calc_path.append(Curr_Node[:])
                print(Curr_Node)
    print("All requested bed are served")
    
################################################################################


input_beds()
print(dest_bed)

path()
for i in range(len(calc_path)-2):
    if calc_path[i]==calc_path[i+1]:
        calc_path.pop(i)

    
