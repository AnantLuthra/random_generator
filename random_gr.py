from datetime import datetime


class RandomGr:
    """
    This is a library like random which creates random values.
    """

    @staticmethod
    def random_generate() -> int:
        """
        This function returns a random integer
        """
        
        return int((datetime.now().second) * (45 + datetime.now().minute) / 
                 45 if datetime.now().second % 2 == 0 else (datetime.now().minute +
                        datetime.now().second))
