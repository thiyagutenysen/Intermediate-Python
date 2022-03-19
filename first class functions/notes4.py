# You can return the function from a function
def logger(message):
    # function inside a function
    def log_message():
        print("loged message: ", message)

    return log_message  # bcz function name is also a python variable


function = logger("hi hello charlie kelly")
function()  # this function call remembered the message that we sent in the above line (this is what we call closure)

