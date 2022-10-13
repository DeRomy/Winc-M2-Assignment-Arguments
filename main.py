# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line


# Part 1: Greet Template
def greet(name, template="Hello, <name>!"):
    return template.replace("<name>", name)


# Part 2: Force
def force(mass, body="earth"):
    gravities = {
        "sun": 274,
        "jupiter": 24.9,
        "neptune": 11.1,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6,
    }
    current_gravity = gravities.get(body)
    return round(mass * current_gravity, 1)


# Part 3: Gravity
def pull(m1, m2, d):
    G = 6.674 * 10**-11
    return G * ((m1 * m2) / d**2)


if __name__ == "__main__":
    # Part 1:
    print(greet("Doc"))
    print(greet("Bob", "What's up, <name>!"))

    # Part 2:
    print(force(48))
    print(force(48, "moon"))

    # Part 3:
    print(pull(0.1, 5.972 * 10**24, 6.371 * 10**6))
