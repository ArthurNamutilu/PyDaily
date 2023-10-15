class Robot:
    """ Defines robot class with a class attribute containing the laws of robots """
    three_laws = (
        """A robot may not injure a human being or, through inaction, allow a 
        human being to come to harm.""",
        """A robot must obey the orders given to it by human beings, except where 
        such orders would conflict with the First Law.,""",
        """A robot must protect its own existence as long as such protection 
        does not conflict with the First or Second Law."""
    )

    def __int__(self, name, build_year):
        self.name = name
        self.build_year = build_year
