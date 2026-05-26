while True:
    num_employees_str = input("Nhập số lượng nhân viên: ").strip()
    
    # Validation cơ bản bảo vệ hệ thống nếu người dùng bỏ trống
    if not num_employees_str:
        print("[!] Vui lòng nhập một số nguyên lớn hơn 0.\n")
        continue
        
    num_employees = int(num_employees_str)
    print() 

    for i in range(1, num_employees + 1):
        print(f"Nhân viên {i}")
        
        # Nhập thông tin chi tiết cho từng nhân sự
        emp_name = input("Tên nhân viên: ").strip()
        days_worked = int(input("Số ngày đi làm: "))
        
        # Hiển thị tiêu đề thông tin xuất ra
        print("Thông tin nhân viên:")
        print(f"Tên: {emp_name}")
        print(f"Số ngày đi làm: {days_worked}")
        
        # LOGIC ĐÁNH GIÁ CHUYÊN CẦN 
        if days_worked < 20:
            print("Cần cải thiện chuyên cần")
        else:
            print("Nhân viên chuyên cần tốt")
            
        print() # Dòng trống phân tách giữa các nhân viên

    # ĐIỀU HƯỚNG TIẾP TỤC HOẶC KẾT THÚC 
    user_choice = input("Tiếp tục chương trình? (y/n): ").strip().lower()
    print() # Tạo khoảng trống dòng theo mẫu
    
    # Nếu chọn 'n', bẻ gãy vòng lặp ngoài để đóng hệ thống
    if user_choice == 'n':
        print("Chương trình kết thúc")
        break