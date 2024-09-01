> 注意：fcitx 与 rime 的码表键值位置顺序相反

# fcitx5

```bash
libime_tabledict flypy.txt flypy.dict
cp flypy.conf /usr/share/fcitx5/inputmethod/flypy.conf
cp flypy.dict /usr/share/libime/flypy.dict
```
# rime

复制放到用户文件夹下，具体位置：

```bash
# windows
%APPDATA%\Rime

# mac
~/Library/Rime

# linux
ibus-rime: ~/.config/ibus/rime
fcitx-rime: ~/.config/fcitx/rime
fcitx5-rime: ~/.local/share/fcitx5/rime
```

> 已找到win下最佳挂接码表的方案：小狼豪 (rime框架在win下的实现)
>
> 鉴于安全问题，不建议使用 搜狗/百度 输入法
