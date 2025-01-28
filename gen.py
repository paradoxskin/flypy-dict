#! /bin/python3

fcitx5_prefix = ";fcitx Version 0x03 Table file\n键码=abcdefghijklmnopqrstuvwxyz;\n码长=4\n[数据]\n"
rime_prefix = "# Rime dictionary\n# encoding: utf-8\n\n---\nname: flypy\nversion: \"0.0.1\"\nsort: original\n...\n\n"

# -> pure_dict.txt
def read_dic():
    with open("pure_dict.txt") as file:
        content = file.read()
    dic = [i.split(' ') for i in content.split("\n") if i != '']
    if len(set([len(i) for i in dic])) != 1:
        print("[!] dict format wrong.")
        return None
    return dic

# <- fcitx5/flypy.txt
def gen_fcitx5(dic):
    content = fcitx5_prefix
    for i in dic:
        content += f"{i[0]} {i[1]}\n"
    with open("fcitx5/flypy.txt", "w") as file:
        file.write(content)

# <- rime/flypy.dict.yaml
def gen_rime(dic):
    content = rime_prefix
    for i in dic:
        content += f"{i[1]}\t{i[0]}\n"
    with open("rime/flypy.dict.yaml", "w") as file:
        file.write(content)

def main():
    dic = read_dic()
    if dic:
        gen_fcitx5(dic)
        gen_rime(dic)
    print("[v] done.")

if __name__ == "__main__":
    main()
