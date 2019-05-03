#### 读入图像
```python3
img = cv2.imread(文件名,[,参数])
```
- cv2.IMREAD_UNCHANGED (图像不可变)
- cv2.IMREAD_GRAYSCALE (灰度图像)
- cv2.IMREAD_COLOR (读入彩色图像)
- cv2.COLOR_BGR2RGB (图像通道BGR转成RGB)

#### 显示图像
```python3
cv2.imshow(窗口名, 图像名)
```

#### 窗口等待
键盘绑定函数，共一个参数，表示等待毫秒数，将等待特定的几毫秒，看键盘是否有输入，返回值为ASCII值。如果其参数为0，则表示无限期的等待键盘输入；参数>0表示等待delay毫秒；参数<0表示等待键盘单击
```python3
cv2.waitKey(delay)
```

#### 删除所有窗口
```python3
// 删除所有窗口
cv2.destroyAllWindows()
// 删除指定的窗口 
cv2.destroyWindows()
```

#### 写入图片
```python3
retval = cv2.imwrite(文件地址, 文件名)
```