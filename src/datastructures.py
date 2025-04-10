"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {"name":"John","last_name":"Jackson","age":33,"lucky_numbers":[7,13,22],"id":1},
            {"name":"Jane","last_name":"Jackson","age":35,"lucky_numbers":[10.14,3],"id":2},
            {"name":"Jimmy","last_name":"Jackson","age":5,"lucky_numbers":[5],"id":3}
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        name = member.get("first_name")
        age = member.get("age")
        lucky_numbers = member.get("lucky_numbers")
        

        if not name or not age or not lucky_numbers:
            return ""
        else:
            self._members.append({
                "name":name,
                "last_name":"Jackson",
                "age":age,
                "lucky_numbers":lucky_numbers,
                "id": self._generateId()
            })

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return
            
        return ""
        

    def get_member(self, id):
        for member in self._members:
            if id == member["id"]:
                return member
            
        return ""
                

        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        ## You have to implement this method
        ## Append the member to the list of _members
        pass

    def delete_member(self, id):
        ## You have to implement this method
        ## Loop the list and delete the member with the given id
        pass

    def get_member(self, id):
        ## You have to implement this method
        ## Loop all the members and return the one with the given id
        pass


    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members