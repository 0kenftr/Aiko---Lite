import time
import webbrowser
import os

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# Setting
gamepath = ""  # C:\Users\kenft\AppData\Roaming\.minecraft
gamelogfile = ""  # C:\Users\kenft\AppData\Roaming\.minecraft/logs
autojoindiscord = "true"  # default true
if autojoindiscord == "true":
    discord = 'https://discord.gg/uGSWp465'
    webbrowser.open(discord)
else:
    print('autojoindiscord not enable')

automatically_enter_the_log_folder = "False"  # Yêu cầu Aiko - Mc
if automatically_enter_the_log_folder == "True": # Yêu cầu Aiko - Mc
    print('Bạn đang sài bản miễn phí vui lòng tải bản full!!') # Yêu cầu Aiko - Mc
else:
    print('automatically enter the log file not enable')

manual = "True"

def Aiko_mclogs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        Aikologs = file.read()
    return Aikologs  # Return Aikologs here

# Manual mode
if manual == "True":
    file_path = "Aikomclogs/logs.txt"
    Aikologs = Aiko_mclogs(file_path)
else:
    print('Tính năng này đang tắt!')

time.sleep(0.2)
print(' $$$$$$\  $$\ $$\                         $$\ $$\   $$\               ')
time.sleep(0.2)
print('$$  __$$\ \__|$$ |                        $$ |\__|  $$ |              ')
time.sleep(0.2)
print('$$ /  $$ |$$\ $$ |  $$\  $$$$$$\          $$ |$$\ $$$$$$\    $$$$$$\  ')
time.sleep(0.2)
print('$$$$$$$$ |$$ |$$ | $$  |$$  __$$\ $$$$$$\ $$ |$$ |\_$$  _|  $$  __$$\ ')
time.sleep(0.2)
print('$$  __$$ |$$ |$$$$$$  / $$ /  $$ |\______|$$ |$$ |  $$ |    $$$$$$$$ |')
time.sleep(0.2)
print('$$ |  $$ |$$ |$$  _$$<  $$ |  $$ |        $$ |$$ |  $$ |$$\ $$   ____|')
print('$$ |  $$ |$$ |$$ | \$$\ \$$$$$$  |        $$ |$$ |  \$$$$  |\$$$$$$$\ ')
print('\__|  \__|\__|\__|  \__| \______/         \__|\__|   \____/  \_______|')
print('\n')
print('Discord : https://dsc.gg/cheatjar')
print('Free version ')


