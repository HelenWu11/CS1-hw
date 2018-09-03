import math
def find_sphere_volume(radius):
    return 4/3*math.pi*radius**3
def find_cube_volume(side):
    return side**3
R = input("Enter the side length of the cube (in.) => ")
print(R)
r = input("Enter the radius of the gum ball (in.) => ")
print(r)
a = float(R)/(float(r)*2)
print("A box of side length",float(R),"will hold",int(a)**3,"gum balls of radius",str(float(r))+".")
print("The gum balls will take up {:.2f}".format(int(a)**3*float(find_sphere_volume(float(r)))),"in^3")
print("of the total volume of {:.2f}".format(find_cube_volume(float(R))),\
      "in^3 or {:.2f}".format(float(int(a)**3*float(find_sphere_volume(float(r))))/find_cube_volume(float(R))*100)+"%")
print("A sphere with a diameter of",float(R),"would have volume {:.2f}".format(find_sphere_volume(float(R)/2)),"in^3")
print("It would hold",int(find_sphere_volume(float(R)/2)*(float(int(a)**3*float(find_sphere_volume(float(r))))/find_cube_volume(float(R)))/find_sphere_volume(float(r))),"gum balls at the same density.")