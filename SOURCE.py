import sys
import time


# Dùng để lưu những chữ cái ở đầu mỗi hạng tử
list_dif_zero ={}

# Biến map dùng để map chữ cái với một số nguyên đại diện
mp = {}

# Biến map dùng để map số nguyên đại diện về ngược lại chữ cái
mp_nguoc ={}

# Lưu kết quả cuối cùng
ketqua=[]

# Biến đo bộ nhớ
size = 0 


# Đặt giới hạn đệ quy mới về 1000000000 để phục vụ cho các test to
sys.setrecursionlimit(1000000000)

def khu_dau_tru(a):

    ### All minus in bracket
    b = a
    
    #Đo lường size
    global size
    size += sys.getsizeof(b)

    i = 0
    check_term = False
    while(i<len(b)):
        if(b[i]>='A' and b[i]<='Z'):
            if(check_term==False):
                if(i!=0):
                    if(b[i-1]!='-' and b[i-1]!='+'):
                        b = b[0:i] + '+' + b[i:]
                        i+=1
                else: 
                    b='+' + b
                    i+=1
                check_term=True
        else:
            check_term=False
        i+=1
    n = len(b)
    c = []
    for i in range(n):
        c.append(b[i])
    
    ### Day dau tru vao
    ok = [0 for _ in range(n)]
    for i in range(n):
        if(i==0): continue
        if(c[i]=='(' and c[i-1]=='-'):
            # just solve when ever the level is zero = 0
            ok[i-1]=1
            level_bracket = 1
            term = False
            j=i+1
            while(j<n):
                
                if(level_bracket==1):
                    if(c[j]=='*'):
                        j+=2
                        continue
                    if(c[j]=='-' or c[j]=='+'):
                        term=False

                    if(term==False):
                        if(c[j]=='+'): 
                            c[j]='-'
                            term=True
                            j+=1
                            continue
                        if(c[j]=='-'): 
                            c[j]='+'
                            term=True
                            j+=1
                            continue

                if(c[j]=='('): level_bracket+=1
                if(c[j]==')'): level_bracket-=1

                if(level_bracket==0 and c[j]==')'): break
                j+=1
        #Đo lường size
    size += sys.getsizeof(c)

    b=''
    for i in range(n):
        if(ok[i]==0):
            b=b+c[i]
        else: b=b+'+'


        ###Xoa ngoac
    b= '_'+b+'_'
    n=len(b)
    dq= []
    l = 0
    r = 0
    bac = 0
    ok = [0 for _ in range(n)] 
    ok[0]=ok[n-1]=1
    for i in range(n):
        level_bracket = 1
        if(b[i]=='('):
            if(b[i-1]!='*'):
                for j in range(i+1,n):
                    if(b[j]=='('):
                        level_bracket +=1
                        continue
                    if(b[j]==')'):
                        level_bracket -=1
                        if(level_bracket==0):
                            if(b[j+1]!="*"):
                                if(b[i-1]=='+'):
                                    ok[i-1]=1
                                ok[i]=ok[j]=1
                            break
                        continue

    #Đo lường size
    size += sys.getsizeof(b) + sys.getsizeof(ok)
    a = ""
    for i in range(n):
        if(ok[i]==0):
            a=a+b[i]

                
        ### Xoa dau cong
    b = a
    i = 0
    while(i<len(b)):
        if(b[i]=='+'):
            if(i==0): 
                b=b[1:]
                i-=1
            else:
                if(b[i-1]=='(' or b[i-1]=='*'):
                    b = b[:i]+b[i+1:]
                    i-=1
        i+=1
    #Đo lường size
    size += sys.getsizeof(b)
    return b


