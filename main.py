# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'
def greet(name, greeting_template='Hello, <name>!'):
    greet = greeting_template.replace('<name>', name)
    return greet

# Part 2: Force
def force(mass, body='earth'):
    planets_gravity = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.15,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
    }
    force = mass * planets_gravity[body]
    return force

# Part 3: Gravity
def pull(m1, m2, d):
    pull = (6.674 * (10 ** -11)) * ((m1 * m2) / d **2)
    return pull
