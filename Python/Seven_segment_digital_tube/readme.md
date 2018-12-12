# 七段数码管绘制模块使用指南

## Seven segment digital tube use docment

---

#### 本模块由Mr.Raphael制作，基于BSD协议，请使用者遵守此协议

##### (The Description document is write by Mr.Raphael ,a poor English writer,this document For reference only. If you want to know the accuracy document ,[Please read English version of this document](). )

This module is design by Mr.Raphael ,it observe BSD protocal.Please observe this protocal if you want to use it.

#### 此模块授权所有人使用，可以自由修改，也可以用于商业用途

This module is design for everyone.You can both change it and use for comercial application.

---

---

##### 你可以使用以下语法来调用此模块。

##### You can use the follow grammar to use this module.

请先导入此模块，然后调用ssdt(year[,month=0,day=0,n=1,p_size=10,p_color='red',c_space=25)]其中橙色等待是可选参数 。控制参数([n])表如下：

Please import the module first ,then use  fuction ssdt(year[,month=0,day=0,n=1,p_size=10,p_color='red',c_space=25])

The follow is the list of control parameter([n]).

                n=1            显示单组数字 # Just display one group number.
    
                n=(2,3)        分别用于显示2-3组数字 # For two or three groups number
    
                n=0            显示年月日#For year ,month & day display                              

当你仅需绘制一个数字时，主要使用参数[year]即可，当您用于显示年份时，需要使用 [year,month,day,n]四个参数。当你需要使用2-3组数字时，您需要定义year,month,n三个参数。

You can just use one parameter [year] if you only for display one number. If you want show date you need use four of parameter [year,month,day,n]. If you want to show two or three groups number ,you shoud use two or three parameter.

---

其他参数：    #Other parameter

- p_size          数码管粗细 #The size of pen

- p_color         数码管颜色    #Color

- c_space     两个数字的间隔    #The spcaing of two numbers

---

顺便说一下，不建议使用多个参数控制模块，最好分次调用此模块

By the way. The module has some bug. It maybe some err if you want to use it with mult-parameter. you can get it for double or more times for show more than single group numbers 



---

### 2018年12月12日更新 对应文件[Seven_segment_digital_tube_sourcec_code _upgrade_1_0_0_1.py]

#### December 12, 2018 Update [Seven_segment_digital_tube_sourcec_code _upgrade_1_0_0_1.py]

##### 增加[drawDigitPro(digit,space,size)]函数，可以通过此函数绘制单个数码管，并且可以使用space参数定义两根管子之间的间隙，默认是5，以及使用size参数定义管子大小，默认是35

Add [drawDigitPro(digit,space,size)] as a new  fuction. The gap between the two pipes can be defined by using the space parameter, which defaults to 5, and the size of the pipe can be defined by using the size parameter, which defaults to 35.