def nhan2so(s,t):
    
    a = []
    b = []

    #Kiểm tra dâu nhân => Dạng nhân tử hỗn hợp A00*B00 cho cả 2 biến s,t
    daunhan_s=False
    daunhan_t=False
    check_s=False
    dem_s=0
    for u in s:
        a.append(u)
        if(u=='*'):
            daunhan_s=True
        if(u!='0'):
            dem_s+=1
    if(dem_s==len(s)):
        check_s=True
    if(daunhan_s==True):
        check_s=False


    check_t=False
    dem_t=0
    for u in t:
        b.append(u)
        if(u=='*'):
            daunhan_t=True
        if(u!='0'):
            dem_t+=1
    if(dem_t==len(t)):
        check_t=True
    if(daunhan_t==True):
        check_t=False

    n = len(a)
    m = len(b)

    tmp = max(n,m)
    khong = []
    khong.append("")
    for i in range(tmp+1):
        u = khong[i] + '0'
        khong.append(u)
     
    tich = ""
    # Ca 2 so deu la mot dang binh thuong thì đơn giản
    if(check_s==True and check_t==True):
        for i in range(m):
            for j in range(n):
                nhantu1 = a[j] 
                nhantu2 = b[i] + khong[m-1-i] + khong[n-1-j]
                tich = tich + '+' + nhantu1 +"*"+ nhantu2

    # Cả 2 số đều là dạng hỗn hợp 
    if(check_s == False and check_t ==False):
        tich = "_"+ s +'*'+t

    # t là số bình thường còn s là số hỗn hợp
    if(check_s == False and check_t == True):
        for i in range(m):
            nhantu = b[i] + khong[m-1-i]
            tich = tich + '+' + s + "*" +nhantu
    
    # s là số bình thường còn t là số hỗn hợp
    if(check_s == True and check_t == False):
        for i in range(n):
            nhantu = a[i] + khong[n-1-i]
            tich = tich + '+' + t + "*" +nhantu

    return '('+tich[1:]+')'



def nhan2bieuthuc(s,t):
    a=[]
    b=[]
    #Đo lường size
    global size
    size += sys.getsizeof(s) + sys.getsizeof(t) 
    if(s[0]!='-' and s[0]!='+'):
        s='+'+s

    if(t[0]!='-' and t[0]!='+'):
        t='+'+t

    ans=""

    # Tách hạng tử của 2 biểu thức
    a = tachhangtu(s)
    b = tachhangtu(t)

    # Lặp để nhân phân phối 2 biểu thức
    n= len (a)
    m=len(b)
    for i in range(m):
        dau1=b[i][0]
        hangtu1=b[i][1]
        for j in range(n):
            dau2=a[j][0]
            hangtu2=a[j][1]

            dau="+"
            if(dau1!=dau2):
                dau='-'
            nhan= nhan2so(hangtu1,hangtu2)
            ans = ans + dau + nhan

    return ans 

# nhan2bieuthuc("ABC+D*E*F","GH+AE")
# print("nhan 2 so:")

# print(nhan2so("D*E*F","GH"))


def nhan2dathuc(a,b):
    check_a = True
    for u in a:
        if(u == '(' or u == ')'):
            check_a = False
            break

    check_b = True
    for u in b:
        if(u == '(' or u == ')'):
            check_b = False
            break
    
    #Trường hợp suy biến là 2 đa thức là 2 biểu thức không có dấu ngoặc
    if(check_a ==True and check_b==True):
        return nhan2bieuthuc(a,b)
    else:
        # Nếu không thì phải tìm dạng không có dấu ngoặc của 2 đa thức
        new_a = dangdonthuc(a)
        new_b = dangdonthuc(b)
        return nhan2bieuthuc(new_a,new_b)

