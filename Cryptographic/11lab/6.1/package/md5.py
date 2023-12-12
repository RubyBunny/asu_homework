import math


def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF


def md5(message) -> str:
    # Constants
    T = [int(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]
    s = (
        [[7, 12, 17, 22]] * 4
        + [[5, 9, 14, 20]] * 4
        + [[4, 11, 16, 23]] * 4
        + [[6, 10, 15, 21]] * 4
    )

    # Initialize variables
    A, B, C, D = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476
    message = bytearray(message)
    length = (8 * len(message)) & 0xFFFFFFFFFFFFFFFF
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0x00)
    message.extend(length.to_bytes(8, byteorder="little"))

    # Process message in 16-word blocks
    for i in range(0, len(message), 64):
        X = [
            int.from_bytes(message[i : i + 4], byteorder="little")
            for i in range(i, i + 64, 4)
        ]
        A_, B_, C_, D_ = A, B, C, D

        # Main loop
        for j in range(64):
            if j < 16:
                F = (B & C) | ((~B) & D)
                F_index = j
            elif j < 32:
                F = (D & B) | ((~D) & C)
                F_index = (5 * j + 1) % 16
            elif j < 48:
                F = B ^ C ^ D
                F_index = (3 * j + 5) % 16
            else:
                F = C ^ (B | (~D))
                F_index = (7 * j) % 16

            dTemp = D
            D = C
            C = B
            B = B + left_rotate(
                (A + F + T[j] + X[F_index]) & 0xFFFFFFFF, s[j % 4][j % 4]
            )
            A = dTemp

        # Update state
        A = (A + A_) & 0xFFFFFFFF
        B = (B + B_) & 0xFFFFFFFF
        C = (C + C_) & 0xFFFFFFFF
        D = (D + D_) & 0xFFFFFFFF

    # Output
    result = bytearray(A.to_bytes(4, byteorder="little"))
    result.extend(B.to_bytes(4, byteorder="little"))
    result.extend(C.to_bytes(4, byteorder="little"))
    result.extend(D.to_bytes(4, byteorder="little"))
    return result.hex()
