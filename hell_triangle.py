class HellTriangle(object):
    def __init__(self, triangle):
        self.triangle = triangle
        self.max_total = None

    def set_max_total(self, max_total):
        """
            Set max total data.
        """
        self.max_total = max_total

    def set_triangle(self, triangle):
        """
            Set triangle data.
        """
        self.triangle = triangle

    def get_max_total(self):
        """
            Get triangle data.
        """
        return self.max_total

    def get_triangle(self):
        """
            Get triangle data.
        """
        return self.triangle

    def check_triangle(self, i=0):
        """
            Check the triangle is ok to Hell Triangle.
        """
        if type(self.triangle) != list or len(self.triangle) == 0 or 0 == len(self.triangle[i]) or i+1 != len(self.triangle[i]):
            return False
        return True

    def search(self, i=0, j=0, sum=0):
        """
            Depth-First Search for meet the max total Hell Triangle.

            Automated Tests
            >>> HellTriangle([[5]]).get_max()
            5
            >>> HellTriangle([[1],[1,1],[1,1,1],[1,1,1,1]]).get_max()
            4
            >>> HellTriangle([[-1],[-1,-1],[-1,-1,-1],[-1,-1,-1,-1]]).get_max()
            -4
            >>> HellTriangle([[6],[3,5],[9,7,1],[4,6,8,4]]).get_max()
            26
            >>> HellTriangle([[6],[2,3],[9,1,1],[9,1,1,1]]).get_max()
            26
            >>> HellTriangle([[9],[1,3],[1,1,9],[1,1,1,9]]).get_max()
            30
            >>> HellTriangle([[9],[1,1],[9,1,9],[9,1,1,9]]).get_max()
            28
            >>> HellTriangle([[5],[3,6],[9,7],[4,6,8,4]]).get_max()
            'Error. Not is a triangle.'
            >>> HellTriangle([]).get_max()
            'Error. Not is a triangle.'
            >>> HellTriangle([[],[],[]]).get_max()
            'Error. Not is a triangle.'
            >>> HellTriangle([[1],[1]]).get_max()
            'Error. Not is a triangle.'
        """
        if len(self.triangle) != i+1:
            if not self.check_triangle(i) or not self.check_triangle(i+1):
                return
            self.search(i+1, j, self.triangle[i][j]+sum)
            self.search(i+1, j+1, self.triangle[i][j]+sum)
        elif sum+self.triangle[i][j] > self.max_total:
            self.max_total = sum+self.triangle[i][j]
        return

    def get_max(self):
        """
            Get max total for Hell Triangle.
        """
        self.set_max_total(None)
        if self.check_triangle():
            self.search()
        if self.get_max_total() == None:
            return "Error. Not is a triangle."
        else:
            return self.get_max_total()
