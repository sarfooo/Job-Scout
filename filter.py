class Filter:
    def __init__(self, max_posting_age):
        self.max_posting_age = max_posting_age
        self.database_connection = None # Setup postgresql connection

    def filter_positions(self, positions, max_posting_age = 0):
        # Filter positions based post age
        positions = filter(lambda position: position["days_posted"] <= max_posting_age, positions)

        # Check if positions are stored already in database
        positions = filter(self.position_exists, positions)

        return positions

    def position_exists(position):
        # databae code goes in ehre
        pass