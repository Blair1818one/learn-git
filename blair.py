# pops sky
def investigation_scene():
    print("you arrive at a dimly lit room with clues scatterd around.")
    if flashlight_available:
      print("you can you see bettre with your flashlight.")
    print("you find a note on the table.")
    if flashlight_available:
       print("The note reads, 'the code to the safe is 4732.'")
    else:
      print("the note reads, 'you need to find the flashlight first.'")

def open_safe(code):
    if code == 4732:
     print("The safe opens, revealing a hedden treasure.")
     print("congratulations! you solved the mystery.")
    else:
        print("The safe emains locked. Try again.")
flashlight_available = True

investigation_scene()
safe_code =4732
open_safe(safe_code) 

def display_student_info(name, age):
    print("students Name:", name)
    print("student Age:", age)
    if age < 18:
       print("status: Minor")
    else:
       print("status: Adult") 
       return
    
student_name = "Alice"
student_age = 20    

display_student_info(student_name, student_age)

def calculate_average(numbers):
    sum = 0
    for number in numbers:
        sum+= number
    average =sum / len(numbers)
    return average
    
numbers = [12,8,16,4,20]
average = calculate_average(numbers)
print("Average:", average)
