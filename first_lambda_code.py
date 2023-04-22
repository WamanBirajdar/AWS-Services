import json

def sum_numbers(a,b):
    return a+b
    
def lambda_handler(event, context):
    # TODO implement
    print(event)
    print(context)
    print("Hello This is my first lambda function")
    print("Sum of a,b is =",sum_numbers(2,5))
