import math
def main():
    try:
    
    

            question = input("Please enter the name of the shape you want to calculate: ")
            while question.lower() not in ["square", "rectangle", "circle", "temperature in celsious", "temperature in fahrenheit", "isosceles triangle","equilateral triangle","right angle triangle","rhombus","parallelogram","trapezium","cube","cuboid"]:
                question = input("Please enter a valid shape or temperature value: ")
            if question.lower() == "square":
                side = float(input("Please enter the size of the side: "))
                square_result = square_size(side)
                question1 = input("Do you want to calculate its area? (yes/no): ")
                
                if question1.lower() == "yes":
                    print(f"Perimeter: {square_result[0]}, Area: {square_result[1]}")
                else:
                    print(f"Perimeter: {square_result[0]}")
            elif question.lower() == "rectangle":
                    length = float(input("Please enter the length of the rectangle: "))
                    breadth = float(input("Please enter the breadth of the rectangle: "))
                    rectangle_result = rectangle(length, breadth)
                    question2 = input("Do you also want to calculate its area? (yes/no): ")
                    if question2.lower() == "yes":
                        print(f"Perimeter: {rectangle_result[0]}, Area: {rectangle_result[1]}")
                    else:
                        print(f"Perimeter: {rectangle_result[0]}")
                    
            elif question.lower()=="circle":
                RAYON=float(input("please enter the rayon of the  circle"))
                circle_result=circle(RAYON)
                question3= input("Do you also want to calculate its area? (yes/no): ")
                if question3=="yes":
                    print(f"Perimeter: {circle_result[0]}, Area: {circle_result[1]}")
                else:
                    print(f"Perimeter: {circle_result[0]}")
                    
            elif question.lower()=="temperature in celsious":
                fahrenheit=float(input("please inter the temp in fahrenheit?:"))
                celsious_temp=Temperature_in_degrees(fahrenheit)
                print(f"the temperature is {celsious_temp} degree celsious")
            
            
            elif question.lower()=="temperature in fahrenheit":
                celsious=float(input("please enter the temp in  celsious?:"))
                fahren_temp=Temperature_in_fahrenheit(celsious)
                print(f"the temperature is {fahren_temp} degree fahrenheit")
                
                
            elif question.lower()=="isosceles triangle":
                base=float(input("please enter the base of the triangle?:"))
                height=float(input(" and the height?:"))
                Isosceles_Triangle_result=Isosceles_Triangle(base,height)
                question3 = input("Do you want to calculate its area? (yes/no): ")
                if question3.lower()=="yes":
                    print(f"Perimeter: {Isosceles_Triangle_result[0]}, Area: {Isosceles_Triangle_result[1]}")
                else:
                    print(f"Perimeter: {Isosceles_Triangle_result} ")
                    
                    
            elif question.lower()=="equilateral triangle":
                base2=float(input("please enter the base of the triangle?:"))
                height2=float(input("also enter the height?:"))
                Equilateral_triangle_result=Equilateral_triangle(base2,height2)
                question4=input("Do you want to calculate its area? (yes/no): ")
                if question4.lower()=="yes":
                    print(f"Perimeter: {Equilateral_triangle_result[2]}, Area: {Equilateral_triangle_result[1]}")
                else:
                    print(f"Perimeter: {Equilateral_triangle_result}")
                    
                    
                    
            elif question.lower()=="right angle triangle":
                base=float(input("please enter the base of the triangle?:"))
                heigth=float(input("please enter the heigth of the triangle?:"))
                
                    
                hypotenus=float(input("please engter the hypotenus of the triangle?:"))
                result=Right_Angle_Triangle(base,heigth,hypotenus)
                question=input("Do you want to calculate its area? (yes/no): ")
                if question.lower()=="yes":
                    print(f"the perimeter is{result[1]}, erea:{result[0]}")
                else:
                        print(f"Perimeter: {result[1]}")
                        
            elif question.lower()=="rhombus":
                first_D=float(input("please enter the first diameter of the rhombus ?:"))
                second_D=float(input("please enter the second diameter of the rhombus ?:"))
                side=float(input("please enter the side of the rhombus ?:"))
                result=rhombus(first_D,second_D,side)
                question=input("Do you want to calculate its area? (yes/no): ")
                if question.lower()=="yes":
                    print(f"the perimeter is{result[1]}, erea:{result[0]}")
                else:
                        print(f"Perimeter: {result[1]}")
                        
                        
            elif question.lower()=="parallelogram":
                base=float(input("please enter the base of the parallelogram ?:"))
                heigth=float(input("please enter the heigth of the parallelogram ?:"))
                length=float(input("please enter the length of the parallelogram  ?:"))
                result=rhombus(base,heigth,length)
                question=input("Do you want to calculate its area? (yes/no): ")
                if question.lower()=="yes":
                    print(f"the perimeter is{result[1]}, erea:{result[0]}")
                else:
                        print(f"Perimeter: {result[1]}")
                        
                        
            elif question.lower()=="trapezium":
                heigth=float(input("please enter the heigth  of the trapezium ?:"))
            
                side_a=float(input("please enter the side a  of the trapezium ?:"))
                side_b=float(input("please enter the side b of the trapezium ?:"))
                side_c=float(input("please enter the side c of the trapezium ?:"))
                side_d=float(input("please enter the side d of the trapezium ?:"))
                
                result=trapezium(heigth,side_a,side_b,side_c,side_d)
                question=input("Do you want to calculate its area? (yes/no): ")
                if question.lower()=="yes":
                    print(f"the perimeter is{result[1]}, erea:{result[0]}")
                else:
                        print(f"Perimeter: {result[1]}")
                        
            elif question.lower()=="cube":
                a=float(input("please enter the side of the cube?:"))
                result=Cube(a)
                question=input("tell me now in which mesurement do you want the result? : ")
                if question.lower()=="Volume Cubic":
                    print(f"{result[0]}")
                    
                elif question.lower()=="Lateral Surface Area Square units":
                    print(result[1])
                    
                else:
                    print(result[2])
                    
            elif question.lower()=="cuboid":
                #length,base,heigth
                length=float(input("please enter the length of the cuboid?:"))
                base=float(input("please enter the base of the cuboid?:"))
                heigth=float(input("please enter the height of the cuboid ?:"))
                
                result=Cuboid(length,base,heigth)
                question=input("tell me now in which mesurement do you want the result? : ")
                if question.lower()=="volume cubic":
                    print(f"{result[0]}")
                    
                elif question.lower()=="Lateral Surface Area Square units":
                    print(result[1])
                    
                else:
                    print(result[2])
                
            
                
                        
                        

    except Exception as e:
      print(f"An error occurred while running the code: {e}")
            


