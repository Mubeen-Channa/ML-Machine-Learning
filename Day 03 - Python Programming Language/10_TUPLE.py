
#   2.Tuple: Tuple are used to store multiple items in a single variable.
        # Immutable (can`t change defined values).
        # It allows duplicate elements.

        # Syntax: ()

        boys = ("Mubeen", "Siraj", "Manthar", "Aaqib")
        print(boys)       # Output: 'Mubeen', 'Siraj', 'Manthar', 'Aaqib'
        print(boys[1])    # Output: 'Siraj'
        print(boys[1:3])  # Output: 'Siraj', 'Manthar'

        # boys[0]  = "Channa"            # Error: Tuples are immutable
        # boys.append("Saifullah")   # 'tuple' object has no attribute 'append' bcz immutable

        # To add item in Tuple, first we need to convert Tuple in to List wiseversa
            students = ("Mubeen", "Siraj", "Manthar", "Aaqib")
            temp = list(students)
            temp.append("Saifullah")
            students = tuple(temp)