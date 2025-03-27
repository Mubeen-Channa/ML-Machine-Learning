
#   3.Sets: Sets are used to store multiple items in a single variable.
        # Mutable (changeable).
        # It did`nt allows duplicate elements.

        # Syntax: {}
        
        male = {"Mubeen", "Siraj", "Manthar", "Mubeen"}
        print(male)       # Output: 'Mubeen', 'Siraj', 'Manthar'
        print(male[1])    # Output: 'Siraj'
        print(male[1:3])  # Output: 'Siraj', 'Manthar'

        male[0]  = "Channa"       # Error: Tuples are immutable
        male.append("Saifullah")  # Add an item to the end