def dangdonthuc(a):

    check = True
    a = str(a)
    for u in a:
        if(u=='(' or u==')'):
            check = False
            break
    # case Suy bien
    if(check == True):
        return a
    # Khong suy bien
    kq = ""
    n = len(a)
    first = True
    check = True


    while(check):
        # Lặp lại cho đến khi không còn dấu ngoặc vì một lần hoàn thành
        # xong một dấu ngoặc thì sẽ tạo ra thêm 1 biểu thức ngoặc mới.
        cnt = 0
        for u in a:
            if(u=='(' or u==')'):
                cnt+=1
                break
        if(cnt==0):
            check=False
            break        

        kq = ""
        n = len(a)
        i = 0

        while(i<n):
            if(a[i]!='('):
                kq = kq + a[i]
            else:

                level_bracket=1
                nhantu1=""
                nhantu2=""
                dau1=1
                dau2=1
                end = i

                if(i!=0 and a[i-1]!='+'and a[i-1]!='-'):
                    dau1=1
                    kq= a[:i]
                else:
                    if(i-1!=-1):
                        kq= a[:i-1]
                    if(i!=0 and a[i-1]=='-'):
                        dau1=-1

                # Xet ngoac dau tien
                for j in range(i+1,n):
                    if(a[j]=='('):
                        level_bracket+=1
                    elif(a[j]==')'):
                        level_bracket-=1
                        if(level_bracket==0):
                            end=j
                            break
                    nhantu1 = nhantu1+a[j]
                
                # Truoc ngoac la don thuc
                if((i!=0 and a[i-1]=='*') or ( i>=2 and a[i-2]=='*')):
                    if(i>=1 and a[i-1]=='*'):
                        pos = i-2
                    if(i>=2 and a[i-2]=='*'):
                        pos = i-3
                    while(pos!=-1):
                        if((a[pos]>='A' and a[pos]<='Z') or (a[pos]=='0')):
                            nhantu2 =  a[pos] + nhantu2
                        else:
                            if(a[pos]=='-'):
                                dau1=-1
                                kq=a[:pos]
                            if(a[pos]=='+'):
                                kq=a[:pos]
                            if(a[pos]=='*'):
                                kq=a[:pos+1]
                            break
                        pos-=1
                        if(pos==-1): kq=""
                # Nhân tứ thứ 2 ở phía sau dấu ngoặc
                elif(end+1<n and a[end+1]=='*'):
                    start= end+2
                    if(a[start]=='+'):
                        dau2=1
                        start+=1
                    else:
                        if(a[start]=='-'):
                            dau2=-1
                            start+=1
                    if((a[start]>='A' and a[start]<='Z') or (a[start]=='0')):
                        while(start!=n):
                            if((a[start]>='A' and a[start]<='Z') or (a[start]=='0')):
                                nhantu2 = nhantu2 + a[start]
                            else:
                                
                                break
                            start+=1
                            i = start - 1
                    elif(a[start]=='('):
                        level_bracket=1
                        for j in range(start+1,n):
                            if(a[j]=='('):
                                level_bracket+=1
                            elif(a[j]==')'):
                                level_bracket-=1
                                if(level_bracket==0):
                                    i = j
                                    break
                            nhantu2 = nhantu2+a[j]
                            i=j
                kq_nhan2dathuc = nhan2dathuc(nhantu1,nhantu2)
                kq_nhan2dathuc = khu_dau_tru(kq_nhan2dathuc)

                if(kq_nhan2dathuc[0]!='-' and kq_nhan2dathuc[0]!='+'):
                    dau = '+'
                    if(dau1!=dau2): 
                        dau='-'
                        # Kẹp dấu ngoặc để khi gặp dấu trừ phá dấu có thể đổi dấu toàn bộ 
                        kq_nhan2dathuc = dau +'('+kq_nhan2dathuc+')'
                        kq_nhan2dathuc = khu_dau_tru(kq_nhan2dathuc)
                    else:
                        kq_nhan2dathuc = dau +kq_nhan2dathuc
                else:
                    dau = '+'
                    if(dau1!=dau2): 
                        if(dau=='-'): dau='+'
                        else: dau='-'
                    kq_nhan2dathuc = dau +'('+kq_nhan2dathuc+')'
                    kq_nhan2dathuc = khu_dau_tru(kq_nhan2dathuc)
                i= max(i,end)
                m=len(a)
                if(i+1<len(a)):
                    kq = kq +'+('+kq_nhan2dathuc+')'+a[i+1:]
                else:
                    kq = kq +'+('+kq_nhan2dathuc+')'
                a=kq
                a=khu_dau_tru(a)
                kq=khu_dau_tru(kq)
                break

            i+=1
        
    kq = ""
    if(a[0]=='_'): kq=a[1:len(a)-1]
    else: kq=kq+a[0:len(a)-1]

    if(a[len(a)-1]!='_'): kq= kq+a[len(a)-1]

    return kq

