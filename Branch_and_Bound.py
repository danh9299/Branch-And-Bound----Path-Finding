#Tạo các cạnh kề và k(u,v)
graph = {                                   
        'A': {'C': 9,'D':7, 'E':13, 'F':20},
        'C': {'H':10},
        'D': {'E':4,'H':8},
        'E': {'K':4,'I':3},
        'K': {'B': 6},
        'H': {'K':5},
        'I': {'K':9,'B':5},
        'F': {'I':6,'G':4},
        'B' : {},
        'G' : {}
        }
#Tạo hàm đánh giá heuristic
heuristic = {                       
        'A': 14,
        'B': 0,
        'C': 15,
        'D': 6,
        'E': 8,
        'F': 7,
        'G': 12,
        'H': 10,
        'K': 2,
        'I': 4,
            }
def bbs(graph_to_seach, start, end,):
    #Thiết lập một giá trị min cực cao khởi tạo
    min=10**100
    #Tạo list way để lưu đường đi
    way=[]
    #Tạo ra 1 list open lưu trữ đường đi, hàm g và hàm f
    open = []
    #Phần tử thứ 0 là đường đi, phần tử thứ 1 là g(), phần tử thứ 2 là f()
    open_check=[[start],0,0]       
    #Đưa điểm đâu tiên vào trong ngăn xếp
    open.append(open_check)
    while True:
        #Nếu ngăn xếp mà rỗng, kết thúc thuật toán, đưa ra đường đi
        if len(open)==0:
            if way == []:
                way.append("Không thấy đường đi")
                return way
            else:
                print("Đường đi: ",end="")
                return way
        open_check = []
        #Lấy list đầu trong open
        path = open.pop(0) 
        #Lấy vị trí cuối cùng trong đường đi
        node = path[0][-1]
        print("Duyệt: ",node)
        #Tìm thấy nút cần tìm
        if node == end:
            #Nếu đường đi nhỏ hơn min
            if(path[2]<min):
                min=path[2]
                way=path[0]
                print("Giá trị cực tiểu cập nhật: ",min)
                continue
            else:
                continue
        #Nếu đường đi lớn hơn min
        elif(path[2]>min):
            print("Phát hiện đường đi có giá trị: ", path[2])
            print("Cắt bỏ nhánh do đường đi có giá trị lớn hơn min")
            continue
        while True:
            #Xác định đường đi từ nút đang xét tới các nút con
            for adjacent in graph_to_seach.get(node,{}):
                    new_path = list(path[0])
                    #Tính g(v)
                    check_way = path[1]+ graph_to_seach[node][adjacent]
                    #tính f(v)
                    check_f = check_way + heuristic[adjacent]
                    #Đẩy nút v mới vào new path
                    new_path.append(adjacent)
                    #Tạo 1 list lưu v, g(v), và f(v)
                    save_path = []
                    save_path.append(new_path)
                    save_path.append(check_way)
                    save_path.append(check_f)
                    #Lưu list này vào open_check
                    open_check.append(save_path)
            #Sắp xếp giảm dần để khi đưa vào open thành tăng dần
            for i in range(0,len(open_check)-1):
                for j in range (i+1,len(open_check)):                          
                    if(open_check[i][2]<open_check[j][2]):
                        tmp=open_check[i]
                        open_check[i]=open_check[j]
                        open_check[j]=tmp
                    elif(open_check[i][2]==open_check[j][2]):
                        if(open_check[i][1]>open_check[j][1]):
                            tmp=open_check[i]
                            open_check[i]=open_check[j]
                            open_check[j]=tmp
            #Đưa vào đầu stack
            for i in open_check:
                open.insert(0,i)
            break

#Phần main của bài
#Người dùng nhập vào dữ liệu cho điểm bắt đầu và điểm kết thúc
start = (input("Nhập điểm bắt đầu: "))
start = start.upper()
while start not in graph:
    print("Điểm bắt đầu phải có trong cây!")
    start = input("Nhập lại điểm bắt đầu: ")
    start = start.upper()
end = input("Nhập điểm cần đến: ")
end = end.upper()
while end not in graph:
    print("Điểm đến phải có trong cây!")
    end = input("Nhập lại điểm cần đến: ")
    end = end.upper()
for x in bbs(graph,start,end):
    if x == start:
        print(x,end="")
    elif x == "Không thấy đường đi":
        print(x)
    else:
        print("->",x,end="")
            
