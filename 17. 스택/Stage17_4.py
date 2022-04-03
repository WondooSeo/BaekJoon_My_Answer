import sys

if __name__ == '__main__':
    while True:
        sentence = sys.stdin.readline().rstrip()
        if sentence == '.':
            break

        sentence = list(sentence)
        braket_stack = list()

        pivot = True

        for word in sentence:
            if word == '(' or word == '[':
                braket_stack.append(word)

            elif word == ')':
                if len(braket_stack) != 0 and braket_stack[-1] == '(':
                    braket_stack.pop()
                else:
                    pivot = False
                    break

            elif word == ']':
                if len(braket_stack) != 0 and braket_stack[-1] == '[':
                    braket_stack.pop()
                else:
                    pivot = False
                    break

            else:
                continue

        if len(braket_stack) == 0 and pivot:
            print('yes')
        else:
            print('no')
