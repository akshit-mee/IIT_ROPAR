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
    print(dest_bed)
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
    while bed_count!=len(dest_bed):
        
        Next_Wing=dest_bed[bed_count][0]
        Next_Room=dest_bed[bed_count][1]
        Next_Bed=dest_bed[bed_count][2]

        if Next_Wing != Curr_Wing:
            node='Start'
            print(node)
            node='Wing_{0}'.format(Next_Wing)
            print(node)
        elif Next_Room != Curr_Room:
            node='Wing_{0},Room_{1}'.format(Next_Wing, Next_Room)
            print(node)
        else:
            bed_count=bed_count+1            
            node1='Wing_{0},Room_{1}'.format(Next_Wing, Next_Room)
            if node1!=node:
                print(node1)               
            node='Wing_{0},Room_{1},Bed_{2}'.format(Next_Wing, Next_Room, Next_Bed)
            print(node)
            node=node1
        Curr_Wing=Next_Wing
        Curr_Room=Next_Room
        Curr_Bed=Next_Bed
    print("Start")
    print("All requested bed are served")
path()
	
    
