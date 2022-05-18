***

Viết chương trình quản lý sản phẩm trong kho hàng của một siêu thị, biết rằng mỗi sản phẩm gồm có các thuộc tính: Mã sản phẩm, tên sản phẩm, đơn giá, số lượng.

 Chương trình gồm các chức năng sau:

Đọc dữ liệu có sẵn từ file text chứa các sản phẩm rồi lưu vào Linked List.
Nhập và thêm một sản phẩm vào cuối của danh sách Linked List.
Hiển thị thông tin của các sản phẩm trong Linked List.
Lưu danh sách các sản phẩm vào file.
Tìm kiếm thông tin của sản phẩm theo ID.
Xóa sản phẩm trong danh sách theo ID.
Sắp xếp các sản phẩm  trong danh sách theo ID.
Biểu diễn số lượng sản phẩm (đang ở hệ đếm cơ số 10) của phần tử đầu tiên trong Linked List về hệ đếm nhị phân bằng phương pháp đệ quy.
Đọc dữ liệu từ file chứa các sản phẩm rồi lưu vào stack. Sau đó lấy từng sản phẩm ra khỏi stack rồi hiển thị ra màn hình.
Đọc dữ liệu từ file chứa các sản phẩm lưu vào queue. Sau đó lấy từng sản phẩm ra khỏi queue rồi hiển thị ra màn hình.

***

Hướng dẫn

Một sản phẩm có 4 trường cơ bản: ID, Title (lưu trữ ở dạng string), quantity (int) và price (float).

Chức năng và yêu cầu cơ bản

1. Thiết kế Menu

Có ít nhất 10 chức năng để lựa chọn
Mỗi chức năng tương ứng với một câu hỏi
Không hạn chế số lần lựa chọn
2. Chức năng và yêu cầu 

Đọc dữ liệu có sẵn từ file và lưu vào danh sách móc nối và hiển thị danh sách ra màn hình
Nhập và thêm một sản phẩm vào cuối của danh sách móc nối
Hiển thị thông tin của các sản phẩm trong danh sách móc nối
Lưu danh sách móc nối các sản phẩm vào file
Tìm kiếm thông tin của sản phẩm theo ID
Xóa sản phẩm trong danh sách theo ID
Sắp xếp các sản phẩm  trong danh sách móc nối theo ID
Biểu diễn số lượng sản phẩm (đang ở hệ đếm cơ số 10) của phần tử đầu tiên trong Linked List ra hệ đếm nhị phân bằng phương pháp đệ quy.
Đọc dữ liệu từ file chứa các sản phẩm rồi lưu vào stack. Hiển thị ra màn hình các sản phẩm có trong stack.
Đọc dữ liệu từ file chứa các sản phẩm lưu vào queue. Hiển thị ra màn hình các sản phẩm có trong queue.
3. Tổ chức code

Lớp Node để quản lý thông tin và hành vi của mỗi node trong danh sách
Lớp MyList chứa thông tin và hành vi cơ bản của một danh sách móc nối
Lớp MyStack chứa thông tin và các hành vi cơ bản của stack
Lớp MyQueue chứa thông tin và các hành vi cơ bản của queue 
Lớp OperationToProduct sẽ chứa các phương thức thức biểu diễn các yêu cầu chức năng của bài toán
Lớp AS2_Main là lớp để tạo menu và thực hiện thực hiện các chức năng  trong lớp ProductEngine của bài toán
Kết quả khi chạy chương trình (Test case)

run:

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

+-----------------------------------------.+

 

Nếu bấm 1, màn hình sẽ hiện ra:

Choice 1: Load data from file and display

Hướng dẫn nhập vào đường dẫn file:

Please enter the find path: ...

Nếu file hợp lệ, hiển thị: 

The file is loaded successfully!

Nếu file không hợp lệ, hiển thị:

File-path is not correct!

 

Nếu bấm 2, màn hình sẽ hiện ra:

Choice 2: Input & add to the end

Hướng dẫn nhập vào ID cho sản phẩm mới:

Please enter the new product ID: ...

VD về new ID: P08

Hướng dẫn nhập vào tên sản phẩm:

