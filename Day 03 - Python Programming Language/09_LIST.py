
#   1.List: Lists are used to store multiple items in a single variable.
        # Mutable (changeable).
        # It allows duplicate elements.

        # Syntax: []
        
        students = ["Mubeen", "Siraj", "Manthar", "Aaqib"]
        print(students)       # Output: 'Mubeen', 'Siraj', 'Manthar', 'Aaqib'
        print(students[1])    # Output: 'Siraj'
        print(students[1:3])  # Output: 'Siraj', 'Manthar'

        print(len(students))  # Output: 4

        students[0]  = "Channa"        # Change the first element
        students[-1] = "Abbasi"        # Change the last  element
        students.append("Saifullah")   # Add an item to the end
        students.removes("Saifullah")  # Remove an desire item

        students.pop()                 # Remove an last item
        students.clear()                 # Empty List


        # Multiple Varibale List
        mubeen_data = ["Mubeen", 23, "Larkana", "Software Engineer"]

        # Loop in List
        for i in mubeen_data:
        print(i)  # Print one by one from given list


        # Comparision in List
        boys = ["Mubeen", "Siraj", "Manthar", "Aaqib"]
        newlist = []

        for x in boys:
        if "n" in x:
            newlist.append(x)

        print(newlist)  # Output Mubeen, Manthar


        # Sort List
        boys.sort()
        print(boys)  # Output: "Aaqib", "Manthar", "Mubeen", "Siraj" 


        # Copy List
        male = boys.copy() 