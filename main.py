# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
# Part 1: Greet Template
def greet(name, greetings='Hello, <name>!'):
       print(f'{greetings}{name}!')
greet('Kazim', 'Hello, ')
# Part 2: Force
def force(mass, body='earth'):
    d = {
        'sun': 274.0,
        'jupiter': 24.92,
        'neptune': 11.15, 
        'saturn': 10.44, 
        'earth': 9.798,
        'uranus': 8.87, 
        'venus': 8.87, 
        'mars': 3.71,
        'mercury': 3.7,
        'moon': 1.62, 
        'pluto': 0.58
    }
    i = round((mass * d[body]), 1)
    return i
print(force(0.1, 'earth'))
# Part 3: Gravity
def pull(m1, m2 , d):
    G = 6.674  * (10 ** -11)
    x = G * ((m1 * m2) / d ** 2)
    return x
print(pull(800, 1500, 3))