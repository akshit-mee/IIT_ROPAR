const int MAX_Nodes=150;
int path[MAX_Nodes][3];
const int MAX_Beds=12;
int dest_bed[MAX_Beds][3]={{1, 2 ,1},
{2, 1, 1},
{2, 2, 2},
{2, 6, 1},
{2, 6, 3},
{3, 5, 1},
{4, 1, 3},
{4, 2, 4}};

void setup()
{
  
}

void loop()
{
  for (int i; i<1; i++)
  {
    path_planning();
  }
  for (int i; i<MAX_Nodes; i++)
  {
    for (int j; j<3; j++)
    {
      Serial.print(path[i][j]);
    }
  }
}
void path_planning()
{
    int q=1;
    int Curr_Wing=0;
    int Curr_Room=0;
    int Curr_Bed=0;
    int bed_count=0;
    int Curr_Node[]={0,0,0};
    
    while (bed_count!=MAX_Beds)
    {
        int Wing_Order;
        int Room_Order;
        int Bed_Order;
        int Next_Wing=dest_bed[bed_count][0];
        int Next_Room=dest_bed[bed_count][1];
        int Next_Bed=dest_bed[bed_count][2];
        
        if (Next_Wing != Curr_Wing)
        {
            
            if (Curr_Node[0]>Next_Wing)
            {
                Wing_Order=-1;
            }
            else
            {
                Wing_Order=1;
            }
            
            for (int i=Curr_Node[0]-Wing_Order; i!=Next_Wing; i=i+Wing_Order)
            {
                Curr_Node[0]=i+Wing_Order;
                for (int j=Curr_Node[1]+1; j>=0; j--)
                {
                    Curr_Node[1]=j+Room_Order;
                    for (int k=Curr_Node[2]+1; k>=0; k--)
                    {
                        Curr_Node[2]=k+Bed_Order;
                        if (path[q-1][0]!=Curr_Node[0] && path[q-1][1]!=Curr_Node[1] && path[q-1][2]!=Curr_Node[2])
                        {
                          for(int i=0;j<3;j++)
                          {
                          path[q][i]=Curr_Node[i];
                          }
                          q++;
                        }
                    }
                }                    
            Curr_Wing=Next_Wing;
            }
        }


        else if (Next_Room != Curr_Room)
        {
            
            if (Curr_Node[1]>Next_Room)
            {
                Room_Order=-1;
            }
            else
            {
                Room_Order=1;
            }
            for (int j=Curr_Node[1]-Room_Order; j!=Next_Room; j=j+Room_Order)
            {
                Curr_Node[1]=j+Room_Order;
                for (int k = Curr_Node[2]+1; k>=0; k--)
                {
                    Curr_Node[2]=k+Bed_Order;
                    if (path[q-1][0]!=Curr_Node[0] && path[q-1][1]!=Curr_Node[1] && path[q-1][2]!=Curr_Node[2])
                        {
                          for(int i=0;j<3;j++)
                          {
                          path[q][i]=Curr_Node[i];
                          }
                          q++;
                        }
                }
              Curr_Room=Next_Room;
            }
        }

            
        else
        {
            bed_count=bed_count+1;
            if (Curr_Node[2]>Next_Bed)
            {
                Bed_Order=-1;
            }
            else
            {
                Bed_Order=1;
            }
            for (int k=Curr_Node[2]-Bed_Order;k!= Next_Bed;k=k+Bed_Order)
            {
                Curr_Node[2]=k+Bed_Order;
                if (path[q-1][0]!=Curr_Node[0] && path[q-1][1]!=Curr_Node[1] && path[q-1][2]!=Curr_Node[2])
                        {
                          for(int i=0;i<3;i++)
                          {
                          path[q][i]=Curr_Node[i];
                          }
                          q++;
                        }
            }
            path[q][0]=999;
            path[q][1]=999;
            path[q][2]=999;
            q++;
            Curr_Node[0]=Next_Wing;
            Curr_Node[1]=Next_Room;
            Curr_Node[2]=Next_Bed;
            Curr_Bed=Next_Bed;
        }

/// Return to start ////                        

    for (int i=Curr_Node[0]+1; i>=0; i--)
    {
        Curr_Node[0]=i-1;
        for (int j=Curr_Node[1]+1;j>= 0; j--)
        {
            Curr_Node[1]=j-1;
            for (int k=Curr_Node[2]+1;k>=0; k--)
            {
                Curr_Node[2]=k-1;
                if (path[q-1][0]!=Curr_Node[0] && path[q-1][1]!=Curr_Node[1] && path[q-1][2]!=Curr_Node[2])
                        {
                          for(int i=0;j<3;j++)
                          {
                          path[q][i]=Curr_Node[i];
                          }
                          q++;
                        }
            }
        }
    }
    } 
}
