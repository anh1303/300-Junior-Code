class Solution(object):
    def decodeString(self, s):

        def decode(index):
            result = ""
            num = 0

            while index < len(s):

                if s[index].isdigit():

                    num = num * 10 + int(s[index])
                    index += 1

                elif s[index] == '[':

                    sub_result, index = decode(index + 1)

                    result += num * sub_result
                    num = 0

                elif s[index] == ']':

                    return result, index + 1

                else:

                    result += s[index]
                    index += 1

            return result, index

        result, _ = decode(0)

        return result