def square_size(side):
    square_peremiter=side*4
    square_area=side**2
    
    return square_peremiter,square_area
    
def rectangle(length,breath):
        peremter_rectangle= 2*(length+ breath)
        
        erea_rectangle=length*breath
        
        return peremter_rectangle,erea_rectangle

def circle(RAYON):
       
        circle_peremeter=2*3.14*RAYON
        circle_erea=3.14*RAYON**2
        
        return circle_peremeter,circle_erea

def Temperature_in_degrees(fahrenheit):
    result=5/9*(fahrenheit-32)
    return result
   
   
def Temperature_in_fahrenheit(celsious):
    fahrenheit=celsious*5/9
    return fahrenheit


#def Scalene_Triangle():
#    pass


def Isosceles_Triangle(base,height):
    Isosceles_Triangle_peremeter=  1/2 * (base + base + height)
    Isosceles_Triangle_erea=0.5*base+height
    return Isosceles_Triangle_peremeter,Isosceles_Triangle_erea


# Area of Equilateral Triangle = ¼(√3a2)
#Area of Triangle = ½ × base × height

def Equilateral_triangle(base2,height2):
    
    Area_of_Triangle =1/2*base2*height2
    Area_of_an_Equilateral_Triangle= 1/4*math.sqrt(3)*base2**2
    Perimeter=3*base2
    return Perimeter,Area_of_an_Equilateral_Triangle,Area_of_Triangle


def Right_Angle_Triangle( base, heigth,hypotenus):
    area=1/2*(base*heigth)
    
    perimeter=base=heigth+hypotenus
    hypotenus=math.sqrt(base**2+heigth**2)
    return area, perimeter

def rhombus(diameter_one,diameter_two,side):
    area=1/2*(diameter_one*diameter_two)
    perimeter=side*4
    return area,perimeter

def parallelogram( base,heigth,length):
    area= base*heigth
    perimeter=2*(length+base)
    return area,perimeter

def trapezium(heigth,side_a,side_b,side_c,side_d):
    area=1/2*heigth*(side_a+side_b)
    perimeter=side_a,side_b,side_c,side_d
    return area,perimeter


def Cube(side):
    Volume_Cubic_units=side**3
    Lateral_Surface_Area_Square_units= 4*(side**2)
    Total_Surface_Area_Square_units=6*(side**2)
    return Volume_Cubic_units,Lateral_Surface_Area_Square_units,Total_Surface_Area_Square_units

def Cuboid(length,base,heigth):
    # 2h(l + b)
    v_cubic=length*base*heigth
    Lateral_Surface_Area=2*heigth*(length+base)
    #2 (lb +bh +hl)
    Total_Surface_Area =2*(length*base+base*heigth+heigth*length)
    return v_cubic,Lateral_Surface_Area,Total_Surface_Area
    



if __name__ == "__main__":
    main()
    
  
   

            
    
    
    
        
        
        


        
    

        
    
    
    
    
    



