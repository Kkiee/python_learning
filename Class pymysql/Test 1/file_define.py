from data_define import Record
import json
class FileReader:

    def read_data(self)->list[Record]:
        pass

class TextFileReader(FileReader):

    def __init__(self,path):
        self.path=path

    def read_data(self):
        f=open(self.path,"r",encoding="UTF-8")
        record_list=[]
        lines=f.readlines()
        for line in lines:
            line=line.strip()
            line=line.split(",")
            record=Record(line[0],line[1],int(line[2]),line[3])
            record_list.append(record)

        f.close()
        return record_list

class JsonFileReader(FileReader):

    def __init__(self,path):
        self.path=path

    def read_data(self):
        f=open(self.path,"r",encoding="UTF-8")
        record_list=[]
        for line in f.readlines():
            data_dict=json.loads(line)
            record=Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == "__main__":
    text_file_reader = TextFileReader("D:/2011年1月销售数据.txt")
    list1 = text_file_reader.read_data()
    json_file_reader = JsonFileReader("D:/2011年2月销售数据JSON.txt")
    list2 = json_file_reader.read_data()
    for l in list1:
        print(l)
    for l in list2:
        print(l)