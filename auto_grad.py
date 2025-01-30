class AutoGrad:
    def __init__(self, value, gradient=None):
        """
        initialize an AutoDiff object.
        
        params:
            value: The value of the variable.
            gradient: The gradient of the operation (default is 1.0 for f(x) = x).
        """
        # complete me 
        self.value = value

    def __add__(self, b):
        if not isinstance(b, AutoDiff):
            b = AutoDiff(b, 0.0)
        return AutoDiff(self.value + b.value, #complete me)

    def __radd__(self, other):
        return self.__add__(other)

    # now, add support for other necessary operators

    # exp is not a built in python method
    @staticmethod # we do not require this, but it saves a bit of work for the computer
    def exp(x): #static method means that we do not need self for this function
        #complete me

        return AutoDiffVector(exp_value, exp_gradient) #still same structure here