def nhanphanphoi2sohang(a):
    n = len(a)
    i = 0
    kq = ""
    pre = "_"
    first=True
    
    while(True):

        b= tachhangtu(a)
        check=True
        for u in b:
            hangtu=u[1]
            dem=0
            for v in hangtu:
                if(v>='A' and v<='Z'):
                    dem+=1
                    if(dem>1):
                        check=False
                        break
                if(v=='*'):
                    dem=0
            if(check==False):
                break
        if(check==True): break


        n = len(a)
        if(i>=n-1): break
        while(i<n):
            kq = kq + a[i]
            if(a[i]=='*' and a[i-1]!=')' and a[i+1]!='('):
                nhantu1=""
                nhantu2=""
                dau1=1
                dau2=1
                back=i-1
                while(back!=-1):
                    if((a[back]>='A' and a[back]<='Z') or (a[back]=='0')):
                        nhantu1 = a[back] + nhantu1
                    else:
                        if(a[back]=='-'):
                            dau1=-1
                            kq=kq[:back]
                        if(a[back]=='+'):
                            kq=kq[:back]
                        if(a[back]=='*'):
                            kq=kq[:back+1]
                        break
                    back-=1
                    if(back==-1): kq=""

                front=i+1
                if(a[front]=='+'):
                    dau2=1
                    front+=1
                else:
                    if(a[front]=='-'):
                        dau2=-1
                        front+=1
                while(front!=n):
                    if((a[front]>='A' and a[front]<='Z') or (a[front] == '0')):
                        nhantu2 = nhantu2 + a[front]
                    else:
                        i = front-1
                        break
                    front+=1
                    i=front-1
                if(dau1==dau2):
                    kq = kq + '+' + nhan2so(nhantu1,nhantu2)
                    
                else:
                    kq = kq + '-' + nhan2so(nhantu1,nhantu2) 
                tmp = i
                i = len(kq) 
                a= kq+ a[tmp+1:]
                break
            i+=1
    #Đo lường size
    global size
    size += sys.getsizeof(a)
    return a


