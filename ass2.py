# params for formatting
PATH = ''
FIELDS = ['ID', 'Title', 'quantity', 'price']
input_file = PATH + '/Data.txt'
output_file = PATH + '/data_out.txt'

class Product:
    def __init__(self, id, title, quantity, price):
        self.id = str(id)
        self.title = str(title)
        self.quantity = int(quantity)
        self.price = float(price)
    
    def __le__(self, another):
        return True if self.id <= another.id else False

    def __gt__(self, another):
        return True if self.id > another.id else False

    def __str__(self):
        return f'ID: {self.id}, Ten: {self.title}, So luong: {self.quantity}, Gia tien: {self.price}'
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        print(self.data)

class LinkedList:
    def __init__(self, data=None):
        self.head = None
        if data is not None:
            self.head = Node(data.pop(0))
            p = self.head  
            for e in data:
                p.next = Node(e)
                p = p.next

    def __str__(self):
        p = self.head
        out = []
        while p is not None:
            out.append(str(p.data))
            p = p.next
        return '\n'.join(out)
    
    def get(self, id):
        p = self.head
        while p is not None:
            if p.data.id == str(id):
                return p
            p = p.next    

    def length(self):
        p = self.head
        counter = 0
        while p is not None:
            counter += 1
            p = p.next
        return counter

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(data)

    def find(self, id):
        p = self.head
        while p is not None:
            if p.data.id == str(id):
                return p.data
            p = p.next
        return -1
    
    def remove(self, id):
        if self.head.data.id == str(id):
            self.head = self.head.next
            return True

        p = self.head
        while p.next is not None:
            if p.next.data.id == str(id):
                p.next = p.next.next
                return True
            else:
                p = p.next
        return False
    # hoán đổi 2 node trong Linked List
    def swap(self, id1, id2):
        if id1 == id2:
            return

        pre1 = None
        cur1 = self.head
        while cur1 != None and cur1.data.id != str(id1):
            pre1 = cur1
            cur1 = cur1.next
        pre2 = None
        cur2 = self.head
        while cur2 != None and cur2.data.id != str(id2):
            pre2 = cur2
            cur2 = cur2.next
        if cur1 == None or cur2 == None:
            return
        # Trường hợp đặc biệt
        if pre1 is not None:
            pre1.next = cur2
        else:
            self.head = cur2
        if pre2 is not None:
            pre2.next = cur1
        else:
            self.head = cur1
        
        cur1.next, cur2.next = cur2.next, cur1.next

    def sort_ascending(self, iStart, iEnd):
        # phân vùng (chia đôi) để chuẩn bị sắp xếp
        def partition(iStart, iEnd):
            pivot = self.head
            for _ in range(iStart):
                pivot = pivot.next
            p = pivot.next
            p0 = pivot
            j = iStart
            while p is not None:
                if p.data <= pivot.data:
                    j += 1
                    if p0 is None:
                        p0 = self.head
                    else:
                        p0 = p0.next
                    self.swap(p0.data.id, p.data.id)
                p = p.next
            self.swap(pivot.data.id, p0.data.id)
            return j

        if iStart >= iEnd:
            return
        j = partition(iStart, iEnd)
        self.sort_ascending(iStart, j-1)
        self.sort_ascending(j+1, iEnd)        

class Stack:
    def __init__(self, data=None):
        self.stack = list()
        self.size = 0
        if data is not None:
            self.stack += data
            self.size += len(data)

    def __str__(self):
        out = []
        while not self.isEmpty():
            out.append(str(self.pop()))
        return '\n'.join(out)

    def isEmpty(self):
        return self.size == 0

    def push(self, value):
        self.stack.append(value)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('Popping from empty stack')
        self.size -= 1
        return self.stack.pop()
        
class Queue:
    def __init__(self, data=None):
        self.queue = list()
        self.size = 0
        if data is not None:
            self.queue += data
            self.size += len(data)
    
    def __str__(self):
        out = []
        while not self.isEmpty():
            out.append(str(self.dequeue()))
        return '\n'.join(out)

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, value):
        self.queue.append(value)
        self.size += 1
    
    def dequeue(self):
        self.size -= 1
        return self.queue.pop(0)    

    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[-1]
