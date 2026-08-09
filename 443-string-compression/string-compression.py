class Solution:
    def compress(self, chars: List[str]) -> int:
        # read=0
        # write=0
        # n=len(chars)
        # while read<n:
        #     char = chars[read]
        #     count=0
        # chars[write] = char
        # write+=1
        # if count>1:
        #     for digit in str(count):
        #         chars[write] = digit
        #         write+=1
        # return write
        write=0
        read=0
        n=len(chars)
        while read<n:
            char=chars[read]
            start=read
            while read<n and chars[read] == char:
                read += 1
            count = read - start
            chars[write] = char
            write += 1
            if count>1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write