# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Part 1: Greet Template
def greet (name, template = 'Hello, <name>!'):
    # check if <name> is inside the template
    if template.find("<name>") != -1:
        # find start and end character
        start = template.find("<")
        end = template.find(">")
   
        # use slicing to replace <name>
        greet = template[:start] + name + template[end +1:]
    else:
        # return the template (or return nothing? Not clear based on exercise)
        greet = template
    return greet


print(greet('Bo'))
print(greet('Bob', "What's up, <name>!"))
print(greet('Bob', "What's up?"))

# Part 2: Force
def force(mass, body = 'earth'):
    # create dictonary of bodies
    bodies = {  'sun':'274.0','jupiter':'24.9','neptune':'11.2','saturn':'10.4',
                'earth': '9.8','uranus':'8.9','venus':'8.9',
                'mars':'3.7','mercury':'3.7','moon':'1.6','pluto':'0.6'}

    # get gravity for body
    gravity = float(bodies.get(body))
   
    # calculate force
    force = mass * gravity
    return force

print(force(4))
print(force(4,'sun'))

# Part 3: Gravity
def pull(m1,m2,d):
    # pull = G × ((m1×m2)/d2)
    
    G = 6.674 * 10**(-11)
    force = G*((m1*m2)/d**2)
    return force

print(pull(800,1500,3))
print(pull(0.1,5.972*10**24,6.371*10**6))