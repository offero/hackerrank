def enum_dimensions(dims):
    """Enumerates all possible combinations of dimensions.
    """
    stack = [0] * len(dims)
    while stack[0] < dims[0]:
        ptr = len(dims)-1  # move to the end

        print(stack)
        stack[ptr] += 1

        while stack[ptr] >= dims[ptr]:
            if ptr == 0:
                return

            stack[ptr] = 0
            ptr -= 1
            stack[ptr] += 1

if __name__ == "__main__":
    dims = [1, 2, 1, 3]
    enum_dimensions(dims)