def forward_checking(i,x,list,sum,ans,diff,order_constraint,c,value_nhan,heso_tmp):
    
    global mp
    global list_dif_zero 
    symbol='+'
    if(i<len(list)):
        symbol = list[i][0]

    
    if(symbol=='+'):

        if(i!=len(list)-1):
            letter = str(list[i][2][0][0])
        else: 
            
            letter = str(list[i][2])
        heso = list[i][1]
        if(letter=='0'):
            giatri=0
        else:
            order = mp[letter]
            giatri = ans[order]

        du=sum%10
        if(i==len(list)-1):
            #Cuối constraint
            #Kiểm tra xem chữ cái cuối này được gán hay chưa
            if(giatri==-1):
                # Nếu chữ cái kết quả chưa được gán thì sẽ gán
                #Để thỏa constraint này thì cần phải giá trị dư cần phải chưa bị chiếm
                
                if(diff[du]==0):
                    if(du==0):
                        if letter in list_dif_zero:
                            return False

                    # Nếu thỏa thì set up cho constraint kế tiếp
                    diff[du]=1
                    ans[order]=du
                    carry = sum//10
                    check = chonbien(c,order_constraint+1,carry,ans,diff)
                    if(check==True):
                        return True
                    ans[order]=-1
                    diff[du]=0
                else:
                    # Với cách gán hiện tại thì sẽ không thỏa mãn constraint này vì có giá trị cho chữ số cuối cùng
                    return False
            else:
                #Nếu đã được gán giá trị trước đó rồi thì kiểm tra kết quả với sum hiện tại
                if(du==giatri):
                    #Thoả điều kiện với cách gán này
                    carry=sum//10
                    return chonbien(c,order_constraint+1,carry,ans,diff)
                    #Vì giá trị đã được gán từ một vòng lặp trước đó nên ta không cần gán reverse lại
                else:
                    # Không thỏa điều kiện
                    return False

        else:
            if(giatri!=-1):
                # Vì biến này đã được gán từ trước nên ta không thể thay đổi giá trị của biến này được
                check=forward_checking(i+1,0,list,sum+giatri*heso,ans,diff,order_constraint,c,1,0)
                if(check == True):
                    return True
            else:
                start = 0
                if letter in list_dif_zero: 
                    start = 1
                for j in range(start,10):
                    if(diff[j]==0):
                        ans[order] = j
                        sum = sum + j*heso
                        diff[j]=1 # occupied
                        check = forward_checking(i+1,0,list,sum,ans,diff,order_constraint,c,1,0)
                        if(check == True):
                            return True
                        ans[order] = -1
                        sum = sum - j*heso
                        diff[j]=0 # unoccupied
        return False
    else:
        #Không cần xử lý trường hợp cuối constraint hiện tại vì ở cuối danh sách là 1 giá trị đơn (khác nhân)
        #Chọn xong giá trị cho các biến trong constraint nhân
        letter = list[i][2]
        heso = list[i][1]       

        if(x==len(letter)):
            check=forward_checking(i+1,0,list,sum+value_nhan*heso_tmp,ans,diff,order_constraint,c,1,0)
            if(check==True):
                return True
        else:
            chucai = letter[x][0]
            bac = letter[x][1]

            order = mp[chucai]

            giatri = ans[order]
            if(giatri!=-1):
                #Đã được gán trước đó
                check=forward_checking(i,x+1,list,sum,ans,diff,order_constraint,c,value_nhan*(giatri**bac),heso)
                if(check==True):
                    return True
            else:
                #Chưa được gán
                start = 0
                if chucai in list_dif_zero: 
                    start = 1 
                for j in range(start,10):
                    if(diff[j]==0):
                        ans[order]=j
                        diff[j]=1
                        check= forward_checking(i,x+1,list,sum,ans,diff,order_constraint,c,value_nhan*(j**bac),heso)
                        if(check == True):
                            return True
                        diff[j]=0# Unoccupied
                        ans[order]=-1
    return False


# Moi constraint se la mot hang chuc, don vi, tram
def chonbien(c,constraint,carry,ans,diff):
    global ketqua
    # Kiểm tra xem đã thỏa mãn hết constraint chưa?
    if(constraint==len(c)):

        # Kiểm tra xem carry cộng dồn bắt buộc phải = 0
        if(carry==0):
            ketqua=ans

            return True
        else:
            return False
    list= c[constraint]

    #recursive
    i=0
    sum_left=carry # Se mang carray cua truoc
    return forward_checking(i,0,list,sum_left,ans,diff,constraint,c,1,0)

def eli_minus(pheptinh):
    new_pheptinh = ""
    for u in pheptinh:
        if(u=='='):
            break
        new_pheptinh =new_pheptinh + u.upper()

    khu_tru = khu_dau_tru(new_pheptinh)

    return khu_tru
