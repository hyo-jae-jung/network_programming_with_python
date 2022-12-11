import socket

def convert_integer():
    data = 1234
    # 32-bit
    print('Original: {} => Long host byte order: {}, Network byte order: {}'.format(data,socket.ntohl(data),socket.htonl(data)))
    # 16-bit
    print('Original: {} => Short host byte order: {}, Network byte order: {}'.format(data,socket.ntohs(data),socket.htons(data)))

if __name__ == "__main__":
    convert_integer()