# Class Choice để xử lý lựa chọn từ người dùng    
class Choice:
    def __init__(self, choice=None):
        self.choice = choice
        self.input_stt = 'Lựa chọn của bạn (Vui lòng nhập STT tương ứng): '
        self.ll = LinkedList()
    # in màn hình Menu
    def menu(self):
        text = """
        +-------------------Menu------------------+
        1. Load data from file and display
        2. Input & add to the end.
        3. Display data
        4. Save product list to file.
        5. Search by ID
        6. Delete by ID
        7. Sort by ID.
        8. Convert to Binary 
        9. Load to stack and display
        10. Load to queue and display.
        Exit:
        0. Exit
        +------------------------------------------+"""
        print(text)
    # Lấy input từ bàn phím
    def get_choice(self):
        self.choice = input(self.input_stt)
        self.validation()
    # Kiểm tra tính hợp lệ của lựa chọn
    def validation(self):
        #input_statement = 'Lựa chọn của bạn (Vui lòng nhập STT tương ứng): '
        #choice = input(input_statement)
        # Kiểm tra input cho den khi hop le
        while 1:
            try:
                self.choice = int(self.choice)
                if 0 <= self.choice <= 10:
                    break
                else:
                    print('Vui lòng nhập STT từ 0-10.')
            except ValueError:
                print('Vui lòng nhập 1 số nguyên.')
            
            self.get_choice()
    # Gọi thao tác tương ứng
    def operation(self):
        if self.choice == 1:
            Doc_du_lieu(self.ll, input_file)
        elif self.choice == 2:
            Them_san_pham(self.ll)
        elif self.choice == 3:
            Hien_thi_TTSP(self.ll)
        elif self.choice == 4:
            Luu_TTSP(self.ll, output_file)
        elif self.choice == 5:
            Tim_TTSP(self.ll)
        elif self.choice == 6:
            Xoa_TTSP(self.ll)
        elif self.choice == 7:
            Sap_xep_tang_dan(self.ll)
        elif self.choice == 8:
            id = input('Nhap ID: ')
            p = self.ll.get(id)
            print(p.data)
            print('So luong san pham dang nhi phan: ', Dang_nhi_phan(p.data.quantity))
        elif self.choice == 9:
            Ghi_vao_stack(input_file)
        elif self.choice == 10:
            Ghi_vao_queue(input_file)

# Các hàm dưới làm các hàm để thao tác với Linked List,...
# 1
def Doc_du_lieu(ll: LinkedList, input_file: str) -> LinkedList:
    with open(input_file) as f:
        next(f)       
        for line in f:
            lst = list(line.strip().split(','))
            p = Product(*lst)
            ll.add(p)
    print('Đã đọc dữ liệu từ file input!')
    
# 2
def Them_san_pham(ll: LinkedList) -> None:
    info = []
    for field in FIELDS:
        info.append(input(field + ': '))
    new_product = Product(*info)
    ll.add(new_product)
    print('Đã thêm 1 sản phẩm!')

# 3
def Hien_thi_TTSP(ll: LinkedList, message=None) -> None:
    if message is not None:
        print(message)
    print(ll)

# 4
def Luu_TTSP(ll: LinkedList, output_file: str) -> None:
    p = ll.head
    with open(output_file, 'w') as f:
        while p is not None:
            f.write(str(p.data) + '\n')
            p = p.next
    print('Đã lưu vào ', output_file)

#5
def Tim_TTSP(ll: LinkedList):
    id = input('Nhap ID san pham can tim: ')
    print(ll.find(id))

#6
def Xoa_TTSP(ll: LinkedList):
    id = input('Nhap ID san pham can xoa: ')
    b = ll.remove(id)
    print(f'Da xoa san pham id = {id}.' if b else 'Khong tim thay ID de xoa.')

#7
def Sap_xep_tang_dan(ll: LinkedList):
    print('Sau khi sap xep')
    ll.sort_ascending(0, ll.length()-1)
    print(ll)

#8
def Dang_nhi_phan(quantity: int):
    if quantity == 0:
        return 0
    return Dang_nhi_phan(quantity//2)*10 + quantity%2

#9
def Ghi_vao_stack(input_file: str):
    st = Stack()
    with open(input_file) as f:
        next(f)
        for line in f:
            info = line.strip().split(',')
            st.push(Product(*info))
    print('San pham trong Stack:')
    print(st)   

#10
def Ghi_vao_queue(input_file: str):
    q = Queue()
    with open(input_file) as f:
        next(f)
        for line in f:
            info = line.strip().split(',')
            q.enqueue(Product(*info))
    print('San pham trong Queue:')
    print(q)


def last_function():
    c = Choice()
    while c.choice != 0:
        # in menu
        c.menu()
        # Giá trị lấy từ bàn phím
        c.get_choice()
        c.operation()
    

if __name__ == '__main__':
    last_function()
    
