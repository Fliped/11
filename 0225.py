void CString2Char(CString str, char ch[])

{undefined

int i;

char *tmpch;

int wLen = WideCharToMultiByte(CP_ACP, 0, str, -1, NULL, 0, NULL, NULL);//得到Char的长度

tmpch = new char[wLen + 1]; //分配变量的地址大小

WideCharToMultiByte(CP_ACP, 0, str, -1, tmpch, wLen, NULL, NULL); //将CString转换成char*

for (i = 0; tmpch[i] != '0'; i++) ch[i] = tmpch[i];

ch[i] = '0';

}
————————————————
版权声明：本文为CSDN博主「上世是朵花」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_29975633/article/details/112166648