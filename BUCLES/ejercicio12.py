"""


Escriba un programa que muestre (por filas) la Tabla ASCII, 
empezando con el código 33 y terminando con el 127 (solución):

033 !   034 "   035 #   036 $   037 %
038 &   039 '   040 (   041 )   042 *
043 +   044 ,   045 -   046 .   047 /
048 0   049 1   050 2   051 3   052 4
053 5   054 6   055 7   056 8   057 9
058 :   059 ;   060 <   061 =   062 >
063 ?   064 @   065 A   066 B   067 C
068 D   069 E   070 F   071 G   072 H
073 I   074 J   075 K   076 L   077 M
078 N   079 O   080 P   081 Q   082 R
083 S   084 T   085 U   086 V   087 W
088 X   089 Y   090 Z   091 [   092 \
093 ]   094 ^   095 _   096 `   097 a
098 b   099 c   100 d   101 e   102 f
103 g   104 h   105 i   106 j   107 k
108 l   109 m   110 n   111 o   112 p
113 q   114 r   115 s   116 t   117 u
118 v   119 w   120 x   121 y   122 z
123 {   124 |   125 }   126 ~   127

"""



code = 33
row = 0
while code <= 127:
    asc = f' {code:>4} {chr(code):>2}'
    code += 1
    row += 1
    print(asc,end=' ')
    if row == 5:
        row = 0
        print()       
        

print('--------------------------------------------')       
# Solución:


line = ''
i = 1
for code in range(33, 128):
    char = chr(code)
    line += f'{code:03d} {char}\t'
    if i % 5 == 0:
        print(line)
        line = ''
    i += 1   
    