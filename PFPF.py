import os
os.system("cls")
import time
import random
from time import sleep

print("\t♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡")
print("\t¡BIENVENIDO A 'AGILIZA TU MENTE'!")
print("\t♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡")
print("\nEste es un juego matemático donde se pone en desafío tu capacidad de resolver operaciones combinadas en el menor tiempo posible.")


for i in range(0,5):
    print(5-i)
    sleep(1)

while True:
    de=input("¿Desea jugar?:  (si) (no) = ")
    if de == "si":
        print("Resuelva las operaciones en el menor tiempo posible")
        print("Comienza el juego ")

        from time import sleep
        for i in range(0,3):
            print(3-i)
            sleep(1)

        print("Responda lo mas rápido posible")
        jugar= "si"
        for i in range(0,2):
            inicio=time.time()

            numazar=random.randint(1,25)
            numazar1=random.randint(1,25)
            
            r=int(input("¿Cuánto es: "+str(numazar)+"+"+str(numazar1)+ " ? = "))
            final=time.time()
            tiempo=round(final-inicio,0)
            r1=numazar+numazar1
    
            if r == r1:
                print("Felicidades, respuesta correcta ◉‿◉ ,",end=" ")
                if tiempo < 7:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                if tiempo >= 7 and tiempo < 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Lo puedes hacer mejor!")
                if tiempo >= 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Te falta practicar velocidad mental, pero vamos bien!")
            else:
                print(" Respuesta incorrecta ")
                print("\tGAME OVER ")
                print("\t☝ THANKS (｡◕‿◕｡)☝")
                print(" Hasta luego, regresa pronto   ")
                
            
                break
            
    
            numazar=random.randint(1,25)
            numazar1=random.randint(1,25)
            
            z=int(input("¿Cuánto es: "+str(numazar)+"-"+str(numazar1)+ " ? = "))
            final=time.time()
            tiempo=round(final-inicio,0)
    
            z1=numazar-numazar1

            if z == z1:
                print("Felicidades, respuesta correcta ◉‿◉ ,",end=" ")
                if tiempo < 7:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                if tiempo >= 7 and tiempo < 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Lo puedes hacer mejor!")
                if tiempo >= 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Te falta practicar velocidad mental, pero vamos bien!")
            else:
                print(" Respuesta incorrecta ")
                print("\tGAME OVER ")
                print("\t☝ THANKS (｡◕‿◕｡)☝")
                print(" Hasta luego, regresa pronto   ")
    
            
                break
           

            numazar=random.randint(1,25)
            numazar1=random.randint(1,25)
            
            t=int(input("¿Cuánto es: "+str(numazar)+"+"+str(numazar1)+ " ? ="))
            final=time.time()
            tiempo=round(final-inicio,0)
            t1=numazar+numazar1
            if t == t1:
                print("Felicidades, respuesta correcta ◉‿◉ ,",end=" ")
                if tiempo < 7:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                if tiempo >= 7 and tiempo < 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Lo puedes hacer mejor!")
                if tiempo >= 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Te falta practicar velocidad mental, pero vamos bien!")
          
            else:
                print(" Respuesta incorrecta ")
                print("\tGAME OVER ")
                print("\t☝ THANKS (｡◕‿◕｡)☝")
                print(" Hasta luego, regresa pronto   ")

                break


            
            numazar=random.randint(1,25)
            numazar1=random.randint(1,25)
            
            u=int(input("¿Cuánto es: "+str(numazar)+"+"+str(numazar1)+ " ? = "))
            final=time.time()
            tiempo=round(final-inicio,0)
            u1=numazar+numazar1
    
            if u == u1:
                print("Felicidades, respuesta correcta ◉‿◉ ,",end=" ")
                if tiempo < 7:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                if tiempo >= 7 and tiempo < 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Lo puedes hacer mejor!")
                if tiempo >= 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Te falta practicar velocidad mental, pero vamos bien!")
            else:
                print(" Respuesta incorrecta ")
                print("\tGAME OVER ")
                print("\t☝ THANKS (｡◕‿◕｡)☝")
                print(" Hasta luego, regresa pronto   ")
                
                break
        


            print("\nPasaste al Segundo nivel")
            print("Empieza en")
            for i in range(0,5):
                print(5-i)
                sleep(1)
    
            for a in range(0,2):
                inicio=time.time()
    
            numazar=random.randint(1,10)
            numazar1=random.randint(1,10)
            numazar2=random.randint(1,10)
            r=float(input("¿ Cuánto es: "+str(numazar2)+"*"+str(numazar)+"+"+str(numazar1)+ " ? = "))
            final=time.time()
            tiempo=round(final-inicio,0)
            r1=numazar2*numazar+numazar1

            if r == r1:
                print("Respuesta correcta ◉‿◉ ,")
                if tiempo < 7:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                if tiempo >= 7 and tiempo < 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Lo puedes hacer mejor!")
                if tiempo >= 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Te falta practicar velocidad mental, pero vamos bien!")
            else:
                print(" Respuesta incorrecta ")
                print("\tGAME OVER ")
                print("\t☝ THANKS (｡◕‿◕｡)☝")
                print(" Hasta luego, regresa pronto   ")
                
                
                break
           

            numazar=random.randint(1,10)
            numazar1=random.randint(1,10)
            numazar2=random.randint(1,10)
            z=int(input("¿ Cuánto es: "+str(numazar2)+"+"+str(numazar)+"*"+str(numazar1)+ " ? = "))
            final=time.time()
            tiempo=round(final-inicio,0)

            z1=numazar2+numazar*numazar1

            if z == z1:
                print("Respuesta correcta ◉‿◉ ,")
                if tiempo < 7:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                if tiempo >= 7 and tiempo < 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Lo puedes hacer mejor!")
                if tiempo >= 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Te falta practicar velocidad mental, pero vamos bien!")
                
            else:
                print(" Respuesta incorrecta ")
                print("\tGAME OVER ")
                print("\t☝ THANKS (｡◕‿◕｡)☝")
             
                
                break


            numazar=random.randint(1,10)
            numazar1=random.randint(1,10)
            numazar2=random.randint(1,10)
            z=int(input("¿ Cuánto es: "+str(numazar2)+"+"+str(numazar)+"-"+str(numazar1)+ " ? = "))
            final=time.time()
            tiempo=round(final-inicio,0)

            z1=numazar2+numazar-numazar1

            if z == z1:
                print("Respuesta correcta ◉‿◉ ,")
                if tiempo < 7:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                if tiempo >= 7 and tiempo < 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Lo puedes hacer mejor!")
                if tiempo >= 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Te falta practicar velocidad mental, pero vamos bien!")
                
            else:
                print(" Respuesta incorrecta  ")
                print("\tGAME OVER ")
                print("\t☝ THANKS (｡◕‿◕｡)☝")
                print(" Hasta luego, regresa pronto   ")
                
                
                break


            numazar=random.randint(1,10)
            numazar1=random.randint(1,10)
            numazar2=random.randint(1,10)
            u=float(input("¿ Cuánto es: "+str(numazar2)+"*"+str(numazar)+"+"+str(numazar1)+ " ? = "))
            final=time.time()
            tiempo=round(final-inicio,0)
            u1=numazar2*numazar+numazar1

            if u == u1:
                print("Respuesta correcta ◉‿◉ ,")
                if tiempo < 7:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                if tiempo >= 7 and tiempo < 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Lo puedes hacer mejor!")
                if tiempo >= 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Te falta practicar velocidad mental, pero vamos bien!")
            else:
                print(" Respuesta incorrecta ")
                print("\tGAME OVER ")
                print("\t☝ THANKS (｡◕‿◕｡)☝")
                print(" Hasta luego, regresa pronto   ")
                
                
                break
                    
               
                
            print("\nPasaste al tercer nivel")
            print("Empieza en")
            
            for i in range(0,5):
                print(5-i)
                sleep(1)
            
            for a in range(0,2):
                inicio=time.time()
            
            numazar=[6,7,8]
            numazar1=[9,8,7]
            numazar2=[1,2,3]
            numazar3=[4,3,2]
            r=int(input("¿ Cuánto es: "+str(numazar[0])+"-"+str(numazar1[0])+"/"+str(numazar2[0])+"+"+str(numazar3[2])+ " ? = "))
            final=time.time()
            tiempo=round(final-inicio,0)
            r1=6-9/1+2
        
            if r == r1:
                print("Respuesta correcta ◉‿◉ ,")
                if tiempo < 7:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                if tiempo >= 7 and tiempo < 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Lo puedes hacer mejor!")
                if tiempo >= 16:
                     print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Te falta practicar velocidad mental, pero vamos bien!")
           
            else:
                print(" Respuesta incorrecta ")
                print("\tGAME OVER ")
                print("\t☝ THANKS (｡◕‿◕｡)☝")
                print(" Hasta luego, regresa pronto   ")
          
                
                break
          
        
            numazar=[6,7,8]
            numazar1=[9,8,7]
            numazar2=[1,2,3]
            numazar3=[4,3,2]
            z=int(input("¿ Cuánto es: "+str(numazar[1])+"-"+str(numazar1[0])+"*"+str(numazar2[2])+"/"+str(numazar3[1])+ " ? = "))
            final=time.time()
            tiempo=round(final-inicio,0)
            z1=7-9*3/3
        
            if z == z1:
                print("Respuesta correcta ◉‿◉ ,")
                if tiempo < 7:
                     print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                if tiempo >= 7 and tiempo < 16:
                     print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Lo puedes hacer mejor!")
                if tiempo >= 16:
                     print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Te falta practicar velocidad mental, pero vamos bien!")
           
                
            else:
                print(" Respuesta incorrecta ")
                print("\tGAME OVER ")
                print("\t☝ THANKS (｡◕‿◕｡)☝")
                print(" Hasta luego, regresa pronto   ")
             
                break
                
        
           
        
            numazar=[6,7,8]
            numazar1=[9,8,7]
            numazar2=[1,2,3]
            numazar3=[4,3,2]
            t=int(input("¿ Cuánto es: "+str(numazar[2])+"*"+str(numazar1[2])+"+"+str(numazar2[2])+"-"+str(numazar3[2])+ " ? = "))
            final=time.time()
            tiempo=round(final-inicio,0)
            t1=8*7+3-2
            if t == t1:
                print("Respuesta correcta ◉‿◉ ,")
                if tiempo < 7:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                if tiempo >= 7 and tiempo < 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Lo puedes hacer mejor!")
                if tiempo >= 16:
                    print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Te falta practicar velocidad mental, pero vamos bien!")
           
                
            else:
               print(" Respuesta incorrecta ")
               print("\tGAME OVER ")
               print("\t☝ THANKS (｡◕‿◕｡)☝")
               print(" Hasta luego, regresa pronto   ")

               break


            
            numazar=[6,7,8]
            numazar1=[9,8,7]
            numazar2=[1,2,3]
            numazar3=[4,3,2]
            z=int(input("¿ Cuánto es: "+str(numazar[1])+"-"+str(numazar1[1])+"*"+str(numazar2[2])+"/"+str(numazar3[0])+ " ? = "))
            final=time.time()
            tiempo=round(final-inicio,0)
            z1=7-8*3/4
        
            if z == z1:
                print("Respuesta correcta ◉‿◉ ,")
                if tiempo < 7:
                     print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Excelente!")
                if tiempo >= 7 and tiempo < 16:
                     print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Lo puedes hacer mejor!")
                if tiempo >= 16:
                     print("tu tiempo fue de:   " +str(tiempo)+"   segundos, ¡Te falta practicar velocidad mental, pero vamos bien!")
           
                print("\nGanaste el juego, mil de IQ")

            else:
                print(" Respuesta incorrecta ")
                print("\tGAME OVER ")
                print("\t☝ THANKS (｡◕‿◕｡)☝")
                print(" Hasta luego, regresa pronto   ")
             
                
            break
                            
    else:
        print("\t☝ THANKS (｡◕‿◕｡)☝")
        print(" Hasta luego, regresa pronto ")
   
    break