import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src import openprofile
from src import xapxepcuaso 
from src import createprofile



def main():
    while True:
        print("\n===== MENU CHÍNH =====")
        print("1️⃣ Mở profile trình duyệt")
        print("2️⃣ Sắp xếp cửa sổ trình duyệt")
        print("3️⃣ Tạo profile trình duyệt")
        print("0️⃣ Thoát")

        choice = input("Nhập lựa chọn của bạn: ").strip()

        if choice == "1":
            openprofile.open_profiles()
        elif choice == "2":
            xapxepcuaso.arrange_windows()
        elif choice == "3":
            createprofile.create_profiles()
        elif choice == "0":
            print("👋 Thoát chương trình. Hẹn gặp lại!")
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ! Vui lòng nhập lại.")

if __name__ == "__main__":
    main()
