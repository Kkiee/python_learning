def print_file(file_path):
    f=None
    try:
        f=open("file_path","r","utf=8")
        print(f.read())
    except Exception as e:
        print(f"出现异常为{e}")
    finally:
        if f:
            f.close()
def append_file(file_path,data):
    f=open(file_path,"a","utf8")