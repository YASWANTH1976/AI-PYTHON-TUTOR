from typing import Dict, List
import random


class ExerciseGenerator:
    """Generates custom Python exercises based on topic and difficulty"""
    
    def __init__(self):
        self.exercises = self._load_exercises()
    
    def _load_exercises(self) -> Dict:
        """Database of exercises for each topic"""
        return {
            "variables": {
                "Easy": [
                    {
                        "prompt": "Create a variable called 'age' and set it to 25. Then print it.",
                        "solution": "age = 25\nprint(age)",
                        "test": "age == 25",
                        "hint": "Use = to assign a value to a variable"
                    },
                    {
                        "prompt": "Create three variables: name (string), age (int), and height (float). Print all three.",
                        "solution": "name = 'John'\nage = 25\nheight = 5.9\nprint(name, age, height)",
                        "test": "isinstance(name, str) and isinstance(age, int) and isinstance(height, float)",
                        "hint": "Strings need quotes, floats need decimal points"
                    }
                ],
                "Medium": [
                    {
                        "prompt": "Swap the values of two variables without using a third variable.",
                        "solution": "a = 5\nb = 10\na, b = b, a\nprint(a, b)",
                        "test": "True",
                        "hint": "Python allows tuple unpacking: a, b = b, a"
                    }
                ],
                "Hard": [
                    {
                        "prompt": "Create variables for a person's info and use type() to check each type.",
                        "solution": "name = 'John'\nage = 25\nheight = 5.9\nis_student = True\nprint(type(name), type(age), type(height), type(is_student))",
                        "test": "True",
                        "hint": "Use type() function to check data types"
                    }
                ]
            },
            "loops": {
                "Easy": [
                    {
                        "prompt": "Print numbers from 1 to 10 using a for loop",
                        "solution": "for i in range(1, 11):\n    print(i)",
                        "test": "True",
                        "hint": "range(1, 11) gives you 1 to 10"
                    },
                    {
                        "prompt": "Print all even numbers from 0 to 20",
                        "solution": "for i in range(0, 21, 2):\n    print(i)",
                        "test": "True",
                        "hint": "Use range(start, stop, step) with step=2"
                    }
                ],
                "Medium": [
                    {
                        "prompt": "Use a while loop to find the sum of numbers from 1 to 100",
                        "solution": "total = 0\ni = 1\nwhile i <= 100:\n    total += i\n    i += 1\nprint(total)",
                        "test": "total == 5050",
                        "hint": "Start with total=0, add i each iteration, increment i"
                    }
                ],
                "Hard": [
                    {
                        "prompt": "Create a nested loop to print a multiplication table (1-10)",
                        "solution": "for i in range(1, 11):\n    for j in range(1, 11):\n        print(f'{i} x {j} = {i*j}')",
                        "test": "True",
                        "hint": "Use two for loops, one inside the other"
                    }
                ]
            },
            "functions": {
                "Easy": [
                    {
                        "prompt": "Write a function called 'greet' that takes a name and returns 'Hello, [name]!'",
                        "solution": "def greet(name):\n    return f'Hello, {name}!'\n\nprint(greet('Alice'))",
                        "test": "greet('Alice') == 'Hello, Alice!'",
                        "hint": "Use def to define a function, use f-strings for formatting"
                    }
                ],
                "Medium": [
                    {
                        "prompt": "Write a function that returns True if a number is prime, False otherwise",
                        "solution": "def is_prime(n):\n    if n < 2:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True",
                        "test": "is_prime(7) == True and is_prime(4) == False",
                        "hint": "Check divisibility from 2 to square root of n"
                    }
                ],
                "Hard": [
                    {
                        "prompt": "Write a recursive function to calculate factorial of a number",
                        "solution": "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)\n\nprint(factorial(5))",
                        "test": "factorial(5) == 120",
                        "hint": "Base case: if n <= 1 return 1, Recursive case: n * factorial(n-1)"
                    }
                ]
            },
            "lists": {
                "Easy": [
                    {
                        "prompt": "Create a list of 5 fruits and print the third one",
                        "solution": "fruits = ['apple', 'banana', 'orange', 'grape', 'mango']\nprint(fruits[2])",
                        "test": "len(fruits) == 5",
                        "hint": "Remember: lists are zero-indexed, so third item is index 2"
                    }
                ],
                "Medium": [
                    {
                        "prompt": "Remove duplicates from a list: [1, 2, 2, 3, 4, 4, 5]",
                        "solution": "nums = [1, 2, 2, 3, 4, 4, 5]\nunique = list(set(nums))\nprint(unique)",
                        "test": "len(unique) == 5",
                        "hint": "Convert to set, then back to list"
                    }
                ],
                "Hard": [
                    {
                        "prompt": "Sort a list and find the median value",
                        "solution": "nums = [5, 2, 8, 1, 9]\nnums.sort()\nmedian = nums[len(nums)//2]\nprint(median)",
                        "test": "True",
                        "hint": "Sort first, then get middle element"
                    }
                ]
            }
        }
    
    def get_exercise(self, topic: str, difficulty: str = "Easy") -> Dict:
        """Get a random exercise for topic and difficulty"""
        topic = topic.lower()
        
        if topic in self.exercises and difficulty in self.exercises[topic]:
            exercises = self.exercises[topic][difficulty]
            return random.choice(exercises)
        
        return None
    
    def generate_custom_exercise(self, weak_topics: List[str]) -> Dict:
        """Generate exercise focused on weak topics"""
        if not weak_topics:
            topic = random.choice(list(self.exercises.keys()))
            difficulty = random.choice(["Easy", "Medium"])
        else:
            topic = random.choice(weak_topics).lower()
            difficulty = "Easy"
        
        return self.get_exercise(topic, difficulty)


# Global instance
exercise_gen = ExerciseGenerator()

def get_exercise(topic: str, difficulty: str = "Easy") -> Dict:
    return exercise_gen.get_exercise(topic, difficulty)

def generate_custom_exercise(weak_topics: List[str]) -> Dict:
    return exercise_gen.generate_custom_exercise(weak_topics)