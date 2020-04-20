import random

class Dice(object):

    """
    The Dice object contains a single numerical dice per instance
    Uses the random module for random generation.
    """

    def __init__(self,number):
        if not isinstance(number,int):
            raise TypeError
        self._number = number
    
    def roll(self,start = 1):

        """A standard dice roller

        Args:

            start (int): An optional argument if you want to only roll a 
                         specific part of a dice.
        
        Returns:

            output (int): A random number between start and the dice number.

        """

        output = random.randrange(start,self._number+1)
        return output

    def num_to_list(self):

        """A function that creates a list of all the faces of the dice

        Args:

            None
        
        Returns:

            temp_lst (list): A list containing all the faces of the dice

        """

        temp_lst = []
        for i in range(self._number):
            temp_lst.append(i+1)
        return temp_lst

    def roll_weighted(self,*args):

        """Rolls a weighted die
        
        Args:

            *args (int): The weights of the die faces
        
        Returns:
            result (int): The result of the weighted roll

        """

        num_lst = self.num_to_list() #list of all faces
        weighted_list = []
        dice_index = 0 #used to mark which face the program is looking at
        for arg in args:
            arg_counter = 1
            while arg_counter <= arg:
                weighted_list.append(num_lst[dice_index])
                arg_counter += 1
            arg_counter = 1
            dice_index += 1
        result = random.choice(weighted_list)
        return result