Please enter the product's name: ...

VD về tên sản phẩm: French fries

Hướng dẫn nhập vào số lượng sản phẩm:

Please enter the product's quantity: ...

VD về số lượng sản phẩm: 5

Hướng dẫn nhập vào giá sản phẩm:

Please enter the product's price: ...

VD về số lượng sản phẩm: 3

 

Nếu bấm 3, màn hình sẽ hiện ra:

Choice 3: Display data

ID |  Title   | Quantity | price

P03  |  Sugar      |   12    | 25.1

P01  |  Miliket      |   10    | 5.2

P02  |  Apple      |   5    | 4.3

P05  |  Rose      |   7    | 15.4

P07  |  Beer      |   11    | 12.2

P04  |  Book      |   9    | 5.2

P06  |Rice |   10   | 3

 

Nếu bấm 4, màn hình sẽ hiện ra:

Choice 4: Save product list to file

Hướng dẫn nhập vào đường dẫn output:

VD về đường dẫn output: '/home/database/outdata.txt'

Please enter the output path: ...

Sau khi lưu file, hiển thị: 

The file is saved successfully!

 

Nếu bấm 5, màn hình sẽ hiện ra:

Choice 5: Search by ID

Hướng dẫn nhập vào ID:

Please enter the ID: ...

VD về ID cần tìm kiếm: P03

Nếu ID có trong dataset, hiển thị:

ID |  Title   | Quantity | price

P03  |  Sugar      |   12    | 25.1

Nếu ID không có trong dataset, hiển thị:

ID is not in the dataset!

 

Nếu bấm 6, màn hình sẽ hiện ra:

Choice 6: Deleted by ID

Hướng dẫn nhập vào ID:

Please enter the ID: ...

VD về ID cần xóa: P03

Nếu ID có trong dataset, hiển thị:

ID |  Title   | Quantity | price

P03  |  Sugar      |   12    | 25.1

The product is removed from the dataset successfully!

Nếu ID không có trong dataset, hiển thị:

ID is not in the dataset!

 

Nếu bấm 7, màn hình sẽ hiện ra:

Choice 7: Sorted by ID

ID |  Title   | Quantity | price

P01  |  Miliket      |   10    | 5.2

P02  |  Apple      |   5    | 4.3

P03  |  Sugar      |   12    | 25.1

P04  |  Book      |   9    | 5.2

P05  |  Rose      |   7    | 15.4

P06  |Rice |   10   | 3

P07  |  Beer      |   11    | 12.2

P08  |French fries |   5   | 3

 

Nếu bấm 8, màn hình sẽ hiện ra:

Choice 8: Convert to Binary

Hướng dẫn nhập vào ID:

Please enter the ID: ...

VD về ID cần convert giá trị quantity sang binary: P03

Nếu ID có trong dataset, hiển thị:

ID |  Title   | Quantity | price

P03  |  Sugar      |   12    | 25.1

Convert quantity to binary: 1100

The product is removed from the dataset successfully!

Nếu ID không có trong dataset, hiển thị:

ID is not in the dataset!

 

Nếu bấm 9, màn hình sẽ hiện ra:

Choice 9: Load to stack and display

ID |  Title   | Quantity | price

P06  |Rice |   10   | 3

P04  |  Book      |   9    | 5.2

P07  |  Beer      |   11    | 12.2

P05  |  Rose      |   7    | 15.4

P02  |  Apple      |   5    | 4.3

P01  |  Miliket      |   10    | 5.2

P03  |  Sugar      |   12    | 25.1

 

Nếu bấm 10, màn hình sẽ hiện ra:

Choice 10: Load to queue and display

ID |  Title   | Quantity | price

P03  |  Sugar      |   12    | 25.1

P01  |  Miliket      |   10    | 5.2

P02  |  Apple      |   5    | 4.3

P05  |  Rose      |   7    | 15.4

P07  |  Beer      |   11    | 12.2

P04  |  Book      |   9    | 5.2

P06  |Rice |   10   | 3

Chú ý: Sau mỗi khi thực thi mỗi bước thì cần hiển thị lại menu để người dùng dễ dàng đưa ra lựa chọn.