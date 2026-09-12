class Solution(object):
    def isValid(self, s):
        st = []

        for char in s:

            if char == '(' or char == '{' or char == '[':
                st.append(char)

            else:
                if not st:
                    return False

                if char == ')' and st[-1] != '(':
                    return False

                if char == '}' and st[-1] != '{':
                    return False

                if char == ']' and st[-1] != '[':
                    return False

                st.pop()

        return len(st) == 0