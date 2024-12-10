import psutil,time
import auto,copy

app_name = "PPSSPPWindows64.exe"

def check_process(app):
    #現在実行中のプロセスのリストを取得
    for proc in psutil.process_iter(['name']):
        #name属性の値と引数の一致を調べる
        if proc.info['name'] == app:
            return True
    return False

app_running = False

while True:
    is_running = check_process(app_name)

    if is_running and not app_running:
        auto.main()
        app_running = True

    elif not is_running and app_running:
        app_running = False
        copy.main()
    time.sleep(1)



