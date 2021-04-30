class FechaHora():
    __dia=0
    __mes=0
    __año=0
    __hora=0
    __min=0
    __seg=0
    def __init__(self,dia=1,mes=1,año=2021,hora=0,min=0,seg=0):
        if(hora>=0 and hora<24 and min>=-1 and min<=60 and seg>-1 and seg<=60 and mes>0 and mes<13):
            if((año%400==0) or (año%100==0 and año%4==0)):
                mesbisiestos=[31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                mesbisiestos=[31,28,31,30,31,30,31,31,30,31,30,31]
            if(dia<=mesbisiestos[mes-1] and dia>0):
                self.__dia=dia
                self.__mes=mes
                self.__año=año
                self.__hora=hora
                self.__min=min
                self.__seg=seg
            else:
                print("dia mal ingresado")
    def Mostrar(self):
        print("--------------")
        print(self.__dia)
        print(self.__mes)
        print(self.__año)
        print(self.__hora)
        print(self.__min)
        print(self.__seg)
        print("--------------")
        print("{}/{}/{}/|{}:{}:{}".format(self.__dia,self.__mes,self.__año,self.__hora,self.__min,self.__seg))
    def __add__(self,otro):
        año=self.__año
        mes=self.__mes
        dia=self.__dia
        h=self.__hora + otro.gethora()
        m=self.__min + otro.getmin()
        s=self.__seg + otro.getseg()
        if((año%400==0) or (año%100==0 and año%4==0)):
            mesbisiestos=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            mesbisiestos=[31,28,31,30,31,30,31,31,30,31,30,31]
        if(s >= 60):
            if(s == 60):
                s=0
                m+=1
            else:
                s-=60
                m+=1
        if(m >= 60):
            if(m==60):
                m=1
                h+=1
            else:
                m-=60
                h+=1
        if(h > 24):
            if(h==24):
                h=0
                dia+=1
            else:
                h-=24
                dia+=1
        if(dia > mesbisiestos[mes-1]):
            dia-=24
            mes+=1
        if(mes > 12):
            mes-=12
            año+=1
            if(mes > 12):
                mes-=12
                año+=1
        print(año)
        print(dia)
        print(mes)
        print(h)
        print(m)
        print(s)
        return(FechaHora(dia,mes,año,h,m,s))
    def __radd__(self,otro):
        año=self.__año
        mes=self.__mes
        dia=self.__dia
        h=self.__hora
        m=self.__min
        s=self.__seg
        #h=self.__hora + otro.gethora()
        #m=self.__min + otro.getmin()
        #s=self.__seg + otro.getseg()
        if((año%400==0) or (año%100==0 and año%4==0)):
            mesbisiestos=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            mesbisiestos=[31,28,31,30,31,30,31,31,30,31,30,31]
        if(type(otro)==int):
            if(otro > 0):
                dia+=otro
                while(dia > mesbisiestos[mes-1]):
                    if(mes==12):
                        mes=1
                        año+=1
                    else:
                        dia-=mesbisiestos[mes-1]
                        mes+=1
                return(FechaHora(dia,mes,año,h,m,s))  
        else:
            h=self.__hora + otro.gethora()
            m=self.__min + otro.getmin()
            s=self.__seg + otro.getseg()

            if(s >= 60):
                if(s == 60):
                    s=0
                    m+=1
                else:
                    s-=60
                    m+=1
            if(m >= 60):
                if(m==60):
                    m=1
                    h+=1
                else:
                    m-=60
                    h+=1
            if(h > 24):
                if(h==24):
                    h=0
                    dia+=1
                else:
                    h-=24
                    dia+=1
            if(dia > mesbisiestos[mes-1]):
                dia-=24
                mes+=1
            if(mes > 12):
                mes-=12
                año+=1
                if(mes > 12):
                    mes-=12
                    año+=1
            print(año)
            print(dia)
            print(mes)
            print(h)
            print(m)
            print(s)
            return(FechaHora(dia,mes,año,h,m,s))
    def __sub__(self,otro):
        if((self.__año%400==0) or (self.__año%100==0 and self.__año%4==0)):
            mesbisiestos=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            mesbisiestos=[31,28,31,30,31,30,31,31,30,31,30,31]
        if(type(otro)!=float and otro>0):
            dia=self.__dia
            año=self.__año
            mes=self.__mes
            dia=dia - otro
            while(dia<1):
                if(mes==0):
                    dia+=31
                    mes=12
                    año-=1
                else:
                    dia=mesbisiestos[dia-2]
                    mes-=1
            print(dia)
            print(año)
            print(mes)
            return (FechaHora(dia,mes,año,self.__hora,self.__min,self.__seg))