#crash logs
code1 = "Failed to start the Minecraft client due to error code 1"
code1073740791 = "Failed to start the Minecraft client due to error code 1073740791"
code1073740940 = "Failed to start the Minecraft client due to error code 1073740940"
code1073741819 = "Failed to start the Minecraft client due to exit code 1073741819"
error1 = """Sửa lỗi Error Code 1 trong Minecraft
Việc sửa lỗi Error code 1 trong Minecraft bao gồm việc giải quyết các vấn đề liên quan đến cấu hình Java, tương thích mod, và driver đồ họa. Dưới đây là hướng dẫn từng bước để khắc phục lỗi này:

1. Cập nhật Java
Đảm bảo rằng bạn đang sử dụng phiên bản mới nhất của Java. Minecraft yêu cầu một phiên bản cụ thể của Java, vì vậy việc có phiên bản không đúng có thể gây ra vấn đề.

Các bước:

Tải phiên bản Java mới nhất từ trang web chính thức.

Gỡ cài đặt các phiên bản Java cũ khỏi hệ thống của bạn.

Cài đặt phiên bản mới vừa tải về.

2. Kiểm tra Mod
Các mod lỗi thời hoặc không tương thích có thể gây ra các lỗi và sự cố.

Các bước:

Đảm bảo tất cả các mod được cài đặt tương thích với phiên bản Minecraft của bạn.

Vô hiệu hóa tất cả các mod và thử chạy Minecraft. Nếu hoạt động, bật từng mod một để xác định mod gây ra vấn đề.

3. Cập nhật Driver Đồ Họa
Các driver đồ họa lỗi thời có thể gây ra các vấn đề về hiệu suất và sự cố trong Minecraft.

Các bước:

Truy cập trang web của nhà sản xuất GPU của bạn (NVIDIA, AMD, Intel).

Tải và cài đặt các driver mới nhất cho card đồ họa của bạn.

Khởi động lại máy tính sau khi cài đặt.

4. Kiểm tra Cài đặt Minecraft
Đôi khi, cài đặt của Minecraft có thể bị hỏng.

Các bước:

Sao lưu các thế giới đã lưu của bạn.

Gỡ cài đặt hoàn toàn Minecraft.

Cài đặt lại Minecraft từ trang web chính thức.

5. Điều chỉnh Cài đặt Launcher của Minecraft
Đảm bảo rằng các cài đặt của launcher được cấu hình đúng.

Các bước:

Mở launcher của Minecraft.

Vào phần Installations và chọn hồ sơ của bạn.

Nhấn vào More Options.

Đảm bảo rằng đường dẫn Java Executable được đặt đúng, thường là như sau: C:\Program Files\Java\jre1.8.0_231\bin\javaw.exe.

6. Kiểm tra Cài Đặt Firewall và Antivirus
Phần mềm firewall hoặc antivirus có thể đôi khi chặn Minecraft chạy đúng cách.

Các bước:

Tạm thời vô hiệu hóa firewall và phần mềm antivirus của bạn.

Thử chạy lại Minecraft.

Nếu hoạt động, thêm Minecraft vào danh sách ngoại lệ trong cài đặt firewall và antivirus của bạn."""
error2 = """1. Cập nhật Driver Đồ Họa
Các driver đồ họa lỗi thời có thể gây ra các vấn đề về hiệu suất và sự cố trong Minecraft.

Các bước:

Truy cập trang web của nhà sản xuất GPU của bạn (NVIDIA, AMD, Intel).

Tải và cài đặt các driver mới nhất cho card đồ họa của bạn.

Khởi động lại máy tính sau khi cài đặt.

2. Đặt Thêm RAM cho Minecraft
Nếu máy tính của bạn không cung cấp đủ RAM cho Minecraft, lỗi này có thể xảy ra.

Các bước:

Mở Minecraft Launcher.

Chọn Installations và nhấn Edit trên cài đặt bạn muốn thay đổi.

Trong phần More Options, thay đổi giá trị -Xmx thành một số lớn hơn. Ví dụ: -Xmx2G sẽ phân bổ 2GB RAM cho Minecraft.

3. Tạm thời Vô hiệu hóa Antivirus và Firewall
Phần mềm antivirus hoặc firewall có thể gây xung đột với Minecraft và gây ra lỗi.

Các bước:

Tạm thời vô hiệu hóa phần mềm antivirus và firewall của bạn.

Thử chạy lại Minecraft.

Nếu hoạt động, thêm Minecraft vào danh sách ngoại lệ trong cài đặt antivirus và firewall của bạn.

4. Cài đặt lại Minecraft
Nếu các bước trên không giải quyết được vấn đề, bạn có thể cài đặt lại Minecraft.

Các bước:

Sao lưu các thế giới đã lưu của bạn.

Gỡ cài đặt hoàn toàn Minecraft.

Cài đặt lại Minecraft từ trang web chính thức."""
error3 = """Bạn
1073740940 cachs fix
Copilot
Để khắc phục lỗi Exit code -1073740940 trong Minecraft, bạn có thể thử các bước sau:

1. Cập nhật Driver Đồ Họa
Các driver đồ họa lỗi thời có thể gây ra các vấn đề về hiệu suất và sự cố trong Minecraft.

Các bước:

Truy cập trang web của nhà sản xuất GPU của bạn (NVIDIA, AMD, Intel).

Tải và cài đặt các driver mới nhất cho card đồ họa của bạn.

Khởi động lại máy tính sau khi cài đặt.

2. Đặt Thêm RAM cho Minecraft
Nếu máy tính của bạn không cung cấp đủ RAM cho Minecraft, lỗi này có thể xảy ra.

Các bước:

Mở Minecraft Launcher.

Chọn Installations và nhấn Edit trên cài đặt bạn muốn thay đổi.

Trong phần More Options, thay đổi giá trị -Xmx thành một số lớn hơn. Ví dụ: -Xmx2G sẽ phân bổ 2GB RAM cho Minecraft.

3. Tạm thời Vô hiệu hóa Antivirus và Firewall
Phần mềm antivirus hoặc firewall có thể gây xung đột với Minecraft và gây ra lỗi.

Các bước:

Tạm thời vô hiệu hóa phần mềm antivirus và firewall của bạn.

Thử chạy lại Minecraft.

Nếu hoạt động, thêm Minecraft vào danh sách ngoại lệ trong cài đặt antivirus và firewall của bạn.

4. Cài đặt lại Minecraft
Nếu các bước trên không giải quyết được vấn đề, bạn có thể cài đặt lại Minecraft.

Các bước:

Sao lưu các thế giới đã lưu của bạn.

Gỡ cài đặt hoàn toàn Minecraft.

Cài đặt lại Minecraft từ trang web chính thức."""
error4 = """Bạn
1073741819
Copilot
Lỗi Exit code -1073741819 trong Minecraft thường xảy ra do một số nguyên nhân phổ biến như lỗi ngẫu nhiên, các overlay không tương thích, driver đồ họa lỗi thời, vấn đề với mod, hoặc tệp game bị hỏng1
. Dưới đây là một số cách khắc phục:

1. Cập nhật Driver Đồ Họa
Cập nhật driver đồ họa của bạn để đảm bảo rằng bạn đang sử dụng phiên bản mới nhất1
.

Các bước:

Truy cập trang web của nhà sản xuất GPU của bạn (NVIDIA, AMD, Intel).

Tải và cài đặt các driver mới nhất cho card đồ họa của bạn.

Khởi động lại máy tính sau khi cài đặt2
.

2. Điều chỉnh hoặc Vô hiệu hóa Overlay
Một số overlay như Discord hoặc D3DGear có thể gây xung đột với Minecraft1
.

Các bước:

Điều chỉnh hoặc vô hiệu hóa các overlay trước khi chạy Minecraft1
.

Thử chạy lại Minecraft và xem lỗi có biến mất hay không1
.

3. Kiểm tra và Cập nhật Mod
Mod không tương thích hoặc bị hỏng có thể gây ra lỗi này1
.

Các bước:

Đảm bảo tất cả các mod được cài đặt tương thích với phiên bản Minecraft của bạn2
.

Vô hiệu hóa tất cả các mod và thử chạy Minecraft2
. Nếu hoạt động, bật từng mod một để xác định mod gây ra vấn đề2
.

4. Kiểm tra và Khắc phục Tệp Game
Tệp game bị hỏng có thể gây ra lỗi này1
.

Các bước:

Sao lưu các thế giới đã lưu của bạn2
.

Gỡ cài đặt hoàn toàn Minecraft2
.

Cài đặt lại Minecraft từ trang web chính thức2
.

5. Khắc phục Lỗi Ngẫu Nhiên
Đôi khi lỗi này có thể do lỗi ngẫu nhiên trong game.

Các bước:

Khởi động lại Minecraft và xem lỗi có biến mất hay không
."""
def main():
    print("""      +------+------------------------------------+
          | nhập |     Các tính năng hiện có          |
          +-------------------------------------------+
          |   1  |  Nether coord to over coord        |
          +-------------------------------------------+
          |   2  |  Over coord to nether coord        |
          +-------------------------------------------+
          |   3  |  fix crash error                   |
          +-------------------------------------------+
          |   4  |  Client archive                    |
          +-------------------------------------------+
          |   5  |  Client bind                       |
          +-------------------------------------------+""")
    print('Đây chỉ là free version 1 số tính năng sẽ không có hoặc không đầy đủ!!')
    time.sleep(2)
    print('Ví dụ : Chọn client archive nhập số 4')
    mode = str(input('Chọn tính năng --> '))
    if mode == "1":
        print('nhập tọa độ!')
        inputx = float(input('x = '))
        inputz = float(input('z = '))
        print(f'nether x = {inputx} z = {inputz} ', 'over x = ', inputx * 8, 'z = ', inputz * 8)
        print('Baritone nether : #goto', inputx * 8, inputz * 8)
        input('bấm enter để trở về menu chính...')
        main()
    if mode == "2":
        print('nhập tọa độ!')
        inputx = float(input('x = '))
        inputz = float(input('z = '))
        print(f'over x = {inputx} z = {inputz} ', 'nether x = ', inputx / 8, 'z = ', inputz / 8)
        print('Baritone overworld : #goto', inputx / 8, inputz / 8)
        input('bấm enter để trở về menu chính...')
        main()
    if mode == "3":
        print('Đưa log của bạn vào Aikomclogs/log.txt') #Nếu đã đưa vào rồi thì không cần quan tâm cái này!
        if code1 in Aikologs:
            print("---------------------")
            print("Error code 1 : True")
            print("Error code 1073740791 : False")
            print('Error code 1073740940 : False')
            print("Process crashed with exit code 1073741819 : False")
            print("---------------------")
            print(error1)

        if code1073740791 in Aikologs:
            print("---------------------")
            print("Error code 1 : False")
            print("Error code 1073740791 : True")
            print('Error code 1073740940 : False')
            print("Process crashed with exit code 1073741819 : False")
            print("---------------------")

        if code1073740940 in Aikologs:
            print("---------------------")
            print("Error code 1 : False")
            print("Error code 1073740791 : False")
            print('Error code 1073740940 : True')
            print("Process crashed with exit code 1073741819 : False")
            print("---------------------")

        if code1073741819 in Aikologs:
            print("---------------------")
            print("Error code 1 : False")
            print("Error code 1073740791 : False")
            print('Error code 1073740940 : False')
            print("Process crashed with exit code 1073741819 : True")
            print("---------------------")

        input('bấm enter để trở về menu chính...')
        main()
    if mode == "4":
        discordurl = 'https://discord.gg/A5manw27VC'
        webbrowser.open(discord)
        print('bạn đã truy cập vào client archive')
        input('bấm enter để trở về menu chính...')
        main()
    if mode == "5":
        print("""Client bind list
                    Meteor : Rshift ( rightshift) | prefix : Cần Aiko-Mc để xem full thông tin!
                    Thunderhack : P | prefix : Cần Aiko-Mc để xem full thông tin!
                    Impact : Rshift ( rightshift ) | prefix : Cần Aiko-Mc để xem full thông tin!
                    Lambda : Y | prefix : Cần Aiko-Mc để xem full thông tin!
                    3arthh4ck : +bind clickgui {key} | prefix : +
                    Future Client : Rshift ( rightshift ) | prefix : Cần Aiko-Mc để xem full thông tin!
                    """)
        print('sử dụng bản Aiko-Mc để có toàn bộ tính năng!')
        input('Bấm enter để trở về menu chính...')
        main()
main()