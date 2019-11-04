
#Reading a File
###从文件读取信息并放入python中
##1.built-in 内置函数open()
f = open('/my_path/my_file.txt', 'r')  #括号内（）的格式：路径，可选参数, 此处r表示read-only只读模式；r也是默认模式，可以不写；
file_data = f.read()##read()访问该文件中的内容,然后赋值给file_data()
f.close()##处理完文件f之后一定一定要关闭；来释放该文件占用的任何系统资源

#Writing to a File
f = open('another_file.txt', 'w')##'w'表示：write文件；在该‘w’模式打开文件，之前包含的任何内容都将被删除掉；若只想添加而不是删除，则用append()
f.write('Hello World!')
f.close()


# with特殊语法：执行完之后自动关闭文件
# with open('unit6-notes.pdf'. 'r') as f:## as f 表示赋值给f；只是在该缩进模块下有效。
#    file_data = f.read()


# Reading Line by Line
# Use the relevant part of the Python documentation to find a method that reads the next line of a file. 
# Put the name of the method in the box.
# The answer is: f.readline()


# Quiz: Flying Circus Cast List

def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)