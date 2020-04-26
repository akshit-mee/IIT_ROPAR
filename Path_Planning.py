dest_bed=list()
bed_id={}


class Bed:
    def __init__(self, Wing, Room, Bed):
        self.node=[Wing, Room, Bed]


## For hospitals bed name would be manually maped
## Loop is only for demostration purposes
i=1
for w in range(1,5):
    for r in range (1,7):
        for b in range (1,5):
            Bed1=Bed(w,r,b)
            bed_id['BED_{0}'.format(i,w,r,b)]=Bed1.node
            i=i+1

#print(bed_id)



def input_beds():
    i=0
    number = input("Enter the number of bed you want:")
    for i in range(int(number)):
        n = input("Enter Bed Number:")
        dest_bed.append(bed_id[n])
    print()
    print('Location of Input Bed:',dest_bed)
    dest_bed.sort()
input_beds()

print(dest_bed)

def path():
    print('\n'*5)
    print("Listing Node in the respective order")
    Curr_Wing=0
    Curr_Room=0
    Curr_Bed=0
    Curr_Node=0
    bed_count=0
    Curr_Node=[0,0,0]
    Prev_Node=Curr_Node
    while bed_count!=len(dest_bed):
        
        Next_Wing=dest_bed[bed_count][0]
        Next_Room=dest_bed[bed_count][1]
        Next_Bed=dest_bed[bed_count][2]
        print(Curr_Node)
        
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
            Curr_Wing=Next_Wing
##            node='Wing_{0}'.format(Next_Wing)
##            print(node)



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
            Curr_Room=Next_Room        
##            node='Wing_{0},Room_{1}'.format(Next_Wing, Next_Room)
##            print(node)


            
        else:
            bed_count=bed_count+1
            if Curr_Node[2]>Next_Bed:
                Bed_Order=-1
            else:
                Bed_Order=1
            for k in range(Curr_Node[2]-Bed_Order, Next_Bed, Bed_Order):
                Curr_Node[2]=k+Bed_Order
                print(Curr_Node)             
            Curr_Node=[Next_Wing, Next_Room, Next_Bed]
            Curr_Bed=Next_Bed
            node='Wing_{0},Room_{1},Bed_{2}'.format(Next_Wing, Next_Room, Next_Bed)
            print(node)

        
            
        
        
        

##Return to Start
    if Curr_Node[0]>0:
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
    for i in range(Curr_Node[0]-Wing_Order, 0, Wing_Order):
        Curr_Node[0]=i+Wing_Order
        for j in range(Curr_Node[1]-Room_Order, 0, Room_Order):
            Curr_Node[1]=j+Room_Order
            for k in range(Curr_Node[2]-Room_Order, 0, Bed_Order):
                Curr_Node[2]=k+Bed_Order
                print(Curr_Node)

    print("Start")
    print("All requested bed are served")
##End
path()
	
    