def nensolv4(pheptinh,kq):
    global list_dif_zero
    global size

    list_dif_zero[kq[0]]=1

    #Tách phép tính thành các tuple hạng tử 
    #đi kèm với dấu của hạng tử 
    a = tachhangtu(pheptinh)
    
    #Đo lường size
    size = sys.getsizeof(a)+sys.getsizeof(pheptinh)

    b = [[] for _ in range(100)]
    # Cấu trúc lưu sẽ là:
    # - Symbol - hệ số - chữ cái(bình thường)/bảng tần suât(phép nhân)
    n = len(a)
    # gom nhom
    b_max = 0
    for u in a:
        hangtu = u[1]
        heso = u[0]
        check_nhan = False
        for v in hangtu:
            if(v=='*'):
                check_nhan=True
                break
        symbol = '+'
        if(check_nhan):
            symbol='*'
            zero = 0
            new_hangtu = []
            for v in hangtu:
                if(v=='0'):
                    zero +=1
                if(v>='A' and v<='Z'):
                    new_hangtu.append(v)
            new_hangtu.sort()
            # Nhóm từng nhân tử trong hạng tử 
            dem = 1
            m = len(new_hangtu)
            tanso = []
            for j in range(1,m):
                if(new_hangtu[j] == new_hangtu[j-1]):
                    dem+=1
                else:
                    tanso.append([new_hangtu[j-1],dem])
                    dem=1
            tanso.append([new_hangtu[m-1],dem])
            b[zero].append([symbol,heso,tanso])

            # Tìm ra số lượng cột tối đa cần xem xét
            b_max = max(b_max,zero+1) 
        else:
            #Hạng tử này chỉ là hạng tử binh thường (không có dấu nhân)
            symbol='+'
            m=len(hangtu)
            for j in range(m):
                letter = hangtu[j]
                tmp= []
                tmp.append([letter,0])
                cot = m - j - 1
                b[cot].append([symbol,heso,tmp])
                # Tìm ra số lượng cột tối đa cần xem xét
                b_max = max(b_max,cot+1) 

    #Đo lường size
    size += sys.getsizeof(b)

    n = max(b_max,len(kq))
    c = [[] for _ in range(n)]
    
    for i in range(n):
        b[i].sort(key = lambda x: x[2])
        m = len(b[i])
        tong = 0
        if(len(b[i])!=0):
            tong = b[i][0][1]
        for j in range(m-1):
            if(b[i][j][2]==b[i][j+1][2]):
                tong+=b[i][j+1][1]
            else:
                if(tong != 0): 
                    c[i].append([b[i][j][0],tong,b[i][j][2]])
                tong = b[i][j+1][1]
       
        if(tong!=0): c[i].append([b[i][m-1][0],tong,b[i][m-1][2]])
        #Them ket qua
        n1 = len(kq)
        if(i<n1):
            c[i].append(['+',1,kq[n1-i-1]])
        else:
            c[i].append(['+',1,'0'])
    
    size += sys.getsizeof(c)

    return c


def solve(all_constraint, cnt):
    ans = [-1 for _ in range(11)]
    diff = [0 for _ in range(10)]
    f = open('output.txt', 'a')

    #Đo lường thời gian bắt đầu 1 test 
    start_time = time.time()
    global size
    global ketqua
    global mp
    global list_dif_zero
    global mp_nguoc
    if(chonbien(all_constraint,0,0,ans,diff) == True):
        ans = []
        for i in range(len(ketqua)):
            if(ketqua[i]==-1):
                continue
            else:
                letter = mp_nguoc[i]
                ans.append((letter,ketqua[i]))

        
        #Đo lường thời gian kết thúc 1 test 
        end_time = time.time()
        ans.sort()
        #print("Ouput:",end=" ")
        for u in ans:
            f.write(str(u[1]))
        f.write("\n")
        # To evaluate
        # print("Size: ",size/1024/1024,"MB")
        #print("Time ",cnt,": ",end_time - start_time," s")
        # print("")
    else:
        f.write("NO SOLUTION\n")

    # Delete previous data
    size=0
    mp.clear()
    mp_nguoc.clear()
    list_dif_zero.clear()
    ketqua.clear()

    f.close()
    return 

