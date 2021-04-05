"""
Lab 4:
"""

def main():
    feedback = get_feedback(15, 20)
    print(feedback)
    print(get_feedback(100, 200))
    print(get_feedback(65, 90))
    print(get_feedback(30, 30))

def get_feedback(mark, out_of):
    result = (mark / out_of) * 100
    if result >= 80:
        return "Excellent"
    
    elif result >= 60:
        return "Good"
    
    elif result >=50:
        return "Pass"

    else:
        return "Not a pass"


main()