def tachhangtu(a):
    b = []
    n= len(a)
    term = False
    hangtu=""
    for i in range(n):
        if(term==False):
            hangtu=hangtu+a[i]
            term=True
        else:
            if(a[i]=='+' or a[i]=='-'):
                if(a[i-1]=='*'):
                    hangtu=hangtu+a[i]
                else:
                    term=False
                    dau=1
                    new_hangtu=""
                    for u in hangtu:
                        if(u=='-'):
                            dau*=-1
                        else:
                            if(u!='+'):
                                new_hangtu= new_hangtu+u
                    b.append([dau,new_hangtu])

                    hangtu=a[i]
            else:
                hangtu= hangtu+a[i]

    dau=1
    new_hangtu=""
    for u in hangtu:
        if(u=='-'):
            dau*=-1
        else:
            if(u!='+'):
                new_hangtu= new_hangtu+u
    b.append([dau,new_hangtu])
    return b

def solve_khac_khong(pheptinh):
    global list_dif_zero
    check = False
    for u in pheptinh:
        
        if(check==False):
            list_dif_zero[u]=1
            check=True
        if(u<'A' or u>'Z'):
            check=False
            continue
    return 

def Alphabet(input : str):
    asciivalue = ord(input)
    return asciivalue > 64 and asciivalue < 91

def reversed(input : str):
    return '+' if input == '-' else '-'

def khungoac(input : str):
    reverse = False
    stack = []
    res=""
    temp='+'
    index = 0
    while index < len(input):
        if Alphabet(input[index]):
            res+=input[index]
            index+=1
            continue
        if input[index] == '(':
            stack.append(reverse)
            if input[index-1] == '-':
                reverse = 1 - reverse
            if Alphabet(input[index+1]):
                res+=temp
            else:
                res+=reversed(temp)
                index+=2
                continue
        if input[index] == ')':
            reverse = stack.pop()
        if input[index] =='+' or input[index] == '-':
            temp = reversed(input[index]) if reverse else input[index]
            if input[index+1] =='(':
                index+=1
                continue
            res+=temp
            index+=1
            continue
        index+=1
    return res

def main():

    f = open('input_level4.txt','r')
    pheptinh = ''
    cnt = 0
    while True:
        data = f.readline()
        if data == '':
            break
        pheptinh = data.strip()
        
        solve_khac_khong(pheptinh)

        global mp
        global mp_nguoc

        # map with interger
        count = -1
        for u in pheptinh:
            if(u>='A' and u<='Z'):
                if u not in mp: 
                    count +=1
                    mp[u]=count
                    mp_nguoc[count]=u
            

        # Tách kết quả sau dấu bằng
        kq = ""
        check = False 
        for u in pheptinh:
            if(check == True and u>='A' and u<='Z'):
                kq = kq + u
            if(u=='='):
                check = True

        # Tách các hạng tử trước dấu bằng
        new_pheptinh=""
        for u in pheptinh:
            if( u=='='):
                break
            else:
                new_pheptinh = new_pheptinh + u
        pheptinh = new_pheptinh

        # Xem xét level
        check_dau_nhan=False
        check_dau_ngoac= False
        for u in pheptinh:
            if(u=='*'):
                check_dau_nhan = True
            if(u=='(' or u==')'):
                check_dau_ngoac = True



        #----------Tiền xử lý----------
    
        # Nếu biểu thức có dấu ngoặc mà không có dấu nhân => Level 3
        if(check_dau_ngoac==True and check_dau_nhan==False):
            pheptinh = khungoac(pheptinh)

        # Nếu biểu thức có dấu nhân => Level 4 
        if(check_dau_nhan==True):
            # Khử ngoặc và dấu trừ
            pheptinh = eli_minus(pheptinh)
            pheptinh = nhanphanphoi2sohang(pheptinh)
            pheptinh = khu_dau_tru(pheptinh)
            # #Chuyển về dạng đơn thức nếu như dang có phép nhân
            pheptinh = dangdonthuc(pheptinh)            
            pheptinh = khu_dau_tru(pheptinh)
        
        if(pheptinh[0]!='+' and pheptinh[0]!='-'):
            pheptinh= '+'+pheptinh

        #Nén số + Tái cấu trúc lại các cột constraint 
        c = nensolv4(pheptinh,kq)
        
        solve(c, cnt)   
        cnt += 1
    f.close()
    
main()


